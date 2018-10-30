from django.urls import path, re_path, include
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'project-list', views.projectViewSet)

from . import views
urlpatterns = [
	re_path(r'^api/projects/', include(router.urls)),
	path('' ,views.projects_list , name="projects"),
	re_path(r'project/new/$', views.project_new, name="project-add"),
	re_path(r'project/update/(?P<pk>\d+)$', views.project_update, name="project-update"),
	re_path(r'^project/delete/(?P<pk>\d+)$', views.project_delete, name="project-delete")

]