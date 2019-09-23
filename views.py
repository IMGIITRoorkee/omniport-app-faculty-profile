import swapper

from django.db import transaction
from django.db.models import FieldDoesNotExist
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser

from kernel.managers.get_role import get_role

from faculty_profile.serializers import serializer_dict
from faculty_profile.permissions.is_faculty_member import IsFacultyMember

viewset_dict = {
    'Profile':None,
    'Education':None,
    'Honour':None,
    'Visit':None,
    'Collaboration':None,
    'Project':None,
    'AssociateScholar':None,
    'Supervision':None,
    'TeachingEngagement':None,
    'Event':None,
    'Interest':None,
    'AdministrativePosition':None,
    'Membership':None,
    'Book':None,
    'Paper':None,
}

def return_viewset(class_name):
    class Viewset(ModelViewSet):
        """
        API endpoint that allows models to be viewed or edited.
        """
        serializer_class = serializer_dict[class_name]
        permission_classes = (IsFacultyMember, )
        pagination_class = None
        filter_backends = tuple()

        def get_queryset(self):
            Model = swapper.load_model('faculty_biodata', class_name)
            faculty_member = get_role(self.request.person, 'FacultyMember')
            return Model.objects.filter(faculty_member=faculty_member)

        def perform_create(self, serializer):
            """
            modifying perform_create for all the views to get FacultyMember
            instance from request
            """
            faculty_member = get_role(self.request.person, 'FacultyMember')
            serializer.save(faculty_member=faculty_member)
            
    return Viewset


for key in viewset_dict:
    viewset_dict[key] = return_viewset(key)

models = {}
for key in viewset_dict:
    models[key] = swapper.load_model('faculty_biodata', key)

class ProfileViewset(ModelViewSet):
    """
    API endpoint that allows models to be viewed or edited.
    """

    serializer_class = serializer_dict['Profile']
    permission_classes = (IsFacultyMember, )
    pagination_class = None
    filter_backends = tuple()

    def get_queryset(self):
        Model = swapper.load_model('faculty_biodata', 'Profile')
        try:
            faculty_member = get_role(self.request.person, 'FacultyMember')
        except:
            return []
        profile = Model.objects.order_by('-id').filter(faculty_member=faculty_member)
        if len(profile) == 0:
            profile = Model.objects.create(faculty_member=faculty_member, handle=self.request.person.user.username, description="Faculty member at IITR")
            profile.save()
            return [profile]
        return profile
    
    def create(self, request, *args, **kwargs):
        """
        Modifying create method to add functionality of adding profile image
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        person = request.person 
        try: 
            img_file = request.data['image']
            if img_file is None or img_file == "null":
                person.display_picture = None
                person.save()  
            else:
                person.display_picture.save(img_file.name, img_file, save=True)
        except MultiValueDictKeyError: 
            pass
        try:
            data['displayPicture'] = request.person.display_picture.url       
        except ValueError:
            data['displayPicture'] = None
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        """
        modifying perform_create for all the views to get Student
        instance from request
        """

        faculty_member = get_role(self.request.person, 'FacultyMember')
        serializer.save(faculty_member=faculty_member)

    def update(self, request, *args, **kwargs):
        """
        modifying update function to change image field to null in case of deleting the profile image
        """

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        parser_class = (MultiPartParser, )
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        data = serializer.data
        try:
            img_file = request.data['image']
            person = request.person
            if img_file is None or img_file == "null":
                person.display_picture = None
                person.save()
            else:
                person.display_picture.save(img_file.name, img_file, save=True)
        except MultiValueDictKeyError:
            pass
        try:
            data['displayPicture'] = request.person.display_picture.url       
        except ValueError:
            data['displayPicture'] = None
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        """
        modifying destroy method to remove only the resume field
        """

        instance = self.get_object()
        instance.resume = None
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[])
    def handle(self, request, pk=None):
        """
        A view to check whether a handle is already taken
        """
        try:
            profile = models['Profile'].objects.get(handle=pk)
            print(profile)
            if profile is not None:
                return Response("no")
        except:
            return Response("yes")
        return Response("yes")
        
viewset_dict["Profile"] = ProfileViewset


class DragAndDropView(APIView):
    """
    API endpoint that allows the changing if the ordering of the models
    """

    permission_classes = (IsFacultyMember, )
    pagination_class = None
    filter_backends = ()

    @transaction.atomic
    def post(self, request):
        data = request.data
        faculty_member = get_role(self.request.person, 'FacultyMember')
        model_name = data['model']
        Model = models[model_name]
        objects = Model.objects.order_by('id').filter(faculty_member=faculty_member)
        serializer = serializer_dict[model_name]
        priority_array = data['order']
        if(len(priority_array) == len(objects)):
            order = dict()
            for i in range(len(priority_array)):
                order[priority_array[i]] = i + 1
            for obj in objects:
                obj.priority = order[obj.id]
                obj.save()
        return Response(serializer(objects.order_by('priority'), many=True).data)