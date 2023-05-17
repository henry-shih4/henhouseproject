from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from pets.models import Foster
from .forms import FosterModelForm

# Create your views here.


class FosterListView(LoginRequiredMixin, generic.ListView):
    template_name = "fosters/foster_list.html"

    def get_queryset(self):
        return Foster.objects.all()
    


class FosterCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "fosters/foster_create.html"
    form_class = FosterModelForm

    def get_success_url(self):
        return reverse("fosters:foster-list")
    
    def form_valid(self, form):
        foster = form.save(commit=False)
        foster.user_profile = self.request.user.userprofile
        foster.save()
        return super(FosterCreateView, self).form_valid(form)
    

class FosterDetailView(LoginRequiredMixin, generic.DetailView):
    template_name= "fosters/foster_detail.html"
    context_object_name = "foster"

    def get_queryset(self):
        return Foster.objects.all()



class FosterUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "fosters/foster_update.html"
    form_class = FosterModelForm

    def get_success_url(self):
        return reverse("fosters:foster-list")
    
    def get_queryset(self):
        return Foster.objects.all()
    

class FosterDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name= "fosters/foster_delete.html"
    context_object_name = "foster"

    def get_queryset(self):
        return Foster.objects.all()
    
    def get_success_url(self):
        return reverse("fosters:foster-list")