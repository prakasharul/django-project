from django.shortcuts import render
from django.contrib.auth.models import User

from . models import projects
from . tables import projectTable
from . forms import projectForm

# class projectList(DatatableView):
# 	model = projects
# 	# template_name="projectslist.html"



def projects_list(request):
	data = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Tom'}]
	projectz = projectTable(projects.objects.all())
	return render(request, "projectlist/projects_list.html", {'projectz':projectz})

def project_new(request):
	
	if request.method == 'POST':
		instance = projectForm

	else:
		form = 	projectForm	
	return render(request, 'projectlist/project_edit.html', {'project_form': form})	

