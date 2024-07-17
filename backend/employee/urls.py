from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

employee_router = DefaultRouter()
employee_router.register(r'employees', EmployeeViewSet)
