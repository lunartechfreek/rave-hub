from django.contrib import admin
from .models import Genre, Artist, Festival
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Festival)
class FestivalAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the Festival model.
    """

    list_display = ('name', 'event_manager', 'date', 'approved')
    search_fields = ['name', 'event_manager']
    list_filter = ('approved',)


@admin.register(Artist)
class ArtistAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the Festival model.
    """

    list_display = ('name', 'genre')
    search_fields = ['name', 'genre']
    list_filter = ('genre',)


admin.site.register(Genre)
