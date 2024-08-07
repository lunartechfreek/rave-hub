from django.contrib import admin
from .models import About, ContactUs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the about model.
    """
    list_display = ('content', 'updated_on')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the recieved messages
    from users.
    """
    list_display = ('name', 'email', 'message', 'read')
    list_filter = ('read',)
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"
