from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Department, Principal, HOD, Staff, Student
from .forms import DepartmentForm, PrincipalForm, HODForm, StaffForm, StudentForm

# Dashboard View
def dashboard(request):
    """Main dashboard with summary statistics"""
    context = {
        'departments_count': Department.objects.count(),
        'principals_count': Principal.objects.count(),
        'hods_count': HOD.objects.count(),
        'staff_count': Staff.objects.count(),
        'students_count': Student.objects.count(),
    }
    return render(request, 'frontend_app1/dashboard.html', context)

# ========== DEPARTMENT VIEWS ==========
def department_list(request):
    """List all departments"""
    departments = Department.objects.all()
    return render(request, 'frontend_app1/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department created successfully!')
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'frontend_app1/department_form.html', {'form': form})

def department_update(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully!')
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'frontend_app1/department_form.html', {'form': form})

def department_delete(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Department deleted successfully!')
        return redirect('department_list')
    return render(request, 'frontend_app1/department_confirm_delete.html', {'department': department})

# ========== PRINCIPAL VIEWS ==========
def principal_list(request):
    """List all principals"""
    principals = Principal.objects.all()
    return render(request, 'frontend_app1/principal_list.html', {'principals': principals})

def principal_create(request):
    if request.method == 'POST':
        form = PrincipalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Principal created successfully!')
            return redirect('principal_list')
    else:
        form = PrincipalForm()
    return render(request, 'frontend_app1/principal_form.html', {'form': form})

def principal_update(request, id):
    principal = get_object_or_404(Principal, id=id)
    if request.method == 'POST':
        form = PrincipalForm(request.POST, instance=principal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Principal updated successfully!')
            return redirect('principal_list')
    else:
        form = PrincipalForm(instance=principal)
    return render(request, 'frontend_app1/principal_form.html', {'form': form})

def principal_delete(request, id):
    principal = get_object_or_404(Principal, id=id)
    if request.method == 'POST':
        principal.delete()
        messages.success(request, 'Principal deleted successfully!')
        return redirect('principal_list')
    return render(request, 'frontend_app1/principal_confirm_delete.html', {'principal': principal})

# ========== HOD VIEWS ==========
def hod_list(request):
    """List all HODs"""
    hods = HOD.objects.all()
    return render(request, 'frontend_app1/hod_list.html', {'hods': hods})

def hod_create(request):
    if request.method == 'POST':
        form = HODForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'HOD created successfully!')
            return redirect('hod_list')
    else:
        form = HODForm()
    return render(request, 'frontend_app1/hod_form.html', {'form': form})

def hod_update(request, id):
    hod = get_object_or_404(HOD, id=id)
    if request.method == 'POST':
        form = HODForm(request.POST, instance=hod)
        if form.is_valid():
            form.save()
            messages.success(request, 'HOD updated successfully!')
            return redirect('hod_list')
    else:
        form = HODForm(instance=hod)
    return render(request, 'frontend_app1/hod_form.html', {'form': form})

def hod_delete(request, id):
    hod = get_object_or_404(HOD, id=id)
    if request.method == 'POST':
        hod.delete()
        messages.success(request, 'HOD deleted successfully!')
        return redirect('hod_list')
    return render(request, 'frontend_app1/hod_confirm_delete.html', {'hod': hod})

# ========== STAFF VIEWS ==========
def staff_list(request):
    """List all staff"""
    staffs = Staff.objects.all()
    return render(request, 'frontend_app1/staff_list.html', {'staffs': staffs})

def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff created successfully!')
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'frontend_app1/staff_form.html', {'form': form})

def staff_update(request, id):
    staff = get_object_or_404(Staff, id=id)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff updated successfully!')
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'frontend_app1/staff_form.html', {'form': form})

def staff_delete(request, id):
    staff = get_object_or_404(Staff, id=id)
    if request.method == 'POST':
        staff.delete()
        messages.success(request, 'Staff deleted successfully!')
        return redirect('staff_list')
    return render(request, 'frontend_app1/staff_confirm_delete.html', {'staff': staff})

# ========== STUDENT VIEWS ==========
def student_list(request):
    """List all students"""
    students = Student.objects.all()
    return render(request, 'frontend_app1/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'frontend_app1/student_form.html', {'form': form})

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'frontend_app1/student_form.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'frontend_app1/student_confirm_delete.html', {'student': student})
