from django.views import generic
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Festival
from .forms import FestivalForm


class FestivalList(generic.ListView):
    """
    Returns all published Festivals in :model:`event.Festival`
    and displays them in a page of six events.

    **Context**

    ``queryset``
        All published instances of :model:`event.Festival`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`event/index.html`
    """
    model = Festival
    template_name = "event/index.html"
    paginate_by = 6

    def get_queryset(self):
        return Festival.objects.filter(
            approved=True, date__gte=timezone.now().date()).order_by('date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_index'] = True
        return context


def festival_list(request):
    """
    Returns all published Festivals in :model:`event.Festival`
    and displays them in a page of eight events.

    **Context**

    ``festivals``
        All published instances of :model:`event.Festival`
    ``paginator``
        Number of posts per page.
    ``page``
        Retrieve the 'page' parameter from the GET request.
    ``context``
        Create a context dictionary for rendering the template.

    **Template:**

    :template:`event/festival_list.html`
    """
    festivals = Festival.objects.filter(
        date__gte=timezone.now().date(), approved=True).order_by('date')

    paginator = Paginator(festivals, 8)

    page = request.GET.get('page')
    try:
        festivals = paginator.page(page)
    except PageNotAnInteger:
        festivals = paginator.page(1)
    except EmptyPage:
        festivals = paginator.page(paginator.num_pages)

    context = {
        'festivals': festivals,
        'is_paginated': festivals.has_other_pages(),
        'page_obj': festivals,
    }

    return render(request, 'event/festival_list.html', context)


def festival_detail(request, id):
    """
    Display an individual :model:`event.Festival`

    **Context**

    ``festival``
        An instance of :model:`event.Festival`
    ``genres``
        Create a set of genre names from all artists in the festival.


    **Template:**

    :template:`event/festival_detail.html`
    """
    festival = get_object_or_404(Festival, id=id)
    # Ensures duplicate genres are not displayed
    genres = {artist.genre.name for artist in festival.artists.all()}
    return render(request, 'event/festival_detail.html', {
        'festival': festival, 'genres': genres
        })


@login_required
def add_festival(request):
    """
    Handle the add festival form.

    **Context**

    ``form``
        Initiate the form with POST data and file uploads.
    ``festival``
        Creates a festival instance from the form data.

    **Template:**

    :template:`event/add_festival.html`
    """
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
    """
    Handle the editing of an event.

    **Context**

    ``festival``
        An instance of :model:`event.Festival`
    ``form``
        Initiate the form with POST data and file uploads.

    **Template:**

    :template:`event/add_festival.html`
    """
    festival = get_object_or_404(Festival, id=id, event_manager=request.user)

    if request.user != festival.event_manager:
        messages.error(
            request, 'You do not have permission to edit this festival.'
            )
        return redirect('festival_detail', id=festival.id)

    if request.method == 'POST':
        form = FestivalForm(request.POST, request.FILES, instance=festival)
        if form.is_valid():
            festival = form.save(commit=False)
            festival.approved = False
            festival.save()
            form.save_m2m()
            messages.success(
                request,
                'Festival updated successfully and is awaiting approval.'
                )
            return redirect('festival_detail', id=festival.id)
    else:
        form = FestivalForm(instance=festival)

    return render(request, 'event/edit_festival.html', {
            'form': form, 'festival': festival
            })


@login_required
def delete_festival(request, id):
    """
    Handle the deletion of an event.

    **Context**

    ``festival``
        An instance of :model:`event.Festival`

    **Template:**

    :template:`event/festival_detail.html`
    """
    festival = get_object_or_404(Festival, id=id)

    if request.user != festival.event_manager:
        messages.error(
            request, 'You do not have permission to delete this festival.'
                )
        return redirect('festival_detail', id=festival.id)

    if request.method == 'POST':
        festival.delete()
        messages.success(request, 'Festival deleted successfully.')
        return redirect('festival_list')

    return redirect('festival_detail', id=festival.id)


def festival_search(request):
    """
    Handle the search for events.

    **Context**

    ``query``
        Retrieve the value of the 'q' query parameter from the GET request.
    ``festivals``
        Retrieves all Festival instances from :model:`event.Festival
        that are approved
    ``page``
        Retrieves the page parameter from the url
    ``paginator``
        creates a new page if there are more than 8 events
    ``context``
        Create a context dictionary for rendering the template.

    **Template:**

    :template:`event/festival_search.html`
    """
    query = request.GET.get('q')
    festivals = Festival.objects.filter(approved=True)

    if query:
        festivals = festivals.filter(
            Q(name__icontains=query) |
            Q(artists__name__icontains=query) |
            Q(artists__genre__name__icontains=query)
        ).distinct()

    page = request.GET.get('page', 1)
    paginator = Paginator(festivals, 8)

    try:
        festivals = paginator.page(page)
    except PageNotAnInteger:
        festivals = paginator.page(1)
    except EmptyPage:
        festivals = paginator.page(paginator.num_pages)

    context = {
        'festivals': festivals,
        'query': query,
        'is_paginated': festivals.has_other_pages(),
        'paginator': paginator,
        'page_obj': festivals,
    }

    return render(request, 'event/festival_search.html', context)


def user_profile(request, user_id):
    """
    Handle the search for events.

    **Context**

    ``event_manager``
        Retrieve an instance of :model:`auth.User`.
    ``festivals``
        Retrieves all Festival instances of :model:`event.Festival
        that have been added by the logged in user.
    ``approved_festivals``
        Retrieves all festivals that are approved.
    ``pending_festivals``
        Retrieves all festivals that are not approved.

    **Template:**

    :template:`event/user_profile.html`
    """
    event_manager = get_object_or_404(User, id=user_id)
    festivals = Festival.objects.filter(event_manager=event_manager)
    approved_festivals = festivals.filter(approved=True)
    pending_festivals = festivals.filter(approved=False)
    return render(request, 'event/user_profile.html', {
        'event_manager': event_manager,
        'approved_festivals': approved_festivals,
        'pending_festivals': pending_festivals
    })
