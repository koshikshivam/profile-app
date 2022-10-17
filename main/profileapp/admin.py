from django.contrib import admin
from .models import *
from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from .resource import UserResource


admin.site.register(Profile)
# class profiles(admin.ModelAdmin):
#     list_display = ['name', 'gender','dob','age','address','user']


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
