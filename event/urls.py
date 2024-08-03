from . import views
from django.urls import path

#URL patterns for event app
urlpatterns = [
    path('', views.FestivalList.as_view(), name='home'),
    path('festival/', views.festival_list, name='festival_list'),
    path('festival/<int:id>/', views.festival_detail, name='festival_detail'),
    path('festival/add/', views.add_festival, name='add_festival'),
    path('festival/<int:id>/edit/', views.edit_festival, name='edit_festival'),
    path('festival/<int:id>/delete/', views.delete_festival, name='delete_festival'),
    path('search/', views.festival_search, name='festival_search'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
]