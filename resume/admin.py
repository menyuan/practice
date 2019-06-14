from django.contrib import admin
from resume.models import *
from resume.models import Contact

# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('__str__','name','phone','post','email') #list

admin.site.register([Contact])

