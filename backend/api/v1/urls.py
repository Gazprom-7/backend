from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .employee import views as employee_views
from .project import views as project_views

router = DefaultRouter()
router.register("employee", employee_views.EmployeeViewSet)
router.register("projects", project_views.ProjectViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
