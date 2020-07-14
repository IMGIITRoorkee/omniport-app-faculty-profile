from django.conf.urls import url, include
from rest_framework import routers
import inflection
from faculty_profile.views import (
    CMSIntegrationView,
    DragAndDropView,
    WriteAppendMultipleObjects,
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

urlpatterns = [
    url(r'rearrange', DragAndDropView.as_view()),
    url(r'cms', CMSIntegrationView.as_view()),
    url(r'csv', WriteAppendMultipleObjects.as_view()),
    url(r'^', include(router.urls)),
]
