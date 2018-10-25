import swapper

from rest_framework.viewsets import ModelViewSet

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
