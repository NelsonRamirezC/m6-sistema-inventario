from django.urls import path

from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('id/<int:id>', views.detalle_producto, name='detalle-producto'),
]
