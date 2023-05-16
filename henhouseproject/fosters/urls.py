from django.urls import path
from .views import FosterListView, FosterCreateView

app_name = 'fosters'

urlpatterns = [

path('', FosterListView.as_view(), name ='foster-list'),
path('create/', FosterCreateView.as_view(), name ='foster-create')

]