from django.urls import path

from prueba import views

urlpatterns=[
    path('',views.index,name='index'),
    path('viewPersonas',views.perso,name='perso'),
    path('viewLenguajes',views.lenguaj,name='lenguaj'),
]