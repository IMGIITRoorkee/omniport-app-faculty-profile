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
            app_token = data_leak.get('facappToken')
            valid_ips = data_leak.get('ipAddresses')

            if app_token is None or valid_ips is None:
                return False

            # request's ip address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                request_ip = x_forwarded_for
            else:
                request_ip = request.META.get('REMOTE_ADDR')

            # request's authorization tokens
            request_token = request.headers.get('Authorization')

            if request_token == app_token and request_ip in valid_ips:
                return True

        return False
