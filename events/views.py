from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required, user_passes_test

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def is_company(user):
    return user.is_authenticated and user.role == 'company'

@login_required
@user_passes_test(is_company)
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def my_tickets(request):
    # логика отображения билетов пользователя
    return render(request, 'events/my_tickets.html')