from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')
  
class Activity(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=200)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  
class Item(models.Model):
  name = models.CharField(max_length=200)
  create_date = models.DateTimeField(auto_now_add=True)
  #create_by
  #amount
  stock = models.BooleanField(default=False)
  #purchased_date
  #purchased-by
  