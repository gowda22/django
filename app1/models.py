from django.db import models

# Create your models here.

class Mymodel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Cource(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Cource, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    actor_name=models.CharField(max_length=100)
    age=models.IntegerField()
    experence=models.IntegerField()
    def __str__(self):
        return self.actor_name

class Movies(models.Model):
    movie_name=models.CharField(max_length=100)
    realize_year=models.IntegerField()
    actors=models.ManyToManyField(Actor,related_name="movies")
    def __str__(self):
        return self.movie_name