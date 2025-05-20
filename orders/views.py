from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm
from events.models import Event

@login_required
def order_create(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.event = event
            order.save()
            return redirect('orders:order_list')
    else:
        form = OrderForm(initial={'event': event})
    return render(request, 'orders/order_form.html', {'form': form, 'event': event})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})
