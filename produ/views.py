from django.shortcuts import render
from rest_framework import generics,permissions,authentication
from .models import Produ
from .serializers import ProduSerializer
from .permissions import IsStaffEditorPermission

from api.authentication import TokenAuthentication

class ProduListCreateAPIView(generics.ListCreateAPIView):
    queryset = Produ.objects.all()
    serializer_class = ProduSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    authentication_classes = [authentication.SessionAuthentication,
                              TokenAuthentication,
                            ]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission,]
    
    def perform_create(self, serializer):
        titel = serializer.validated_data.get('titel')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = titel
        serializer.save(content=content)    

produ_List_create_view= ProduListCreateAPIView.as_view()
class ProduDatailAPIView(generics.RetrieveAPIView):
    queryset = Produ.objects.all()
    serializer_class = ProduSerializer
    # lookup_fieid = pk??
produ_detail_view = ProduDatailAPIView.as_view()     

class ProduUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Produ.objects.all()
    serializer_class = ProduSerializer
    # lookup_fieid = 'pk'
    permission_classes = [permissions.DjangoModelPermissions]
produ_update_view = ProduUpdateAPIView.as_view() 


class ProduDestroyAPIView(generics.DestroyAPIView):
    queryset = Produ.objects.all()
    serializer_class = ProduSerializer
    lookup_fieid = 'pk'
    # authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
produ_destroy_view = ProduDestroyAPIView.as_view() 