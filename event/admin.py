from django.contrib import admin
from .models import Genre, Artist, Festival

# Register your models here.
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Festival)
