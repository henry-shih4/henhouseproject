from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Pet, User, UserProfile
from .forms import PetForm, ProfileModelForm, PetApplicationForm
from django.contrib.auth import authenticate,login, logout
from .forms import myUserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models  import Q
from django.http import HttpResponse
from django.views import generic
from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = myUserCreationForm

    def get_success_url(self):
        return reverse('login')

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


def check_user_able_to_see_page(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_foster:
            return function(request, *args, **kwargs)
        return HttpResponse('You are not allowed this action.')

    return wrapper


@login_required(login_url='/login')
@check_user_able_to_see_page
def PetCreate(request):
    page = 'create'
    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.foster = request.user
            pet.save()
            send_mail(subject="A pet has been created", message="Go to the web site to see the new pet.", from_email="test@test.com", recipient_list=["test2@test.com"])
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


@login_required(login_url='/login')
def PetApplication(request,pk):
    user = request.user
    profile = UserProfile.objects.get(id=user.id)
    pet = Pet.objects.get(id=pk)
    form = PetApplicationForm()
    applicants = pet.applicants.all()
    if request.user in applicants:
        return HttpResponse('You have already applied for this pet')
    if request.method == 'POST':
        form = PetApplicationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            pet.applicants.add(user)
            pet.save()
            return redirect('pet-detail', pk=pet.id)
        else:
            form = PetApplicationForm()
    context = {'pet':pet, 'user':user, 'profile':profile, 'form':form}
    return render(request,'pet-application.html',context)



@login_required(login_url='/login')
def ProfileView(request):
    user = request.user
    profile = UserProfile.objects.get(id=user.id)
    context = {'user':user, 'profile':profile}
    return render(request,'user-profile.html',context)


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "update-profile.html"
    form_class = ProfileModelForm

    def get_success_url(self):
        return reverse("user-profile")
    
    def get_queryset(self):
        return UserProfile.objects.all()