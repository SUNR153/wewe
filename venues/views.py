from django.shortcuts import render, redirect
from .models import Venue
from .forms import VenueForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_company(user):
    return user.is_authenticated and user.role == 'company'

@login_required
@user_passes_test(is_company)
def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'venues/venue_list.html', {'venues': venues})

@login_required
@user_passes_test(is_company)
def venue_create(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venues:venue_list')
    else:
        form = VenueForm()
    return render(request, 'venues/venue_form.html', {'form': form})
