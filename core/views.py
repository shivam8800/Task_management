from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task, Task_comment, Nested_comment
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

	for comment in task_comment:
		comment.nested_comments = comment.nested_comment_set.all()

	# import ipdb; ipdb.set_trace()
	if request.method == "POST":
		comment = request.POST.get('comment')
		new_comment  = Task_comment.objects.create(task=a_task, comment_text=comment)
		return redirect('comment', pk=pk)
	else:
		return render(request, 'core/comment.html', {'task': a_task, 'comments': task_comment})

def nestedcomment(request):
	if request.method == "POST":
		if request.is_ajax():
			replytext = request.POST.get('input')
			commentid = request.POST.get('comment_id')
			taskComment = Task_comment.objects.get(pk=commentid)
			nestedcomment = Nested_comment.objects.create(task_comment = taskComment,nested_comment_text = replytext)
			nestedcomment.save()
			return redirect('/')
		else:
			pprint("this is not ajax request")
	return render(request, 'base.html')

