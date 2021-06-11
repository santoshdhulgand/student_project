from django.contrib import admin
from studentapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'marks' , 'roll_num']

admin.site.register(Student , StudentAdmin)

