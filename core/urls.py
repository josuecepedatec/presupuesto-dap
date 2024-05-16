from django.urls import path, include
from .views import index, login_view, crear_factura, facturas, presupuestos

urlpatterns = [
    path('', index, name='index'),
    path('facturas/', facturas, name='facturas'),
    path('presupuestos/', presupuestos, name='presupuestos'),
    path('login/', login_view, name='login'),
    path('crear-factura/', crear_factura, name='crear_factura'),
]