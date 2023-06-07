import random
from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from pets.models import Foster, User
from .forms import FosterModelForm
from django.core.mail import send_mail
from .mixins import FosterAndLoginRequiredMixin, SuperUserRequiredMixin

# Create your views here.


class FosterListView(LoginRequiredMixin, generic.ListView):
    template_name = "fosters/foster_list.html"

    def get_queryset(self):
        return Foster.objects.all()
    


class FosterCreateView(SuperUserRequiredMixin, generic.CreateView):
    template_name = "fosters/foster_create.html"
    form_class = FosterModelForm

    def get_success_url(self):
        return reverse("fosters:foster-list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_foster = True
        user.username = f'{user.first_name}{user.last_name}'
        random_password = random.randint(0,100000)
        user.set_password(f"{random_password}")
        user.save()
        Foster.objects.create(
            user=user,
            user_profile=user.userprofile,
        )
        send_mail(
            subject="You are invited to be an approved Foster for Hen's House",
            message=f"Congratulations. You are approved as a Foster for Hen's House. Please come login to get started. Your temporary password is {random_password}. You can reset your password if you want to on the login page by clicking reset password."
            ,
            from_email="admin@henshouse.com", 
            recipient_list=[user.email]
        )
        # foster.user_profile = self.request.user.userprofile
        # foster.save()
        return super(FosterCreateView, self).form_valid(form)
    

class FosterDetailView(LoginRequiredMixin, generic.DetailView):
    template_name= "fosters/foster_detail.html"
    context_object_name = "foster"

    def get_queryset(self):
        return Foster.objects.all()



class FosterUpdateView(FosterAndLoginRequiredMixin, generic.UpdateView):
    template_name = "fosters/foster_update.html"
    form_class = FosterModelForm

    def get_success_url(self):
        return reverse("fosters:foster-list")
    
    def get_queryset(self):
        return Foster.objects.all()
    

# class FosterDeleteView(SuperUserRequiredMixin, generic.DeleteView):
#     template_name= "fosters/foster_delete.html"
#     context_object_name = "user"

#     def get_queryset(self):
#         return User.objects.all()
    
#     def get_success_url(self):
#         return reverse("fosters:foster-list")
    


def FosterDelete(request,pk):
    foster = Foster.objects.get(id=pk)
    user = foster.user
     
    if request.method == 'POST':
        user.delete()
        return redirect('fosters:foster-list')
    return render(request, 'fosters/foster_delete.html', {'obj':user})
