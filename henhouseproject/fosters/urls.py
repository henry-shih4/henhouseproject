from django.urls import path
from .views import FosterListView, FosterCreateView, FosterDetailView, FosterUpdateView, FosterDeleteView

app_name = 'fosters'

urlpatterns = [

path('', FosterListView.as_view(), name ='foster-list'),
path('create/', FosterCreateView.as_view(), name ='foster-create'),
path('<int:pk>',FosterDetailView.as_view(),name='foster-detail'),
path('update-foster/<int:pk>',FosterUpdateView.as_view(),name='foster-update'),
path('delete-foster/<int:pk>',FosterDeleteView.as_view(),name='foster-delete'),
]