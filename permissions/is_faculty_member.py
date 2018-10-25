import swapper

from rest_framework import permissions

from kernel.managers.get_role import get_role


class IsFacultyMember(permissions.BasePermission):
    """
    Custom permission check for the user to be faculty member or not
    """

    def has_permission(self, request, view):
        """
        Permission to use Faculty App views
        """
        
        FacultyMember = swapper.load_model('kernel', 'FacultyMember')
        try:
            faculty = get_role(request.person, 'FacultyMember')
            return True
        except FacultyMember.DoesNotExist:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Permission to check whether the object handled by the faculty member 
        belongs to the faculty member
        """
        
        FacultyMember = swapper.load_model('kernel', 'FacultyMember')
        faculty_member = get_role(request.person, 'FacultyMember')
        if obj.faculty_member == faculty_member:
            return True
        else:
            return False




