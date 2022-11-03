from django.conf.urls import url, include
from django.urls import path
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
    url(r'rearrange', DragAndDropView.as_view()),
    url(r'cms', CMSIntegrationView.as_view()),
    url(r'csv/download', WriteAppendMultipleObjects.as_view(
        actions={'get': 'download'})
    ),
    url(r'csv/affordances', WriteAppendMultipleObjects.as_view(
        actions={'get': 'affordance'})
    ),
    url(r'csv', WriteAppendMultipleObjects.as_view(actions={'post': 'post'})),
    path('data/<int:employee_id>/', DataLeakView.as_view()),
    path('data', DataLeakView.as_view()),
    url(r'^', include(router.urls)),
]
