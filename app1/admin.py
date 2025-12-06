from django.contrib import admin

from django.contrib import admin
from app1.models import Principal, Department, HOD, Staff, Student


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']
    ordering = ['name']

admin.site.register(Department,DepartmentAdmin)


class PrincipalAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email']
    ordering = ['name']

admin.site.register(Principal,PrincipalAdmin)


class HODAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'department']
    list_filter = ['department']
    search_fields = ['name', 'email']
    list_select_related = ['department']
    ordering = ['name']

admin.site.register(HOD,HODAdmin)



class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'department']
    list_filter = ['department']
    search_fields = ['name', 'email']
    list_select_related = ['department']
    ordering = ['name']

admin.site.register(Staff,StaffAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'department', 'year', 'class_advisor']
    list_filter = ['department', 'year', 'class_advisor']
    search_fields = ['name', 'email']
    list_select_related = ['department', 'class_advisor']
    ordering = ['name']
admin.site.register(Student,StudentAdmin)


