from django.shortcuts import render
from django.views import generic
from .models import Festival

class FestivalList(generic.ListView):
    model = Festival