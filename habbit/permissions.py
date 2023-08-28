from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsPublicOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.public == True:
            return True
        elif obj.public == False and obj.user != request.user:
            return False
        else:
            return False
