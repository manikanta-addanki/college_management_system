from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/<int:id>/update/', views.department_update, name='department_update'),
    path('departments/<int:id>/delete/', views.department_delete, name='department_delete'),
    
    path('principals/', views.principal_list, name='principal_list'),
    path('principals/create/', views.principal_create, name='principal_create'),
    path('principals/<int:id>/update/', views.principal_update, name='principal_update'),
    path('principals/<int:id>/delete/', views.principal_delete, name='principal_delete'),
    
    path('hods/', views.hod_list, name='hod_list'),
    path('hods/create/', views.hod_create, name='hod_create'),
    path('hods/<int:id>/update/', views.hod_update, name='hod_update'),
    path('hods/<int:id>/delete/', views.hod_delete, name='hod_delete'),
    
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/<int:id>/update/', views.staff_update, name='staff_update'),
    path('staff/<int:id>/delete/', views.staff_delete, name='staff_delete'),
    
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:id>/update/', views.student_update, name='student_update'),
    path('students/<int:id>/delete/', views.student_delete, name='student_delete'),
]
