from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	user = models.ManyToManyField(User)
	project_heading = models.CharField(max_length=50)

	def __str__(self):
		return self.project_heading

class Task(models.Model):
	project = models.ForeignKey(Project)
	task_heading = models.CharField(max_length=100)
	assigned_to = models.ForeignKey(User)
	due_date = models.DateTimeField()

	def __str__(self):
		return self.task_heading

class Task_comment(models.Model):
	task = models.ForeignKey(Task)
	comment_text = models.CharField(max_length=1000)

	def __str__(self):
		return self.comment_text