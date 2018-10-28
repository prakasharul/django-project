from django.urls import path

from . import views
urlpatterns = [
	path('' ,views.projects_list , name="projects"),
	path('project/new', views.project_new, name="project-add")

]