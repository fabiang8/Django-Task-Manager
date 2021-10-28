from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskCategory(models.Model):
	category = models.CharField(max_length=128, null=True,unique=True)
	def __str__(self):
		return self.category


class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	complete = models.BooleanField(default=False)
	category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, null=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['complete']
