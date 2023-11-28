from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from user.models import User, Profile



class IsOnlyAdministrator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user = request.user) 
        return profile.role == "Администратор"
    
class IsOnlyAnimator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(user = request.user) 
        return profile.role == "Аниматор"