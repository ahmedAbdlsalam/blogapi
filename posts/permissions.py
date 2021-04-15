from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            # print("Read-only permissions are allowed for any request")
            return True
        # Write permissions are only allowed to the author of a post
        # print("Read-and-Write permissions are allowed for any request")
        return obj.author == request.user
