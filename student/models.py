from django.db import models

# ORM -> Object Relational Mapping

class Student(models.Model):
    name = models.CharField(name='name',max_length=10)
    clas = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    add = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    

class AboutModel(models.Model):
    text = models.CharField(max_length=200)