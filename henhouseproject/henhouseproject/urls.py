"""
URL configuration for henhouseproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from pets.views import LogoutPage, SignupView
from django.conf.urls.static import static
from .views import loginPage
from django.contrib.auth.views import (PasswordResetView, 
                                       PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name='main'),
    path('signup/', SignupView.as_view(), name = 'signup'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', loginPage, name = 'login'),
    path('logout/',LogoutPage,name='logout'),
    path('pets/', include('pets.urls'), name='pets'),
    path('fosters/', include('fosters.urls', namespace='fosters'))

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)