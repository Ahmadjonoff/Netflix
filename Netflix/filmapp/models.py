from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    gender = models.CharField(max_length=6, choices=[('Ayol', 'Ayol'), ('Erkak', 'Erkak')])
    nation = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    yonalishi = models.CharField(max_length=15)
    actors = models.ManyToManyField(Actor)
    imdb = models.FloatField()
    def __str__(self):
        return self.title