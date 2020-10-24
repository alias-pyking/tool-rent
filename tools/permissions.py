from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object lever permission to only author of object to edit it or delete it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
