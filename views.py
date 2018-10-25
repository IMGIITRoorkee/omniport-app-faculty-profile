import swapper
from rest_framework.viewsets import ModelViewSet 

from faculty_profile.serializers import HonorSerializer 
from kernel.managers.get_role import get_role

from faculty_profile.permissions.is_faculty_member import IsFacultyMember
Honor = swapper.load_model('faculty_biodata', 'Honor')

class HonorViewSet(ModelViewSet):
    """
    API endpoint that allows Honor to be viewed or edited.
    """
    serializer_class = HonorSerializer
    permission_classes = (IsFacultyMember, )
    filter_backends = tuple()
    def perform_create(self, serializer):
        """
        modifying perform_create for all the views to get FacultyMember
        instance from request
        """
        faculty_member = get_role(self.request.person,'FacultyMember')
        serializer.save(faculty_member=faculty_member) 

    def get_queryset(self):
        faculty_member = get_role(self.request.person,'FacultyMember')
        return Honor.objects.filter(faculty_member=faculty_member)


# from kernel.managers.get_role import get_role
# from faculty_profile.serializers.serializers import *
# from faculty_profile.permissions.is_faculty_member import IsFacultyMember


# EducationalDetails = swapper.load_model('biodata_faculty', 'EducationalDetails')
# Honor = swapper.load_model('biodata_faculty', 'Honor')
# Visit = swapper.load_model('biodata_faculty', 'Visit')
# Collaboration = swapper.load_model('biodata_faculty', 'Collaboration')
# ResearchProject = swapper.load_model('biodata_faculty', 'ResearchProject')
# ScholarMap = swapper.load_model('biodata_faculty', 'ScholarMap')
# Supervision = swapper.load_model('biodata_faculty', 'Supervision')
# TeachingEngagement = swapper.load_model('biodata_faculty', 'TeachingEngagement')
# Conference = swapper.load_model('biodata_faculty', 'Conference')
# GuestLecture = swapper.load_model('biodata_faculty', 'GuestLecture')
# Seminar = swapper.load_model('biodata_faculty', 'Seminar')
# ShortTermCourse = swapper.load_model('biodata_faculty', 'ShortTermCourse')
# SpecialLecture = swapper.load_model('biodata_faculty', 'SpecialLecture')
# Talk = swapper.load_model('biodata_faculty', 'Talk')
# Interest = swapper.load_model('biodata_faculty', 'Interest')
# Miscellaneous = swapper.load_model('biodata_faculty', 'Miscellaneous')
# AdministrativePosition = swapper.load_model(
#     'biodata_faculty',
#     'AdministrativePosition'
# )
# Membership = swapper.load_model('biodata_faculty', 'Membership')
# Book = swapper.load_model('biodata_faculty', 'Book')
# Paper = swapper.load_model('biodata_faculty', 'Paper')


# class BaseViewSet(viewsets.ModelViewSet):
#         """
#         Common viewset for all the viewsets
#         """

#         permission_classes = (IsFacultyMember, )
#         filter_backends = tuple()

#         def get_faculty(self):
#             faculty = get_role(self.request.person, 'FacultyMember')
#             return faculty

        # def perform_create(self, serializer):
        #     """
        #     modifying perform_create for all the views to get FacultyMember
        #     instance from request
        #     """

        #     serializer.save(faculty=self.get_faculty())


# class AdministrativePositionViewSet(BaseViewSet):
#     """
#     API endpoint that allows AdministrativePostion to be edited or viewed
#     """

#     serializer_class = AdministrativePositionSerializer

#     def get_queryset(self):
#         return AdministrativePosition.objects.all().filter(faculty=self.get_faculty())


# class ScholarMapViewSet(BaseViewSet):
#     """
#     API endpoint that allows ScholarMap to be edited or viewed
#     """
    
#     serializer_class = ScholarMapSerializer

#     def get_queryset(self):
#         return ScholarMap.objects.all().filter(faculty=self.get_faculty())


# class GuestLectureViewSet(BaseViewSet):
#     """
#     API endpoint that allows GuestLecture to be viewed or edited
#     """
#     serializer_class = GuestLectureSerializer
    
#     def get_queryset(self):
#         return GuestLecture.objects.all().filter(faculty=self.get_faculty())


# class HonorViewSet(BaseViewSet):
#     """
#     API endpoint that allows Honor to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Honor.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = HonorSerializer


# class SeminarViewSet(BaseViewSet):
#     """
#     API endpoint that allows ParticipationSeminar to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Seminar.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = SeminarSerializer


# class MembershipViewSet(BaseViewSet):
#     """
#     API endpoint that allows Membership to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Membership.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = MembershipSerializer


# class MiscellaneousViewSet(BaseViewSet):
#     """
#     API endpoint that allows Miscellaneous to be viewed or edited.
#     """
    
    
#     def get_queryset(self):
#         return Miscellaneous.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = MiscellaneousSerializer


# class EducationalDetailsViewSet(BaseViewSet):
#     """
#     API endpoint that allows EducationalDetail to be viewed or edited.
#     """
    
    
#     def get_queryset(self):
#         return EducationalDetails.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = EducationalDetailsSerializer


# class CollaborationViewSet(BaseViewSet):
#     """
#     API endpoint that allows Collaboration to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Collaboration.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = CollaborationSerializer


# class BookViewSet(BaseViewSet):
#     """
#     API endpoint that allows BooksAuthored to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Book.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = BookSerializer


# class PaperViewSet(BaseViewSet):
#     """
#     API endpoint that allows RefereedJournalPapers to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Paper.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = PaperSerializer


# class TeachingEngagementViewSet(BaseViewSet):
#     """
#     API endpoint that allows TeachingEngagement to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return TeachingEngagement.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = TeachingEngagementSerializer

  
# class ResearchProjectViewSet(BaseViewSet):
#     """
#     API endpoint that allows ResearchProject to be viewed or edited.
#     """
#     def get_queryset(self):
#         return ResearchProject.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = ResearchProjectSerializer


# class SupervisionViewSet(BaseViewSet):
#     """
#     API endpoint that allows Supervision to be viewed or edited.
#     """

#     def get_queryset(self):
#         return Supervision.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = SupervisionSerializer


# class InterestViewSet(BaseViewSet):
#     """
#     API endpoint that allows Interest to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Interest.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = InterestSerializer


# class  VisitViewSet(BaseViewSet):
#     """
#     API endpoint that allows  Visit to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Visit.objects.all().filter(faculty=self.get_faculty())

#     serializer_class =  VisitSerializer


# class  ShortTermCourseViewSet(BaseViewSet):
#     """
#     API endpoint that allows ParticipationInShortTermCourses to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return ShortTermCourse.objects.all().filter(faculty=self.get_faculty())
        
#     serializer_class = ShortTermCourseSerializer


# class ConferenceViewSet(BaseViewSet):
#     """
#     API endpoint that allows Conference to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return Conference.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = ConferenceSerializer


# class SpecialLectureViewSet(BaseViewSet):
#     """
#     API endpoint that allows SpecialLecture to be viewed or edited.
#     """
    
#     def get_queryset(self):
#         return SpecialLecture.objects.all().filter(faculty=self.get_faculty())

#     serializer_class = SpecialLectureSerializer
