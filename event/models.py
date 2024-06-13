import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


TIME_SLOTS = [
    (datetime.time(hour, 0).strftime("%H:%M"),
    datetime.time(hour, 0).strftime("%H:%M")) for hour in range(24)]


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


class Festival(models.Model):
    """ A model for each festival of events. """
    name = models.CharField(max_length=100, null=False, blank=False)
    event_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    artists = models.ManyToManyField(Artist, related_name="festivals")
    website = models.URLField(max_length=256, blank=True, null=True)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(choices=TIME_SLOTS, null=False, blank=False)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=False, blank=False)

    def __str__(self):
        return self.name

    def clean(self):
        """ Ensure a user cannot enter a date in the past. """
        super().clean()
        if self.date < timezone.now().date():
            raise ValidationError("The date cannot be in the past.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


