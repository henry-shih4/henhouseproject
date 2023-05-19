from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


def Home(request):
    return render(request,'main.html')


class MyLoginView(LoginView):
    redirect_authenticated_user = True


    