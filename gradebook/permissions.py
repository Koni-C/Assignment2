from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print("object author", obj.author)
        print("request user", request.user)
        return obj.author == request.user

class IsLecturerOrStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        if 'Lecturer' in user_groups:
            return True
        elif 'Student' in user_groups and view.action in ['retrieve', 'list']:
            return True
        return False