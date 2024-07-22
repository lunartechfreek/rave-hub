from . import views
from django.urls import path

urlpatterns = [
    path('about', views.about_us, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),
]