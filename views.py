from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from inventory.models import EmployeeList, EmployeeForm, Location, LocationForm, ComputerControl, ComputerForm, DisplayControl, DisplayForm, UPSControl, UPSForm, LicenseControl, LicenseForm
from django.urls import reverse

def employee_create(request):
    err_msg = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            row = EmployeeList.objects.filter(emp_id='emp_id')
            if row.count() == 0:
                form.save()
    else:
        form = EmployeeForm()
    return render(request, 'create-user.html', {'form':form}|{'err_msg':err_msg})

def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LocationForm()
    return render(request, 'create-location.html', {'form':form})

def computer_create(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComputerForm()
        user_data = EmployeeList.objects.all()
        location_data = EmployeeList.objects.all()
    return render(request, 'create-computer.html', {'form':form}|{'user_data':user_data}|{'location_data':location_data})

def display_create(request):
    if request.method == 'POST':
        form = DisplayForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DisplayForm()
        user_data = EmployeeList.objects.all()
        location_data = EmployeeList.objects.all()
    return render(request, 'create-display.html', {'form':form}|{'user_data':user_data}|{'location_data':location_data})

def ups_create(request):
    if request.method == 'POST':
        form = UPSForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UPSForm()
        user_data = EmployeeList.objects.all()
        location_data = EmployeeList.objects.all()
    return render(request, 'create-ups.html', {'form':form}|{'user_data':user_data}|{'location_data':location_data})

def lic_create(request):
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LicenseForm()
        user_data = EmployeeList.objects.all()
    return render(request, 'create-license.html', {'form':form}|{'user_data':user_data})

def employee_read(request):
    user_data = EmployeeList.objects.all()
    return render(request, 'list-user.html', {'user_data':user_data})

def employee_edit(request, id):
    if request.method == 'POST':
        rec = EmployeeList.objects.get(id=id)
        form = EmployeeForm(instance=rec, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        row = EmployeeList.objects.filter(id=id).values()
        form = EmployeeForm()
        return render(request, 'edit-user.html', {'form':form}|{'row':row})

def employee_delete(request, id):
    EmployeeList.objects.get(id=id).delete()
    user_data = EmployeeList.objects.filter()[:10]
    return render(request, 'list-user.html', {'user_data':user_data})