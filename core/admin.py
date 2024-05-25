from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from .models import Factura, Presupuesto, Area, SubArea, Proveedor, TipoDeGasto, UserAreaOrSubArea



def presupuestos_query(request, q = None):

    if q:
        presupuestos = q
    else:
        presupuestos = Presupuesto.objects.all()

    if request.user.is_superuser:
        return presupuestos

    try:
        u = UserAreaOrSubArea.objects.get(user=request.user)
        area = u.area
        sub_area = u.sub_area

        if area.nombre == 'General':
            return presupuestos
        if sub_area and sub_area.nombre != 'No_Aplica':
            return presupuestos.filter(area__id=area.pk, sub_area__id=sub_area.pk)
        if area:
            return presupuestos.filter(area__id=area.pk)

    except UserAreaOrSubArea.DoesNotExist:
        pass
    return presupuestos.none()


class FacturaAdmin(admin.ModelAdmin):
    readonly_fields_non_superuser = ['pdf', 'cantidad', 'precio_unitario', 'descripcion', 'iva', 'subtotal', 'total', 'presupuesto', 'proveedor']

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields_non_superuser
        return super().get_readonly_fields(request, obj)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        presupuestos = presupuestos_query(request)
        return qs.filter(presupuesto__in=presupuestos)

class PresupuestoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return presupuestos_query(request, qs)



admin.site.register(Factura, FacturaAdmin)
admin.site.register(Presupuesto,  PresupuestoAdmin)
admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Proveedor)
admin.site.register(TipoDeGasto)
admin.site.register(UserAreaOrSubArea)