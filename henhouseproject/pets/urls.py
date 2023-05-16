from django.urls import path
from . import views


urlpatterns = [
    path('',views.PetList,name='pet-list'),
    
    path('create/',views.PetCreate,name='pet-create'),
    path('<int:pk>',views.PetDetail,name='pet-detail'),
    path('update-pet/<int:pk>',views.PetUpdate,name='pet-update'),
    path('delete-pet/<int:pk>',views.PetDelete,name='pet-delete'),

    path('interested/<int:pk>',views.PetInterested, name='pet-interested'),
]