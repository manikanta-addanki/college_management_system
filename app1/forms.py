from django import forms
from app1.models import Principal, Department

class PrincipalForm(forms.ModelForm):
    class Meta:
        model = Principal
        fields = ['name', 'email', 'phone']
       



from .models import Department, Principal

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code']
        



from .models import HOD, Department

class HODForm(forms.ModelForm):
    class Meta:
        model = HOD
        fields = ['name', 'email', 'phone', 'department']
        


from .models import Staff, Department

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'phone', 'department']
        

from .models import Student, Department, Staff

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'department', 'year', 'class_advisor']
        





