from bookings.models import Booking
from django.shortcuts import get_object_or_404, render, redirect
from .forms import BookingForm
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def index(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings/index.html', context)

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings:index')
    else:
        form = BookingForm()
    context = {
        'form': form,
    }
    return render(request, 'bookings/create.html', context)

@login_required
@require_safe
def detail(request, pk):
    booking = Booking.objects.get(pk=pk)
    context = {
        'booking': booking
    }
    return render(request, 'bookings/detail.html', context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            return redirect('bookings:detail',  booking.pk)
    else:
        form = BookingForm(instance=booking)
    context = {
        'booking': booking,
        'form': form,
    }
    return render(request, 'bookings/update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()

    return redirect('bookings:index')
