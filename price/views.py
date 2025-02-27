from django.shortcuts import render, redirect
from .models import Cotizacion


# Define bookshelf models (Hardcoded since they won't be in the DB)
BOOKSHELF_MODELS = [
    {"id": 1, "name": "Modelo 1", "description": "A sturdy oak bookshelf.", "image_url": "/static/images/Modelo1.jpg"},
    {"id": 2, "name": "Modelo 2", "description": "A sleek glass bookshelf.", "image_url": "/static/images/Modelo2.png"},
    {"id": 3, "name": "Modelo 3", "description": "A strong metal bookshelf.", "image_url": "/static/images/Modelo3.png"},
]


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


def landing(request):
    return render(request, 'landing.html')


def shop(request):
    if request.method == 'POST':
        try:
            model_id = int(request.POST.get("model_id"))
            selected_model = next((m for m in BOOKSHELF_MODELS if m["id"] == model_id), None)
            ancho = float(request.POST.get('ancho'))
            alto = float(request.POST.get('alto'))
            profundidad = float(request.POST.get('profundidad'))
        except (ValueError, TypeError):
            return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Valores inválidos'})

        if not selected_model:
            return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Seleccione un modelo válido'})

        nueva_cotizacion = Cotizacion(
            total=0,
            detalles=f"Cotización para {selected_model['name']}",
            ancho=ancho,
            alto=alto,
            profundidad=profundidad,
        )
        nueva_cotizacion.save()
        return redirect('success')

    return render(request, 'shop.html', {'models': BOOKSHELF_MODELS})

def success(request):
    return render(request, 'success.html')