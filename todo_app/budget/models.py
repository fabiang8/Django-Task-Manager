from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BudgetCategory(models.Model):
	category = models.CharField(max_length=128, null=True,unique =True)
	def __str__(self):
		return self.category
class Budget(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE, null=True)
	projected = models.PositiveIntegerField(null=True, blank=False, default=0)
	actual = models.PositiveIntegerField(null=True, blank=False, default=0)
	balance = models.IntegerField(null=True, default=0)

	