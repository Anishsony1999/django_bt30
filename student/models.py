from django.db import models
from django.utils.text import slugify

# ORM -> Object Relational Mapping

class Student(models.Model):
    name = models.CharField(name='name',max_length=10)
    clas = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    add = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='image',null=True,blank=True)
    slug = models.SlugField(unique=True,blank=True)

    def save(self, *args,**kwargs):
        if not self.slug :

            self.slug = slugify(self.name)

        super().save(*args,**kwargs)
    def __str__(self):
        return self.name
    
class Country(models.Model) :

    country_name = models.CharField(max_length=30)

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=30)

class Dis(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    dis_name = models.CharField(max_length=30)
