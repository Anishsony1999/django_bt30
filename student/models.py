from django.db import models

# ORM -> Object Relational Mapping

class Student(models.Model):
    name = models.CharField(name='name',max_length=10)
    clas = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    add = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
class Country(models.Model) :

    country_name = models.CharField(max_length=30)

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=30)

class Dis(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    dis_name = models.CharField(max_length=30)
