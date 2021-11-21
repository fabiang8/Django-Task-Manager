from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	tasks_view_hide_completed = models.BooleanField(default=False)

	@property
	def set_hide(self):
		if self.tasks_view_hide_completed is False:
			print("test1")
			self.tasks_view_hide_completed = True
			self.save()
			return self.tasks_view_hide_completed
		else:
			print("test2")
			self.tasks_view_hide_completed = False
			self.save()
			return self.tasks_view_hide_completed
		#print("threw")
		#return('') # returns none b/c cant find object
