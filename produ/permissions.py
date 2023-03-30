from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
      perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
      # def has_object_permission(self, request, view, obj):
      #       if not request.user.username == "user":
      #         return False
      #       if not request.user.is_staff:
      #         return False   
      #       return super().has_object_permission(request, view, obj)
    
    # def has_object_permission(self, request, view, obj):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_object_permission(request, view, obj)
    # def has_permission(self, request, view):
    #     user =  request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has.perm("produ.add_produ"):
    #             return True
    #         if user.has.perm("produ.delete_produ"):
    #             return True
    #         if user.has.perm("produ.change_produ"):
    #             return True
    #         if user.has.perm("produ.view_produ"):
    #             return True
    #         return False
    #     return False
    
    
    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj) 