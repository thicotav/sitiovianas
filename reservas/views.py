from django.shortcuts import render, redirect
from .models import Reserva
from datetime import datetime

def reservar(request):

    data_entrada = request.GET.get("entrada")
    data_saida = request.GET.get("saida")

    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        data_entrada = request.POST.get("data_entrada")
        data_saida = request.POST.get("data_saida")

        entrada = datetime.strptime(data_entrada, '%Y-%m-%d').date()
        saida = datetime.strptime(data_saida, '%Y-%m-%d').date()

        conflito = Reserva.objects.filter(
            data_entrada__lte=saida,
            data_saida__gte=entrada
        ).exists()

        if conflito:
            return render(request, 'reservas/formulario.html', {
                'erro': 'Essas datas já estão reservadas.',
                'entrada': data_entrada,
                'saida': data_saida
            })

        Reserva.objects.create(
            nome_cliente=nome,
            telefone=telefone,
            data_entrada=data_entrada,
            data_saida=data_saida
        )

        return redirect("/")
    
    return render(request, "reservas/formulario.html", {
        "entrada": data_entrada,
        "saida": data_saida
        
    })

from django.http import JsonResponse

def eventos_reservas(request):
    reservas = Reserva.objects.all()

    eventos = []

    for reserva in reservas:
        eventos.append({
            "title": "Reservado",
            "start": str(reserva.data_entrada),
            "end": str(reserva.data_saida),
            "color": "#e74c3c"
        })

    return JsonResponse(eventos, safe=False)

def calendario(request):
    return render(request, "reservas/calendario.html")

from django.http import JsonResponse

def datas_ocupadas(request):
    reservas = Reserva.objects.all()

    datas = []

    for reserva in reservas:
        datas.append({
            "start": str(reserva.data_entrada),
            "end": str(reserva.data_saida)
        })
    return JsonResponse(datas, safe=False)

from django.http import JsonResponse

def datas_ocupadas(request):
    reservas = Reserva.objects.all()

    eventos = []

    for reserva in reservas:
        eventos.append({
            "start": str(reserva.data_entrada),
            "end": str(reserva.data_saida)
        })

    return JsonResponse(eventos, safe=False)

from django.shortcuts import render

def home(request):
    return render(request, 'reservas/home.html')

from django.http import JsonResponse
from datetime import timedelta
from .models import Reserva

def api_reservas(request):

    reservas = Reserva.objects.all()

    eventos = []

    for reserva in reservas:

        eventos.append({
            "title": "Reservado",
            "start": str(reserva.data_entrada),
            "end": str(reserva.data_saida + timedelta(days=1)),
            "color": "red"
        })

    return JsonResponse(eventos, safe=False)

def home(request):
    return render(request, "reservas/home.html")



# Create your views here.
