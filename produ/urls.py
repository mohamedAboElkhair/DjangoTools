from django.urls import path
from . import views
#/api/produ/
urlpatterns = [
 path('',views.produ_List_create_view),
 path('<int:pk>/', views.produ_detail_view) , 
 path('<int:pk>/update/', views.produ_update_view),
 path('<int:pk>/delete/', views.produ_destroy_view)  
]
 