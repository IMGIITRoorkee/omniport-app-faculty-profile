import swapper

from rest_framework import serializers 
Honor = swapper.load_model('faculty_biodata', 'Honor')

# common_fields = (
#     'priority',
#     'visibility',
# )

class HonorSerializer(serializers.ModelSerializer):
    """
    Serializer for Honor
    """

    faculty_member = serializers.ReadOnlyField(source='faculty_member.person.full_name')

    class Meta:
        """
        Meta class for HonorSerializer
        """

        model = Honor
        fields = '__all__'

# # EducationalDetails = swapper.load_model('biodata_faculty', 'EducationalDetails')
# # Honor = swapper.load_model('biodata_faculty', 'Honor')
# # Visit = swapper.load_model('biodata_faculty', 'Visit')
# # Collaboration = swapper.load_model('biodata_faculty', 'Collaboration')
# # ResearchProject = swapper.load_model('biodata_faculty', 'ResearchProject')
# # ScholarMap = swapper.load_model('biodata_faculty', 'ScholarMap')
# # Supervision = swapper.load_model('biodata_faculty', 'Supervision')
# # TeachingEngagement = swapper.load_model('biodata_faculty', 'TeachingEngagement')
# # Conference = swapper.load_model('biodata_faculty', 'Conference')
# # GuestLecture = swapper.load_model('biodata_faculty', 'GuestLecture')
# # Seminar = swapper.load_model('biodata_faculty', 'Seminar')
# # ShortTermCourse = swapper.load_model('biodata_faculty', 'ShortTermCourse')
# # SpecialLecture = swapper.load_model('biodata_faculty', 'SpecialLecture')
# # Talk = swapper.load_model('biodata_faculty', 'Talk')
# # Interest = swapper.load_model('biodata_faculty', 'Interest')
# # Miscellaneous = swapper.load_model('biodata_faculty', 'Miscellaneous')
# # AdministrativePosition = swapper.load_model(
# #     'biodata_faculty',
# #     'AdministrativePosition'
# # )
# # Membership = swapper.load_model('biodata_faculty', 'Membership')
# # Book = swapper.load_model('biodata_faculty', 'Book')
# # Paper = swapper.load_model('biodata_faculty', 'Paper')
# # Student = swapper.load_model('kernel', 'Student')
# # Person = swapper.load_model('kernel', 'Person')




# # common_lecture_fields = (
# #         'name',
# #         'place',
# #         'sponsor',
# # common_fields = (
# #     'priority',
# #     'visibility',
# # )
# #         'role',
# #         'start_date',
# #         'end_date',
# # ) + common_fields


# # class PersonSerializer(serializers.ModelSerializer):
# #     """

# #     """

# #     class Meta:
        
# #         model = Person
# #         fields = (
# #             'full_name',
# #         )


# # class StudentSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Student model
# #     """ 
    
# #     class Meta:
# #         """
# #         Meta class for StudentSerializers
# #         """
        
# #         model = Student.filter(faculty=get_role(self.request.person,'FacultyMember'))
# #         fields = (.filter(faculty=get_role(self.request.person,'FacultyMember'))
# #             'enrolment_num.filter(faculty=get_role(self.request.person,'FacultyMember'))ber',
# #             'branch',.filter(faculty=get_role(self.request.person,'FacultyMember'))
# #             'current_year'.filter(faculty=get_role(self.request.person,'FacultyMember')),
# #             'current_semes.filter(faculty=get_role(self.request.person,'FacultyMember'))ter',
# #             'current_cgpa',
# #         )

   

# # class E# class HonorSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Honor
# #     """

# #     class Meta:
# #         """
# #         Meta class for HonorSerializer
# #         """


# #         model = Honor
# #         fields = (
# #             'award',
# #             'year',
# #             'organisation',
# #         ) + common_fieldsrializer(serializers.ModelSerializer):
# #     """# class HonorSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Honor
# #     """

# #     class Meta:
# #         """
# #         Meta class for HonorSerializer
# #         """


# #         model = Honor
# #         fields = (
# #             'award',
# #             'year',
# #             'organisation',
# #         ) + common_fields
# #     Serializer for EducationalDetails
# #     """

# #     class Meta:
# #         """
# #         Meta class for EducationalDetailsSerializer
# #         """

# #         model = EducationalDetails
# #         fields = (
# #             'subject',
# #             'degree',
# #             'university',
# #             'year',
# #             'priority',
# #             'visibility',
# #         ) + common_fields


# # class HonorSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Honor
# #     """

# #     class Meta:
# #         """
# #         Meta class for HonorSerializer
# #         """


# #         model = Honor
# #         fields = (
# #             'award',
# #             'year',
# #             'organisation',
# #         ) + common_fields


# # class VisitSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Visit
# #     """

# #     class Meta:
# #         """
# #         Meta class for VisitSerializer
# #         """

# #         model = Visit
# #         fields = (
# #             'place',
# #             'purpose',
# #             'date',
# #         ) + common_fields


# # class CollaborationSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Collaboration
# #     """

# #     class Meta:
# #         """
# #         Meta class for Collaboration
# #         """


# #         model = Collaboration
# #         fields = (
# #             'organisation',
# #             'topic',
# #         ) + common_fields


# # class ResearchProjectSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for ResearchProject
# #     """

# #     class Meta:
# #         """
# #         Meta class for ResearchProjectSerializer
# #         """

# #         model = ResearchProject
# #         fields = (
# #             'topic',
# #             'financial_outlay',
# #             'funding_agency',
# #             'start_date',
# #             'end_date',
# #             'other_investigating_officer', 
# #             'project_type',
# #         ) + common_fields


# # class ScholarMapSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for ScholarMap
# #     """
    
# #     class Meta:
# #         """
# #         Meta class for ScholarMapSerializer
# #         """

# #         model = ScholarMap
# #         fields = (
# #             'scholar',
# #         ) + common_fields


# # class SupervisionSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Supervision
# #     """

# #     class Meta:
# #         """
# #         Meta class for SupervisionSerializer
# #         """

# #         model = Supervision
# #         fields = (
# #             'topic',
# #             'scholars_name',
# #             'category',
# #             'start_date',
# #             'end_date',
# #             'name_of_other_supervisors',
# #         ) + common_fields


# # class TeachingEngagementSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for TeachingEngagement
# #     """

# #     class Meta:
# #         """
# #         Meta class for TeachingEngagementSerializer
# #         """


# #         model = TeachingEngagement
# #         fields = (
# #             'class_name',
# #             'course',
# #             'student_count',
# #             'lecture_hours',
# #             'practical_hours',
# #             'tutorial_hours',
# #         ) + common_fields


# # class ConferenceSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for TeachingEngagement
# #     """

# #     class Meta:
# #         """
# #         Meta class for TeachingEngagementSerializer
# #         """

# #         model = Conference
# #         fields = common_lecture_fields


# # class GuestLectureSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for GuestLecture
# #     """

# #     class Meta:
# #         """
# #         Meta class for GuestLectureSerializer
# #         """

# #         model = GuestLecture
# #         fields = common_lecture_fields


# # class SeminarSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Seminar
# #     """

# #     class Meta:
# #         """
# #         Meta class for SeminarSerializer
# #         """

# #         model = Seminar
# #         fields = common_lecture_fields


# # class ShortTermCourseSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for ShortTermCourse
# #     """

# #     class Meta:
# #         """
# #         Meta class for ShortTermCourseSerializer
# #         """

# #         model = ShortTermCourse
# #         fields = common_lecture_fields


# # class SpecialLectureSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for SpecialLecture
# #     """

# #     class Meta:
# #         """
# #         Meta class for SpecialLectureSerializer
# #         """


# #         model = SpecialLecture
# #         fields = common_lecture_fields


# # class MembershipSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Membership
# #     """

# #     class Meta:
# #         """
# #         Meta class for MembershipSerializer
# #         """

# #         model = Membership
# #         fields = (
# #             'organisation',
# #             'designation',
# #             'scope',
# #             'start_date',
# #             'end_date',
# #         ) + common_fields


# # class AdministrativePositionSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for AdministrativePosition
# #     """

# #     class Meta:
# #         """
# #         Meta class for AdministrativePositionSerializer
# #         """

# #         model = AdministrativePosition
# #         fields = (
# #             'organisation',
# #             'designation',
# #             'scope',
# #             'start_date',
# #             'end_date',
# #         ) + common_fields


# # class MiscellaneousSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Miscellaneous
# #     """

# #     class Meta:
# #         """
# #         Meta class for MiscellaneousSerializer
# #         """

# #         model = Miscellaneous
# #         fields = (
# #             'title',
# #             'description',
# #         ) + common_fields


# # class BookSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Book
# #     """

# #     class Meta:
# #         """
# #         Meta class for BookSerializer
# #         """

# #         model = Book
# #         fields = (
# #             'title',
# #             'content',
# #         ) + common_fields
        

# # class PaperSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Paper
# #     """

# #     class Meta:
# #         """
# #         Meta class for PaperSerializer
# #         """

# #         model = Paper
# #         fields = (import swapper

# from rest_framework import serializers

# Honor = swapper.load_model('biodata_faculty', 'Honor')

# common_fields = (
#     'priority',
#     'visibility',
# )

# class HonorSerializer(serializers.ModelSerializer):
#     """
#     Serializer for Honor
#     """


#     class Meta:
#         """
#         Meta class for HonorSerializer
#         """

#         model = Honor
#         fields = (
#             'award',
#             'year',
#             'organisation',
#         ) + common_fields

# # EducationalDetails = swapper.load_model('biodata_faculty', 'EducationalDetails')
# # Honor = swapper.load_model('biodata_faculty', 'Honor')
# # Visit = swapper.load_model('biodata_faculty', 'Visit')
# # Collaboration = swapper.load_model('biodata_faculty', 'Collaboration')
# # ResearchProject = swapper.load_model('biodata_faculty', 'ResearchProject')
# # ScholarMap = swapper.load_model('biodata_faculty', 'ScholarMap')
# # Supervision = swapper.load_model('biodata_faculty', 'Supervision')
# # TeachingEngagement = swapper.load_model('biodata_faculty', 'TeachingEngagement')
# # Conference = swapper.load_model('biodata_faculty', 'Conference')
# # GuestLecture = swapper.load_model('biodata_faculty', 'GuestLecture')
# # Seminar = swapper.load_model('biodata_faculty', 'Seminar')
# # ShortTermCourse = swapper.load_model('biodata_faculty', 'ShortTermCourse')
# # SpecialLecture = swapper.load_model('biodata_faculty', 'SpecialLecture')
# # Talk = swapper.load_model('biodata_faculty', 'Talk')
# # Interest = swapper.load_model('biodata_faculty', 'Interest')
# # Miscellaneous = swapper.load_model('biodata_faculty', 'Miscellaneous')
# # AdministrativePosition = swapper.load_model(
# #     'biodata_faculty',
# #     'AdministrativePosition'
# # )
# # Membership = swapper.load_model('biodata_faculty', 'Membership')
# # Book = swapper.load_model('biodata_faculty', 'Book')
# # Paper = swapper.load_model('biodata_faculty', 'Paper')
# # Student = swapper.load_model('kernel', 'Student')
# # Person = swapper.load_model('kernel', 'Person')




# # common_lecture_fields = (
# #         'name',
# #         'place',
# #         'sponsor',
# # common_fields = (
# #     'priority',
# #     'visibility',
# # )
# #         'role',
# #         'start_date',
# #         'end_date',
# # ) + common_fields


# # class PersonSerializer(serializers.ModelSerializer):
# #     """

# #     """

# #     class Meta:
        
# #         model = Person
# #         fields = (
# #             'full_name',
# #         )


# # class StudentSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Student model
# #     """ 
    
# #     class Meta:
# #         """
# #         Meta class for StudentSerializers
# #         """
        
# #         model = Student
# #         fields = (
# #             'enrolment_number',
# #             'branch',
# #             'current_year',
# #             'current_semester',
# #             'current_cgpa',
# #         )

   

# # class E# class HonorSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Honor
# #     """

# #     class Meta:
# #         """
# #         Meta class for HonorSerializer
# #         """


# #         model = Honor
# #         fields = (
# #             'award',
# #             'year',
# #             'organisation',
# #         ) + common_fieldsrializer(serializers.ModelSerializer):
# #     """# class HonorSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Honor
# #     """

# #     class Meta:
# #         """
# #         Meta class for HonorSerializer
# #         """


# #         model = Honor
# #         fields = (
# #             'award',
# #             'year',
# #             'organisation',
# #         ) + common_fields
# #     Serializer for EducationalDetails
# #     """

# #     class Meta:
# #         """
# #         Meta class for EducationalDetailsSerializer
# #         """

# #         model = EducationalDetails
# #         fields = (
# #             'subject',
# #             'degree',
# #             'university',
# #             'year',
# #             'priority',
# #             'visibility',
# #         ) + common_fields


# # class HonorSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Honor
# #     """

# #     class Meta:
# #         """
# #         Meta class for HonorSerializer
# #         """


# #         model = Honor
# #         fields = (
# #             'award',
# #             'year',
# #             'organisation',
# #         ) + common_fields


# # class VisitSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Visit
# #     """

# #     class Meta:
# #         """
# #         Meta class for VisitSerializer
# #         """

# #         model = Visit
# #         fields = (
# #             'place',
# #             'purpose',
# #             'date',
# #         ) + common_fields


# # class CollaborationSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Collaboration
# #     """

# #     class Meta:
# #         """
# #         Meta class for Collaboration
# #         """


# #         model = Collaboration
# #         fields = (
# #             'organisation',
# #             'topic',
# #         ) + common_fields


# # class ResearchProjectSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for ResearchProject
# #     """

# #     class Meta:
# #         """
# #         Meta class for ResearchProjectSerializer
# #         """

# #         model = ResearchProject
# #         fields = (
# #             'topic',
# #             'financial_outlay',
# #             'funding_agency',
# #             'start_date',
# #             'end_date',
# #             'other_investigating_officer', 
# #             'project_type',
# #         ) + common_fields


# # class ScholarMapSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for ScholarMap
# #     """
    
# #     class Meta:
# #         """
# #         Meta class for ScholarMapSerializer
# #         """

# #         model = ScholarMap
# #         fields = (
# #             'scholar',
# #         ) + common_fields


# # class SupervisionSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Supervision
# #     """

# #     class Meta:
# #         """
# #         Meta class for SupervisionSerializer
# #         """

# #         model = Supervision
# #         fields = (
# #             'topic',
# #             'scholars_name',
# #             'category',
# #             'start_date',
# #             'end_date',
# #             'name_of_other_supervisors',
# #         ) + common_fields


# # class TeachingEngagementSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for TeachingEngagement
# #     """

# #     class Meta:
# #         """
# #         Meta class for TeachingEngagementSerializer
# #         """


# #         model = TeachingEngagement
# #         fields = (
# #             'class_name',
# #             'course',
# #             'student_count',
# #             'lecture_hours',
# #             'practical_hours',
# #             'tutorial_hours',
# #         ) + common_fields


# # class ConferenceSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for TeachingEngagement
# #     """

# #     class Meta:
# #         """
# #         Meta class for TeachingEngagementSerializer
# #         """

# #         model = Conference
# #         fields = common_lecture_fields


# # class GuestLectureSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for GuestLecture
# #     """

# #     class Meta:
# #         """
# #         Meta class for GuestLectureSerializer
# #         """

# #         model = GuestLecture
# #         fields = common_lecture_fields


# # class SeminarSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Seminar
# #     """

# #     class Meta:
# #         """
# #         Meta class for SeminarSerializer
# #         """

# #         model = Seminar
# #         fields = common_lecture_fields


# # class ShortTermCourseSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for ShortTermCourse
# #     """

# #     class Meta:
# #         """
# #         Meta class for ShortTermCourseSerializer
# #         """

# #         model = ShortTermCourse
# #         fields = common_lecture_fields


# # class SpecialLectureSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for SpecialLecture
# #     """

# #     class Meta:
# #         """
# #         Meta class for SpecialLectureSerializer
# #         """


# #         model = SpecialLecture
# #         fields = common_lecture_fields


# # class MembershipSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Membership
# #     """

# #     class Meta:
# #         """
# #         Meta class for MembershipSerializer
# #         """

# #         model = Membership
# #         fields = (
# #             'organisation',
# #             'designation',
# #             'scope',
# #             'start_date',
# #             'end_date',
# #         ) + common_fields


# # class AdministrativePositionSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for AdministrativePosition
# #     """

# #     class Meta:
# #         """
# #         Meta class for AdministrativePositionSerializer
# #         """

# #         model = AdministrativePosition
# #         fields = (
# #             'organisation',
# #             'designation',
# #             'scope',
# #             'start_date',
# #             'end_date',
# #         ) + common_fields


# # class MiscellaneousSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Miscellaneous
# #     """

# #     class Meta:
# #         """
# #         Meta class for MiscellaneousSerializer
# #         """

# #         model = Miscellaneous
# #         fields = (
# #             'title',
# #             'description',
# #         ) + common_fields


# # class BookSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Book
# #     """

# #     class Meta:
# #         """
# #         Meta class for BookSerializer
# #         """

# #         model = Book
# #         fields = (
# #             'title',
# #             'content',
# #         ) + common_fields
        

# # class PaperSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Paper
# #     """

# #     class Meta:
# #         """
# #         Meta class for PaperSerializer
# #         """

# #         model = Paper
# #         fields = (
# #             'title',
# #             'content',
# #         ) + common_fields


# # class InterestSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Interest
# #     """

# #     class Meta:
# #         """
# #         Meta class for InterestSerializer
# #         """

# #         model = Interest
# #         fields = (
# #             'general_topic',
# #             'research_work_topic',
# #         ) + common_fields

# #             'title',
# #             'content',
# #         ) + common_fields


# # class InterestSerializer(serializers.ModelSerializer):
# #     """
# #     Serializer for Interest
# #     """

# #     class Meta:
# #         """
# #         Meta class for InterestSerializer
# #         """

# #         model = Interest
# #         fields = (
# #             'general_topic',
# #             'research_work_topic',
# #         ) + common_fields
