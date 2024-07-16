from . import views
from django.urls import path

urlpatterns = [
    path('', views.FestivalList.as_view(), name='home'),
    path('festival/', views.festival_list, name='festival_list'),
    path('festival/<int:id>/', views.festival_detail, name='festival_detail'),
    path('festival/add/', views.add_festival, name='add_festival'),
    path('festival/<int:id>/edit/', views.edit_festival, name='edit_festival'),
]