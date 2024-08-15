from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .employee import views

router = DefaultRouter()
router.register("employee", views.EmployeeViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
