import swapper
import requests
import logging
import csv
import pandas as pd
import mimetypes
from pandas.io.parsers import ParserError

from django.db import transaction, IntegrityError
from django.core.exceptions import (
    ObjectDoesNotExist,
    ValidationError,
    ImproperlyConfigured,
    FieldDoesNotExist
)
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view, permission_classes

from kernel.managers.get_role import get_role
from omniport.settings.configuration.base import CONFIGURATION

from faculty_profile.serializers import serializer_dict
from faculty_profile.permissions.is_faculty_member import IsFacultyMember
from faculty_profile.permissions.has_data_leak_rights import CanDataLeak

logger = logging.getLogger('faculty_profile')

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
    'Miscellaneous': None,
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
            return Model.objects.filter(faculty_member=faculty_member).order_by('priority')

        def exception_handler(func):
            """
            Decorator to add exception handling to create and update methods.
            :param func: function to apply this decorator over

            :return: a function which raises an error if the passed function
            raises an error
            """

            def raise_error(*args, **kwargs):
                """
                Wrapper function to raise error
                """

                try:
                    return func(*args, **kwargs)
                except IntegrityError as error:
                    return Response(
                        {'Fatal error': [error.__cause__.diag.message_detail]},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                except ValidationError as error:
                    return Response(
                        error.message_dict,
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return raise_error

        @exception_handler
        def create(self, request, *args, **kwargs):
            """
            Modify create method to catch errors
            """

            return super().create(request, *args, **kwargs)

        def perform_create(self, serializer):
            """
            modifying perform_create for all the views to get FacultyMember
            instance from request
            """
            faculty_member = get_role(self.request.person, 'FacultyMember')
            serializer.save(faculty_member=faculty_member)

        @exception_handler
        def update(self, request, *args, **kwargs):
            """
            Modify update method to catch errors
            """

            return super().update(request, *args, **kwargs)

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
            logger.info('MultiValueDictKeyError has occurred when the user tried\
                    to upload the profile image')
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
            logger.info('MultiValueDictKeyError has occurred when the user tried\
                    to upload the profile image')
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


class CMSIntegrationView(APIView):
    """
    This view interacts with CMS Integration. If you don't have a CMS
    integrated, you don't need this view
    """

    CMS = CONFIGURATION.integrations.get('cms', False)

    def get(self, request):
        """
        Returns whether CMS configuration exists or not
        :return: whether CMS configuration exists or not
        """

        if self.CMS:
            attributes = [
                self.CMS.get('host'),
                self.CMS.get('facapp_token'),
                self.CMS.get('faculty_url'),
            ]
            if all(attributes):
                return Response(
                    'CMS configuration detected',
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    (
                        'CMS falsely configured. Please provide `host`,'
                        '`facapp_token` and `faculty_url` in the configuration'
                    ),
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
        else:
            return Response(
                'You probably do not need faculty\'s information published',
                status=status.HTTP_404_NOT_FOUND,
        )

    def post(self, request):
        """
        Forwards request to CMS for further processing.
        """

        data = {}
        data['username'] = request.person.user.username
        data['token'] = self.CMS.get('facapp_token')

        user = request.user.username

        host = self.CMS.get('host')
        faculty_url = self.CMS.get('faculty_url')
        action = request.data.get('action')
        url = f'{host}{faculty_url}{action}'
        
        try:
            # Remove `verify=False` when CMS adds chain certificate
            response = requests.post(url, data, timeout=5, verify=False)
        except:
            logger.info('CMS is not responding to requests')
            return Response(
                'Connection Refused',
                status=status.HTTP_502_BAD_GATEWAY,
            )

        if response.status_code == 205:
            logger.info(f'{user} successfully made a {action} request')
            return Response(response.json())
        elif response.status_code == 403:
            logger.warning(f'{user} made a forbidden {action} request')
            return Response(
                'Authorization Error',
                status=status.HTTP_403_FORBIDDEN,
            )
        elif response.status_code == 404:
            logger.warning(f'{user} does not have a faculty instance')
            return Response(
                'Faculty not found',
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            logger.warning('CMS responded with an unidentified error')
            return Response(
                'Unidentified Error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class WriteAppendMultipleObjects(viewsets.ViewSet):
    """
    API endpoint that allows importing and exporting csv files
    """

    exclude_fields = [
        'id',
        'datetime_created',
        'datetime_modified',
        'faculty_member',
        'file',
        'paper'
    ]

    permission_classes = [IsFacultyMember]

    def download(self, request, *args, **kwargs):
        """
        Returns a blank csv file for given model
        :return: a blank csv file for given model
        """

        username = request.user.username
        model_name = request.GET.get('model')
        if model_name is None:
            logger.warning(
                f'{username} didn\'t send model parameter in get request.'
            )
            return Response(
                { 'Error': ['Model parameter is missing.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            Model = swapper.load_model('faculty_biodata', model_name)

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = (
                f'attachment; filename={model_name}.csv'
            )

            all_fields = Model._meta.get_fields()
            column_headers = [
                field.name
                for field in all_fields
                if field.name not in self.exclude_fields
            ]

            writer = csv.writer(response)
            writer.writerow(column_headers)

            return response
        except ImproperlyConfigured:
            logger.warning(
                f'{username} sent an invalid model in get request.'
            )
            return Response(
                { 'Invalid model': ['Model doesn\'t exists.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def affordance(self, request, *args, **kwargs):
        """
        Returns an array of affordances of given model
        """

        username = request.user.username
        model_name = request.GET.get('model')
        if model_name is None:
            logger.warning(
                f'{username} didn\'t send model parameter in get request.'
            )
            return Response(
                { 'Error': ['Model parameter is missing.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            Model = swapper.load_model('faculty_biodata', model_name)
            all_fields = Model._meta.get_fields()

            affordances = [{
                (f'{field.name} (required)')
                if not field.blank and field._get_default() == ''
                else (field.name)
                :
                (field.description % field.__dict__)
            } for field in all_fields
            if field.name not in self.exclude_fields]

            return Response(affordances, status=status.HTTP_200_OK)
        except ImproperlyConfigured:
            logger.warning(
                f'{username} sent an invalid model in get request.'
            )
            return Response(
                { 'Invalid model': ['Model doesn\'t exists.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request, *args, **kwargs):
        """
        Adds data from uploaded file in corresponding model
        """

        username = request.user.username
        uploaded_file = request.FILES.get('file')
        if uploaded_file is None:
            logger.warning('File is missing in post request.')
            return Response(
                { 'Error': ['No file uploaded.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if it is parseble by read_csv()
        valid_mimetypes = ['text/csv']
        file_ext = mimetypes.guess_type(uploaded_file.name)[0] # Get the type
        if file_ext not in valid_mimetypes:
            logger.warning(f'{username} tried to upload an invalid file.')
            return Response(
                { 'Invalid file': ['Only CSV files are allowed.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = request.data
        model_name = data.get('model')

        # Check if model parameter is valid
        if model_name is None:
            logger.warning(
                f'{username} didn\'t send model parameter in get request.'
            )
            return Response(
                { 'Error': ['Model parameter is missing.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            Model = swapper.load_model('faculty_biodata', model_name)
            all_fields = Model._meta.get_fields()
            column_headers = [
                field.name
                for field in all_fields
                if field.name not in self.exclude_fields
            ]
        except ImproperlyConfigured:
            logger.warning(
                f'{username} sent an invalid model in post request.'
            )
            return Response(
                { 'Invalid model': ['Model doesn\'t exists.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = serializer_dict[model_name]
        faculty_member = get_role(self.request.person, 'FacultyMember')

        try:
            df = pd.read_csv(uploaded_file, encoding='utf-8', keep_default_na=False)

            # Check if column headers are correct of not
            data_headers = df.columns.values.tolist()
            if not column_headers == data_headers:
                raise TypeError

            # Remove keys which doesn't have any value, from all the objects
            actual_data = [{
                key: value.strip() if isinstance(value, str) else value
                for key, value in obj.items() if len(str(value)) > 0
            } for obj in df.to_dict('records')]

            with transaction.atomic():
                uploaded_type = data.get('upload_type')

                # Check if upload type is valid
                valid_types = ['append', 'new']
                if uploaded_type is None:
                    logger.warning('Upload type parameter is missing.')
                    return Response(
                        { 'Error': ['Upload type parameter is missing.'] },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                if uploaded_type not in valid_types:
                    logger.warning(f'{username} sent an invalid upload type.')
                    return Response(
                        { 'Error': ['Upload type doesn\'t exists.'] },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                # Parse data and add instances to model
                if uploaded_type == 'new':
                    Model.objects.filter(faculty_member=faculty_member) \
                    .all() \
                    .delete()
                # This is necessary because `bulk_create` doesn't validate
                # data itself
                instances = []
                for vals in actual_data:
                    instance = Model(faculty_member=faculty_member, **vals)
                    instance.full_clean()
                    instances.append(instance)
                logger.info(
                    f'{username} uploaded data in {model_name} via csv file.'
                )
                Model.objects.bulk_create(instances)
        # read_csv() cannot parse if the uploaded file doesn't have 'utf-8'
        # encoding.
        except (ParserError, UnicodeDecodeError):
            logger.warning(f'{username} tried to upload a unparsable file.')
            return Response(
                {
                    'Error': [
                        'You have uploaded a malformed file that isn\'t' \
                        'parsable.'
                    ],
                    'Suggestion': [
                        'You can use the given sample file to add your data.'
                    ]
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValidationError as error:
            logger.warning('Uploaded file contains invalid data.')
            return Response(
                error.message_dict,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except TypeError:
            logger.warning('Column headers doesn\'t match to model fields.')
            return Response(
                {
                    'Error': [
                        'Uploaded file has incorrect column headers.'
                    ],
                    'Suggestion': [
                        'You can use the given sample file to add your data.'
                    ]
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        objects = Model.objects.filter(faculty_member=faculty_member)
        return Response(
            serializer(objects.order_by('priority'), many=True).data
        )

class DataLeakView(APIView):
    """
    Endpoint to get faculty data using their employeeId
    """

    permission_classes = (CanDataLeak,)
    pagination_class = None

    def get(self, request, *args, **kwargs):
        employee_id = kwargs.get('employee_id')
        if employee_id is None:
            return Response(
                { 'Error': ['Faculty id parameter is missing.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            FacultyMember = swapper.load_model('kernel', 'facultyMember')
            faculty_member = FacultyMember.objects.get(employee_id=employee_id)
            response = {}
            for key in viewset_dict:
                Model = models[key]
                serializer = serializer_dict[key]
                # Profile doesn't have visibility field
                if key == 'Profile':
                    objects = Model.objects.filter(faculty_member=faculty_member)
                else:
                    objects = Model.objects.filter(
                        faculty_member=faculty_member).filter(visibility=True)
                response[key] = serializer(objects, many=True).data
            return Response(response, status=status.HTTP_200_OK)
        except FacultyMember.DoesNotExist:
            return Response(
                { 'Error': ['Invalid Faculty id.'] },
                status=status.HTTP_400_BAD_REQUEST,
            )
