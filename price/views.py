from django.shortcuts import render, redirect
from .models import Cotizacion1, Cotizacion2, Cotizacion3, SimpleUsuario

# Define bookshelf models (Hardcoded since they won't be in the DB)
BOOKSHELF_MODELS = [
    {"id": 1, "name": "Modelo 1", "description": "Con dos secciones laterales y repisas ajustables.", "image_url": "/static/images/Modelo1.png"},
    {"id": 2, "name": "Modelo 2", "description": "Vertical con repisas y altura personalizable de la primera repisa.", "image_url": "/static/images/Modelo2.png"},
    {"id": 3, "name": "Modelo 3", "description": "Con repisas pequeñas y una repisa inferior con cajón integrado.", "image_url": "/static/images/Modelo3.jpeg"},
]

def shop(request):
    if request.method == 'POST':
        try:
            model_id = int(request.POST.get("model_id"))
            selected_model = next((m for m in BOOKSHELF_MODELS if m["id"] == model_id), None)
            ancho = float(request.POST.get('ancho'))
            alto = float(request.POST.get('alto'))
            profundidad = float(request.POST.get('profundidad'))
            correo = request.POST.get('correo')
        except (ValueError, TypeError):
            return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Valores inválidos'})

        if not selected_model:
            return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Seleccione un modelo válido'})

        if selected_model['name'] == 'Modelo 1':
            try:
                espesor = float(request.POST.get('espesor'))
                n_cajones_der = int(request.POST.get('n_cajones_der'))
                n_cajones_izq = int(request.POST.get('n_cajones_izq'))
            except (ValueError, TypeError):
                return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Valores inválidos'})

            usuario, created = SimpleUsuario.objects.get_or_create(email=correo)
            nueva_cotizacion = Cotizacion1(
                usuario=usuario,
                alto=alto,
                ancho=ancho,
                fondo=profundidad,
                espesor=espesor,
                n_cajones_der=n_cajones_der,
                n_cajones_izq=n_cajones_izq,
            )
        elif selected_model['name'] == 'Modelo 2':
            try:
                alturarepisa = float(request.POST.get('alturarepisa'))
                Nrepisas = int(request.POST.get('Nrepisas'))
                puerta = request.POST.get('puerta') == 'on'
            except (ValueError, TypeError):
                return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Valores inválidos'})
            usuario, created = SimpleUsuario.objects.get_or_create(email=correo)
            nueva_cotizacion = Cotizacion2(
                usuario=usuario,
                alto=alto,
                ancho=ancho,
                fondo=profundidad,
                alturarepisa=alturarepisa,
                Nrepisas=Nrepisas,
                puerta=puerta,
            )
            
        elif selected_model['name'] == 'Modelo 3':
            try:
                altura_1 = float(request.POST.get('altura_1'))
                altura_2 = float(request.POST.get('altura_2'))
                N_repisas_p = int(request.POST.get('N_repisas_p'))
                cajon = request.POST.get('cajon') == 'on'
            except (ValueError, TypeError):
                return render(request, 'shop.html', {'models': BOOKSHELF_MODELS, 'error': 'Valores inválidos'})
            usuario, created = SimpleUsuario.objects.get_or_create(email=correo)
            nueva_cotizacion = Cotizacion3(
                usuario=usuario,
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

def landing(request):
    return render(request, 'landing.html')

def success(request):
    return render(request, 'success.html')
