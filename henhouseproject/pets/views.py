from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Pet
from .forms import PetForm
from .models import User
from django.contrib.auth import authenticate,login, logout
from .forms import myUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models  import Q
from django.http import HttpResponse
from django.views import generic

# Create your views here.

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = myUserCreationForm

    def get_success_url(self):
        return reverse('login')

# def RegisterPage(request):
#     page='register'
#     form = myUserCreationForm()

#     if request.method == 'POST':
#         form = myUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request,user)
#             return redirect('pet-list')
#         else:
#             messages.error(request, 'An error occurred during registration')
#     context = {'form':form, 'page':page}
#     return render(request, 'login_register.html', context)

def RegisterPage(request):
    pass

# def LoginPage(request):
#     page = 'login'
#     if (request.user.is_authenticated):
#         return redirect('main')
    
#     if request.method == 'POST':
#         username =request.POST.get('username').lower()
#         password =request.POST.get('password')

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'User does not exist')

#         user = authenticate(request, username=username, password=password)       

#         if user is not None:
#             login(request,user)
#             return redirect('main')
#         else:
#             messages.error(request, 'Username or password incorrect')
    
#     context = {'form':form,'page':page}
#     return render(request, 'login_register.html', context)

def LoginPage(request):
    pass


def LogoutPage(request):
    logout(request)
    return redirect('main')


@login_required(login_url='/login')
def PetList(request):
    q = request.GET.get('q')
    if q:
        print(q)
        pets = Pet.objects.filter(interested__in =[q])
    else:
        pets = Pet.objects.all()
    context = {'pets':pets}
    return render(request, 'pet-list.html', context )


def PetDetail(request,pk):
    pet = Pet.objects.get(id=pk)
    interested = pet.interested.all()
    count = interested.count()
    context = {'pet':pet, 'interested':interested, 'count':count}
    return render(request,'pet-detail.html', context)


@login_required(login_url='/login')
def PetCreate(request):
    page = 'create'
    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.foster = request.user
            pet.save()
            return redirect('pet-list')
        
    context={'form':form, 'page':page}
    return render(request, 'pet-form.html', context)


@login_required(login_url='/login')
def PetUpdate(request,pk):
    page = 'update'
    pet = Pet.objects.get(id=pk)
    form = PetForm(instance=pet)

    if request.user != pet.foster:
        return HttpResponse('You are not allowed this action.')
    
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid:
            form.save()
            return redirect('pet-detail', pk=pet.id)
    context = {'form':form, 'page':page, 'pet':pet}
    return render(request, 'pet-form.html', context)    


@login_required(login_url='/login')
def PetDelete(request,pk):
    pet = Pet.objects.get(id=pk)

    if request.user != pet.foster:
        return HttpResponse('You are not allowed this action.')   
     
    if request.method == 'POST':
        pet.delete()
        return redirect('pet-list')
    return render(request, 'delete.html', {'obj':pet})



def PetInterested(request,pk):
    pet = Pet.objects.get(id=pk)
    interested = pet.interested.all()
    if request.method == 'POST':
        if request.user in interested:
            pet.interested.remove(request.user)
        else:
            pet.interested.add(request.user)
    return redirect('pet-detail', pk=pet.id)