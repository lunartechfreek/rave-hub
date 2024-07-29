from django.views import generic
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_index'] = True  # Add this line to indicate the index page
        return context


def festival_list(request):
    festivals = Festival.objects.filter(date__gte=timezone.now().date(), approved=True).order_by('date')
    return render(request, 'event/festival_list.html', {'festivals': festivals})


def festival_detail(request, id):
    festival = get_object_or_404(Festival, id=id)
    # Ensures duplicate genres are not displayed
    genres = {artist.genre.name for artist in festival.artists.all()}
    return render(request, 'event/festival_detail.html', {'festival': festival, 'genres': genres})


@login_required
def add_festival(request):
    if request.method == 'POST':
        form = FestivalForm(request.POST, request.FILES)
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


@login_required
def edit_festival(request, id):
    festival = get_object_or_404(Festival, id=id, event_manager=request.user)

    if request.user != festival.event_manager:
        messages.error(request, 'You do not have permission to edit this festival.')
        return redirect('festival_detail', id=festival.id)
    
    if request.method == 'POST':
        form = FestivalForm(request.POST, request.FILES, instance=festival)
        if form.is_valid():
            festival = form.save(commit=False)
            festival.approved = False
            festival.save()
            form.save_m2m()
            messages.success(request, 'Festival updated successfully and is awaiting approval.')
            return redirect('festival_detail', id=festival.id)
    else:
        form = FestivalForm(instance=festival)
    
    return render(request, 'event/edit_festival.html', {'form': form, 'festival': festival})


@login_required
def delete_festival(request, id):
    festival = get_object_or_404(Festival, id=id)

    if request.user != festival.event_manager:
        messages.error(request, 'You do not have permission to delete this festival.')
        return redirect('festival_detail', id=festival.id)

    if request.method == 'POST':
        festival.delete()
        messages.success(request, 'Festival deleted successfully.')
        return redirect('festival_list')

    return redirect('festival_detail', id=festival.id)


def festival_search(request):
    query = request.GET.get('q')
    festivals = Festival.objects.all()

    if query:
        festivals = festivals.filter(
            Q(name__icontains=query) |
            Q(artists__name__icontains=query) |
            Q(artists__genre__name__icontains=query)
        ).distinct()

    return render(request, 'event/festival_search.html', {'festivals': festivals, 'query': query})


def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    festivals = Festival.objects.filter(event_manager=user)
    approved_festivals = festivals.filter(approved=True)
    pending_festivals = festivals.filter(approved=False)
    # return render(request, 'event/user_profile.html', {'user': user, 'festivals': festivals, 'pending_festivals': pending_festivals})
    return render(request, 'event/user_profile.html', {
        'user': user,
        'approved_festivals': approved_festivals,
        'pending_festivals': pending_festivals
    })