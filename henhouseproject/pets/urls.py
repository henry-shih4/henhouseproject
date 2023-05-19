from django.urls import path
from . import views
from .views import ProfileUpdateView

urlpatterns = [
    path('',views.PetList,name='pet-list'),
    
    path('create/',views.PetCreate,name='pet-create'),
    path('<int:pk>',views.PetDetail,name='pet-detail'),
    path('update-pet/<int:pk>',views.PetUpdate,name='pet-update'),
    path('delete-pet/<int:pk>',views.PetDelete,name='pet-delete'),
    path('interested/<int:pk>',views.PetInterested, name='pet-interested'),
    path('application/<int:pk>',views.PetApplication, name='pet-application'),
    path('profile/',views.ProfileView, name='user-profile'),
    path('update-profile/<int:pk>',ProfileUpdateView.as_view(),name='update-profile'),
]