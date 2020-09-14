from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    

# class IsProjectOwnerOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             if request.user == project.owner:
#                 return obj.owner == request.user