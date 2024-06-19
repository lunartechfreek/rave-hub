from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Festival

class FestivalList(generic.ListView):
    model = Festival
    template_name = "event/index.html"
    paginate_by = 6

    def get_queryset(self):
        # Ensures festivals that are in the past are not displayed
        return Festival.objects.filter(approved=True, date__gte=timezone.now().date()).order_by('date')

def festival_list(request):
    print("festival_list view called")
    festivals = Festival.objects.filter(date__gte=timezone.now().date(), approved=True).order_by('date')
    print(festivals)
    return render(request, 'event/festival_list.html', {'festivals': festivals})

def festival_detail(request, id):
    festival = get_object_or_404(Festival, id=id)
    return render(request, 'event/festival_detail.html', {'festival': festival})
