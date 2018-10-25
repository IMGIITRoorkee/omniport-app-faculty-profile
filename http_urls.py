from django.conf.urls import url, include
from rest_framework import routers
import inflection
from faculty_profile.views import viewset_dict

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
]

router = routers.DefaultRouter()

for model in models:
    router.register(
        inflection.underscore(model),
        viewset_dict[model],
        base_name=model
    )

urlpatterns = [
    url(r'^', include(router.urls)),
]
