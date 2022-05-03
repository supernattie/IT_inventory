from django.db import models
from django import forms


class EmployeeList(models.Model):
    emp_id = models.CharField(max_length=4, unique=True)
    emp_name = models.CharField(max_length=30)
    emp_lastname = models.CharField(max_length=30)

class Location(models.Model):
    work_order = models.CharField(max_length=9, unique=True)
    location_name = models.CharField(max_length=30)
    location_address = models.TextField()

class ComputerControl(models.Model):
    com_id = models.CharField(max_length=11, unique=True)
    com_brands = models.CharField(max_length=20)
    com_serial = models.CharField(max_length=50, unique=True)
    com_processor = models.TextField()
    com_hdd_type = models.CharField(max_length=15)
    com_hdd_cap = models.CharField(max_length=5)
    com_ram = models.CharField(max_length=5)
    com_GPU = models.TextField()
    com_owner = models.ForeignKey(EmployeeList, on_delete=models.CASCADE)
    com_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    com_note = models.TextField(null=True, blank=True)

class DisplayControl(models.Model):
    dis_id = models.CharField(max_length=11, unique=True)
    dis_brands = models.CharField(max_length=20)
    dis_serial = models.CharField(max_length=50, unique=True)
    dis_size = models.CharField(max_length=10)
    dis_owner = models.ForeignKey(EmployeeList, on_delete=models.CASCADE)
    dis_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    dis_note = models.TextField(null=True, blank=True)

class UPSControl(models.Model):
    ups_id = models.CharField(max_length=11, unique=True)
    ups_brands = models.CharField(max_length=20)
    ups_serial = models.CharField(max_length=50, unique=True)
    ups_owner = models.ForeignKey(EmployeeList, on_delete=models.CASCADE)
    ups_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    ups_note = models.TextField(null=True, blank=True)

class LicenseControl(models.Model):
    lic_brands = models.CharField(max_length=20)
    lic_key = models.CharField(max_length=50, unique=True)
    lic_activate_date = models.DateField()
    lic_expire_date = models.DateField()
    lic_owner = models.ForeignKey(EmployeeList, on_delete=models.CASCADE)
    lic_note = models.TextField(null=True, blank=True)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeList
        fields = '__all__'
        labels = {
            'emp_id' : 'Employee ID',
            'emp_name' : 'Employee Name',
            'emp_lastname' : 'Employee Lastname'
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        labels = {
            'work_order' : 'Work Order',
            'location_name' : 'Location',
            'location_address' : 'Address'
        }

class ComputerForm(forms.ModelForm):
    class Meta:
        model = ComputerControl
        fields = '__all__'
        labels = {
            'com_id' : 'Computer ID',
            'com_brands' : 'Brands',
            'com_serial' : 'Serial Number',
            'com_processor' : 'Microprocessor',
            'com_hdd_type' : 'Harddisk Type',
            'com_hdd_cap' : 'Harddisk Capacity',
            'com_ram' : 'RAM',
            'com_GPU' : 'GPU',
            'com_owner' : 'Owner',
            'com_location' : 'Computer Location',
            'com_note' : 'Note'
        }

class DisplayForm(forms.ModelForm):
    class Meta:
        model = DisplayControl
        fields = '__all__'
        labels = {
            'dis_id' : 'Display ID',
            'dis_brands' : 'Brands',
            'dis_serial' : 'Serial Number',
            'dis_size' : 'Display size',
            'dis_owner' : 'Owner',
            'dis_location' : 'Display Location',
            'dis_note' : 'Note'
        }

class UPSForm(forms.ModelForm):
    class Meta:
        model = UPSControl
        fields = '__all__'
        labels = {
            'ups_id' : 'Display ID',
            'ups_brands' : 'Brands',
            'ups_serial' : 'Serial Number',
            'ups_owner' : 'Owner',
            'ups_location' : 'UPS Location',
            'ups_note' : 'Note'
        }

class LicenseForm(forms.ModelForm):
    class Meta:
        model = LicenseControl
        fields = '__all__'
        labels = {
            'lic_brands' : 'Program Name',
            'lic_key' : 'Key license',
            'lic_activate_date' : 'Activate date',
            'lic_expire_date' : 'Expire date',
            'lic_owner' : 'Owner',
            'lic_note' : 'Note'
        }