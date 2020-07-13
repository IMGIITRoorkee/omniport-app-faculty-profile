import swapper

from faculty_biodata.constants.semesters import SEMESTER_TYPES

from rest_framework import serializers

serializer_dict = {
    'Profile': None,
    'Education': None,
    'Honour': None,
    'Visit': None,
    'Collaboration': None,
    'Project': None,
    'AssociateScholar': None,
    'Supervision': None,
    'TeachingEngagement': None,
    'Event': None,
    'Interest': None,
    'AdministrativePosition': None,
    'Membership': None,
    'Book': None,
    'Paper': None,
    'Miscellaneous': None,
}


def return_serializer(class_name):
    """
    Return the serializer for the given class
    :param class_name: the class whose serializer is being generated
    """

    Model = swapper.load_model('faculty_biodata', class_name)

    class Serializer(serializers.ModelSerializer):
        """
        Serializer for given class name
        """

        faculty_member = serializers.ReadOnlyField(
            source='faculty_member.person.full_name'
        )

        if hasattr(Model, 'has_already_ended'):
            is_completed = serializers.SerializerMethodField()
            status_type = serializers.SerializerMethodField()

        if hasattr(Model, 'semester'):
            semester_name = serializers.SerializerMethodField()

        class Meta:
            """
            Meta class for Serializer
            """

            model = Model
            fields = '__all__'

        def get_is_completed(self, instance):
            """
            Returns if the duration of an instance has ended
            :return: if the duration of an instance has ended
            """

            return instance.has_already_ended

        def get_status_type(self, instance):
            """
            Returns status type for instance 
            :return: if the duration of an instance has ended
            """

            return "A" if instance.has_already_ended else "O"

        def get_semester_name(self, instance):
            """
            Returns semester name from semester annotations. i.e Spring for s.
            :return: semester name from semester annotations
            """

            for sem in SEMESTER_TYPES:
                if sem[0] == instance.semester:
                    return sem[1]
            
            return ""

    return Serializer


for key in serializer_dict:
    serializer_dict[key] = return_serializer(key)
