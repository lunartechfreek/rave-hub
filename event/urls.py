from . import views
from django.urls import path

urlpatterns = [
    path('', views.FestivalList.as_view(), name='home'),
]