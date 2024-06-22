from django.views import generic
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Festival
from .forms import FestivalForm


class FestivalList(generic.ListView):
    model = Festival
    template_name = "event/index.html"
    paginate_by = 6

    def get_queryset(self):
        # Ensures festivals that are in the past are not displayed
        return Festival.objects.filter(approved=True, date__gte=timezone.now().date()).order_by('date')


def festival_list(request):
    festivals = Festival.objects.filter(date__gte=timezone.now().date(), approved=True).order_by('date')
    return render(request, 'event/festival_list.html', {'festivals': festivals})


def festival_detail(request, id):
    festival = get_object_or_404(Festival, id=id)
    return render(request, 'event/festival_detail.html', {'festival': festival})


@login_required
def add_festival(request):
    if request.method == 'POST':
        form = FestivalForm(request.POST)
        if form.is_valid():
            festival = form.save(commit=False)
            festival.event_manager = request.user
            festival.approved = False
            festival.save()
            form.save_m2m()
            messages.add_message(
                request, messages.SUCCESS,
                'Event submitted and awaiting approval'
            )
            return redirect('festival_list')
    else:
        form = FestivalForm()
    return render(request, 'event/add_festival.html', {'form': form})