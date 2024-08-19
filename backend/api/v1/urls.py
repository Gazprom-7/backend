from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .employee import views as employee_views
from .team.views import projects as project_views
from .team.views import teams as team_views

router = DefaultRouter()
router.register(r"employee", employee_views.EmployeeViewSet)
router.register("projects", project_views.ProjectViewSet)
router.register(r"teams", team_views.TeamViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
