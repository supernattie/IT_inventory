from django.urls import path
from . import views

urlpatterns = [
    path('create/user/', views.employee_create, name='emp_create'),
    path('create/location/', views.location_create, name='location_create'),
    path('create/computer/', views.computer_create, name='com_create'),
    path('create/display/', views.display_create, name='dis_create'),
    path('create/ups/', views.ups_create, name='ups_create'),
    path('create/license/', views.lic_create, name='lic_create'),
    path('list/user/', views.employee_read, name='emp_list'),
    path('edit/user/<int:id>/', views.employee_edit, name='user_edit'),
    path('delete/user/<int:id>/', views.employee_delete, name='user_delete')
]