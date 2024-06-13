from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    """ A model for artist genres (managed by site owner). """
    name = models.CharField(max_length=75, null=False, blank=False)

    def __str__(self):
        return self.name


class Artist(models.Model):
    """ A model for each artist (managed by site owner). """
    name = models.CharField(max_length=100, null=False, blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
