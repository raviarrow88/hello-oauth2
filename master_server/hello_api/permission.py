from rest_framework.permissions import BasePermission
from rest_framework import permissions
class IsOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        else:
            return False


