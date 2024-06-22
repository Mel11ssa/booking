from rest_framework.permissions import BasePermission

class IsChauffeurOrTransporteur(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user and (hasattr(user, 'chauffeur') or hasattr(user, 'transporteur')))