from rest_framework import permissions

class CustomHttpMethodAuthentication(permissions.BasePermission):        

    def has_permission(self, request, view):
        """ 
        Skipping http method from authentication which 
        are listed in the view
        params: http_allowed_method <type 'list'>
        """
        if request.method in view.http_allowed_method:
            return True

        # Otherwise, only allow authenticated requests
        return request.user and request.user.is_authenticated