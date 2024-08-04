from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import ContactUsForm


def about_us(request):
    """
    Returns the text from :model:`information.About`.

    **Context**

    ``about``
        Returns the text from the about field in :model:`information.About`.

    **Template:**

    :template:`event/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(request, "information/about.html", {"about": about})


def contact_us(request):
    """
    Handles the contact form submission.

    **Context**

    ``form``
        Initiate the form with POST data.

    **Template:**

    :template:`event/about.html`
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!'
                )
            return redirect('contact_us')
    else:
        form = ContactUsForm()

    return render(request, 'information/contact_us.html', {'form': form})
