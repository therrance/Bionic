from django.contrib import admin
from coursera.models import Student, Group
# Register your models here.



class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'group']

admin.site.register(Student, StudentAdmin)
admin.site.register(Group)