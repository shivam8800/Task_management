from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task, Task_comment
from django.contrib.auth.models import User
from pprint import pprint

def home(request):
	all_projects = Project.objects.filter(user=request.user)
	# import ipdb; ipdb.set_trace()
	pprint(all_projects)
	return render(request, 'core/index.html', {'all_projects': all_projects})

def detail(request, pk):
	a_project = Project.objects.get(pk=pk)
	# for getting all user of an projects
	all_user =  a_project.user.all()
	project_task = Task.objects.filter(project=a_project)
	# import ipdb; ipdb.set_trace()
	return render(request, 'core/detail.html', {'project': a_project, 'users': all_user, 'tasks': project_task})

def comment(request, pk):
	a_task = Task.objects.get(pk=pk)
	task_comment = Task_comment.objects.filter(task=a_task)
	# import ipdb; ipdb.set_trace()
	return render(request, 'core/comment.html', {'task': a_task, 'comment': task_comment})
