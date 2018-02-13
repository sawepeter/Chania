from django.contrib import admin
from gallery.models import Profile


# Register your models here.
class UserProfile (admin.ModelAdmin):
    list_display=['user','name','description','dob','country']

def description(self,object):
    return option.description

description.short_description=('info')
def get_queryset(self,request):

    queryset=super(UserProfile,self).get_queryset(request)
    return queryset
admin.site.register(Profile, UserProfile)