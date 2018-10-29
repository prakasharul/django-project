from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from . models import projects

from . forms import projectForm

# class projectList(DatatableView):
# 	model = projects
# 	# template_name="projectslist.html"


@login_required(login_url='/login/')
def projects_list(request):
	"""fetch project list """
	data = projects.objects.all()
	return render(request, "projectlist/projects_list.html", {'data':data})

@login_required(login_url='/login/')
def project_new(request):
	""" create new project"""

	form = 	projectForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('projects')
	else:
		form = 	projectForm(request.GET or None)	

	return render(request, 'projectlist/project_edit.html', {'project_form': form})	

@login_required(login_url='/login/')
def project_update(request, pk):
	"""update existing project"""

	project = get_object_or_404(projects, pk=pk)
	form =  projectForm(request.POST or None, instance=project)

	if form.is_valid():
		form.save()
		return redirect('projects')
	else:
		form =  projectForm(request.POST or None, instance=project)	
		return render(request, 'projectlist/project_edit.html', {'project_form': form})	

	return HttpResponse(status=400)	

@login_required(login_url='/login/')
def project_delete(request, pk):
	"""project delete by id"""

	project = get_object_or_404(projects, pk=pk)

	if project:
		project.delete()
		return redirect('projects')

	return HttpResponse(status=405)	





