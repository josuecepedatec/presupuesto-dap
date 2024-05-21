from django.contrib import admin

from .models import Factura, Presupuesto, Area, SubArea, Proveedor, TipoDeGasto

admin.site.register(Factura)
admin.site.register(Presupuesto)
admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Proveedor)
admin.site.register(TipoDeGasto)
