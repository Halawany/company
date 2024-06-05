from django.urls import path

from .views import EmployeeView, EmployeeCreateAPIView

urlpatterns = [
    path('employee', EmployeeView.as_view(), name='employee-list'),
    path('employee/create', EmployeeCreateAPIView.as_view(), name='employee-create')
]