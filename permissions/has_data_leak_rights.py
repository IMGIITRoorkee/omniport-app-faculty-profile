from rest_framework import permissions

from omniport.settings.configuration.base import CONFIGURATION


class CanDataLeak(permissions.BasePermission):
    """
    Custom permission to check if user can get faculty data
    """

    def has_permission(self, request, view):
        """
        Permission to get faculty data
        """

        # Check if dataLeak is configured or not
        data_leak = CONFIGURATION.integrations.get('dataLeak')

        if data_leak is not None:
            data_leak_map = {data['facappToken']: data for data in data_leak}

            # request's ip address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                request_ip = x_forwarded_for
            else:
                request_ip = request.META.get('REMOTE_ADDR')

            # request's authorization tokens
            request_token = request.headers.get('Authorization')

            leak = data_leak_map.get(request_token)
            if leak and request_ip in leak['ipAddresses']:

                department = request.GET.get('department')

                # Check is user's access is limited to certain departments only
                allowed_departments = leak.get('departments')
                if allowed_departments:
                    return department in allowed_departments

                return True

        return False

