from django.urls import path, include
from .views import index, editar_monto, extraer_monto, login_view, crear_factura, facturas, presupuestos, logout_view, PresupuestoListView

urlpatterns = [
    path('', index, name='index'),
    path('editar-monto/', editar_monto, name='editar-monto'),
    path('facturas/', facturas, name='facturas'),
    path('presupuestos/', presupuestos, name='presupuestos'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('crear-factura/', crear_factura, name='crear_factura'),
    path('extraer-monto/', extraer_monto, name='extraer_monto'),
    path('api/presupuestos/', PresupuestoListView.as_view(), name='presupuesto-list'),
]
