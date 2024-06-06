from django.urls import path

from .views import EmployeeView, EmployeeCreateAPIView, EmployeeUpdateView

urlpatterns = [
    path('employee', EmployeeView.as_view(), name='employee-list'),
    path('employee/create', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('employee/update/<pk>', EmployeeUpdateView.as_view(), name='employee-update'),
]