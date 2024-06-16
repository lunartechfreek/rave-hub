from django.views import generic
from django.utils import timezone
from .models import Festival

class FestivalList(generic.ListView):
    model = Festival
    template_name = 'festival_list.html'

    def get_queryset(self):
        # Ensures festivals that are in the past are not displayed
        return Festival.objects.filter(approved=True, date__gte=timezone.now().date())