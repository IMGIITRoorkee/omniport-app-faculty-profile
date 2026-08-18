from django.urls import path

from faculty_profile.consumers import EnablePublishConsumer

urlpatterns = [
    path('cms/', EnablePublishConsumer)
]
