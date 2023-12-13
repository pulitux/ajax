from django.urls import path

from hospital import views

urlpatterns=[
    path('',views.index,name='index'),
    path('viewHospitales',views.hosps,name='hosps'),
    path('viewDoctores',views.docs,name='docs'),
    path('viewEmpleados',views.emps,name='emps'),
]

