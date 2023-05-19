from django.contrib import admin
from .models import Pet, User, Foster, UserProfile, PetApplication
# Register your models here.


admin.site.register(Pet)
admin.site.register(User)
admin.site.register(Foster)
admin.site.register(UserProfile)
admin.site.register(PetApplication)