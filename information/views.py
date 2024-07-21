from django.shortcuts import render
from .models import About


def about_us(request):
    about = About.objects.all().order_by('-updated_on').first()

    return render(request, "information/about.html", {"about": about})
