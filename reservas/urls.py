from django.urls import path
from . import views

urlpatterns = [
    path("reservar/", views.reservar, name="reservar"),
    path("eventos/", views.eventos_reservas, name="eventos_reservas"),
    path("calendario/", views.calendario, name="calendario"),
    path("datas/", views.datas_ocupadas, name="datas_ocupadas"),
    path('', views.home, name='home'),
    path("api/reservas/", views.api_reservas, name="api_reservas"),
    path('', views.home, name='home'),
         
         
]