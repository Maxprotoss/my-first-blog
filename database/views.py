from django.shortcuts import render
from .models import Evento
from django.utils import timezone
# Create your views here.

def ultimos_eventos(request):
    eventos=Evento.objects.order_by('-published_date')[:6]
    return render(request, 'blog/eventos.html', {'eventos':eventos})

    