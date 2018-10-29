from django.urls import path, re_path

from . import views
urlpatterns = [
	path('' ,views.projects_list , name="projects"),
	re_path(r'project/new/$', views.project_new, name="project-add"),
	re_path(r'project/update/(?P<pk>\d+)$', views.project_update, name="project-update"),
	re_path(r'^project/delete/(?P<pk>\d+)$', views.project_delete, name="project-delete")

]