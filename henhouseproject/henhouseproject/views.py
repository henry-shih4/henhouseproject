from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from pets.models import User
from django.contrib import messages

def Home(request):
    return render(request,'main.html')


# class MyLoginView(LoginView):
#     redirect_authenticated_user = True



def loginPage(request):
    page = 'login'
    if (request.user.is_authenticated):
        return redirect('pet-list')

    if request.method == 'POST':
        email =request.POST.get('email').lower()
        password =request.POST.get('password')
        try:
            username = User.objects.get(email=email).username
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('pet-list')    
        else:
            messages.error(request, 'Username or password incorrect')

    context={'page':page}
    return render(request, 'registration/login.html',context)


