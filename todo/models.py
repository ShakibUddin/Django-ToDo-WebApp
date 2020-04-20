from django.db import models

# Create your models here.
class ToDoItem(models.Model):
	task = models.TextField(max_length=100,default=None,blank=True,null=True)
	date = models.TextField(max_length=100,default="",blank=True,null=True)
