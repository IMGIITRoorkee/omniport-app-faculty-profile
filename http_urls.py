from django.conf.urls import url, include
from rest_framework import routers
from faculty_profile.views import (
#     EducationalDetailsViewSet,
    HonorViewSet,
#     VisitViewSet,
#     CollaborationViewSet,
#     ResearchProjectViewSet,
#     ScholarMapViewSet,
#     SupervisionViewSet,
#     TeachingEngagementViewSet,
#     ConferenceViewSet,
#     GuestLectureViewSet,
#     ShortTermCourseViewSet,
#     SpecialLectureViewSet,
#     InterestViewSet,
#     MiscellaneousViewSet,
#     AdministrativePositionViewSet,
#     MembershipViewSet,
#     BookViewSet,
#     PaperViewSet,
)

router = routers.DefaultRouter()

# router.register(r'educational_detail',EducationalDetailsViewSet, base_name = "educational_detail")
router.register(r'honor',HonorViewSet, base_name = "honor")
# router.register(r'visit',VisitViewSet, base_name = "visit")
# router.register(r'collaboration',CollaborationViewSet, base_name = "collaboration")
# router.register(r'research_project',ResearchProjectViewSet, base_name = "research_project")
# router.register(r'scholar_map',ScholarMapViewSet, base_name = "scholar_map")
# router.register(r'supervision',SupervisionViewSet, base_name = "supervision")
# router.register(r'teaching_engagement',TeachingEngagementViewSet, base_name = "teaching_engagement")
# router.register(r'conference',ConferenceViewSet, base_name = "conference")
# router.register(r'guest_lecture',GuestLectureViewSet, base_name = "guest_lecture")
# router.register(r'short_term_course',ShortTermCourseViewSet, base_name = "short_term_course")
# router.register(r'special_lecture', SpecialLectureViewSet, base_name = "special_lecture")
# router.register(r'interest', InterestViewSet, base_name = "interest")
# router.register(r'administrative_position', AdministrativePositionViewSet, base_name = "administrative_positions")
# router.register(r'membership', MembershipViewSet, base_name = "membership")
# router.register(r'book', BookViewSet, base_name = "book")
# router.register(r'paper', PaperViewSet, base_name = "paper")
# router.register(r'miscellaneous', MiscellaneousViewSet, base_name= "miscellaneous")
# app_name = 'faculty_profile'

urlpatterns = [
    url(r'^', include(router.urls)),
]

