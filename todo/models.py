from django.db import models

# Create your models here.
class ToDoItem(models.Model):
	name = models.TextField(max_length=100,default="",null=False,blank=False)
	task = models.TextField(max_length=100,default=None,blank=True,null=True)
	addedon = models.TextField(max_length=100,default="",blank=False,null=False)
	duedate = models.TextField(max_length=100,default="",blank=False,null=False)
