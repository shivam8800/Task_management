from django.contrib import admin
from .models import Project, Task, Task_comment
# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Task_comment)
