from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from employee.urls import employee_router

router = DefaultRouter()
router.registry.extend(employee_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]