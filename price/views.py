from django.shortcuts import render, redirect
from .models import Cotizacion1, Cotizacion2, Cotizacion3

# Define bookshelf models (Hardcoded since they won't be in the DB)
BOOKSHELF_MODELS = [
    {"id": 1, "name": "Cotizacion1", "description": "A sturdy oak bookshelf.", "image_url": "/static/images/Modelo1.jpg"},
    {"id": 2, "name": "Cotizacion2", "description": "A sleek glass bookshelf.", "image_url": "/static/images/Modelo2.png"},
    {"id": 3, "name": "Cotizacion3", "description": "A strong metal bookshelf.", "image_url": "/static/images/Modelo3.png"},
]


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

        if selected_model['name'] == 'Cotizacion1':
            try:
                espesor = float(request.POST.get('espesor'))
                n_cajones_der = int(request.POST.get('n_cajones_der'))
                n_cajones_izq = int(request.POST.get('n_cajones_izq'))
            except (ValueError, TypeError):
                return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Valores inválidos'})

            nueva_cotizacion = Cotizacion1(
                alto=alto,
                ancho=ancho,
                fondo=profundidad,
                espesor=espesor,
                n_cajones_der=n_cajones_der,
                n_cajones_izq=n_cajones_izq,
            )
        elif selected_model['name'] in ['Cotizacion2', 'Cotizacion3']:
            try:
                altura_1 = float(request.POST.get('altura_1'))
                altura_2 = float(request.POST.get('altura_2'))
                N_repisas_p = int(request.POST.get('N_repisas_p'))
                cajon = request.POST.get('cajon') == 'on'
            except (ValueError, TypeError):
                return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Valores inválidos'})

            if selected_model['name'] == 'Cotizacion2':
                nueva_cotizacion = Cotizacion2(
                    alto=alto,
                    ancho=ancho,
                    fondo=profundidad,
                    altura_1=altura_1,
                    altura_2=altura_2,
                    N_repisas_p=N_repisas_p,
                    cajon=cajon,
                )
            else:
                nueva_cotizacion = Cotizacion3(
                    alto=alto,
                    ancho=ancho,
                    fondo=profundidad,
                    altura_1=altura_1,
                    altura_2=altura_2,
                    N_repisas_p=N_repisas_p,
                    cajon=cajon,
                )

        nueva_cotizacion.save()
        return redirect('success')

    return render(request, 'shop.html', {'models': BOOKSHELF_MODELS})


def success(request):
    return render(request, 'success.html')