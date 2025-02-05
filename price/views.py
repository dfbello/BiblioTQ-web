from django.shortcuts import render, redirect
from .models import Cotizacion

def home(request):
    if request.method == 'POST':
        try:
            ancho = float(request.POST.get('ancho'))
            alto = float(request.POST.get('alto'))
            profundidad = float(request.POST.get('profundidad'))
        except (ValueError, TypeError):
            return render(request, 'home.html', {'error': 'Valores inválidos'})

        nueva_cotizacion = Cotizacion(
            total=0,
            detalles="Cotización generada con dimensiones",
            ancho=ancho,
            alto=alto,
            profundidad=profundidad,
        )
        nueva_cotizacion.save()
        return redirect('home')
    return render(request, 'home.html')
