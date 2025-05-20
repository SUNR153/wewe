from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from events.models import Event

@login_required
def buy_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.event = event
            ticket.save()
            return redirect('tickets:ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_buy.html', {'form': form, 'event': event})

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, user=request.user)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})
