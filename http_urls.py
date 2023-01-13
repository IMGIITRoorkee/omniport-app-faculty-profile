from django.conf.urls import include
from django.urls import path, re_path
from rest_framework import routers
import inflection
from faculty_profile.views import (
    CMSIntegrationView,
    DragAndDropView,
    AddressViewSet,
    WriteAppendMultipleObjects,
    DataLeakView,
    viewset_dict,
)

models = [
    'Profile',
    'Education',
    'Honour',
    'Visit',
    'Collaboration',
    'Project',
    'AssociateScholar',
    'Supervision',
    'TeachingEngagement',
    'Event',
    'Interest',
    'AdministrativePosition',
    'ProfessionalBackground',
    'Membership',
    'Book',
    'Paper',
    'Miscellaneous'
]

router = routers.DefaultRouter()

for model in models:
    router.register(
        inflection.underscore(model),
        viewset_dict[model],
        basename=model
    )

router.register(r'address',AddressViewSet, basename='address')

urlpatterns = [
    re_path(r'rearrange', DragAndDropView.as_view()),
    re_path(r'cms', CMSIntegrationView.as_view()),
    re_path(r'csv/download', WriteAppendMultipleObjects.as_view(
        actions={'get': 'download'})
    ),
    re_path(r'csv/affordances', WriteAppendMultipleObjects.as_view(
        actions={'get': 'affordance'})
    ),
    re_path(r'csv', WriteAppendMultipleObjects.as_view(actions={'post': 'post'})),
    re_path('data/<int:employee_id>/', DataLeakView.as_view()),
    re_path('data', DataLeakView.as_view()),
    re_path(r'^', include(router.urls)),
]
