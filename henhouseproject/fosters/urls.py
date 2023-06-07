from django.urls import path
from .views import FosterListView, FosterCreateView, FosterDetailView, FosterUpdateView, FosterDelete
app_name = 'fosters'

urlpatterns = [

path('', FosterListView.as_view(), name ='foster-list'),
path('create/', FosterCreateView.as_view(), name ='foster-create'),
path('<int:pk>',FosterDetailView.as_view(),name='foster-detail'),
path('<int:pk>/update/',FosterUpdateView.as_view(),name='foster-update'),
path('<int:pk>/delete/',FosterDelete,name='foster-delete'),
]