from . import views
from django.urls import path

urlpatterns = [
    path('about', views.about_us, name='about'),
]