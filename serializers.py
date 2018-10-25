import swapper

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
}

def return_serializer(class_name):
    """
    Return the serializer for the given class
    :param class_name: the class whose serializer is being generated
    """

    class Serializer(serializers.ModelSerializer):
        """
        Serializer for given class name
        """

        faculty_member = serializers.ReadOnlyField(
            source='faculty_member.person.full_name'
        )

        class Meta:
            """
            Meta class for Serializer
            """

            model = swapper.load_model('faculty_biodata', class_name)
            fields = '__all__'

    return Serializer

for key in serializer_dict:
    serializer_dict[key] = return_serializer(key)
