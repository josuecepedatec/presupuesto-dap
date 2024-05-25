from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import Factura, Presupuesto

class Command(BaseCommand):
    help = 'Crea los grupos Facturas y Presupuestos y asigna los permisos correspondientes'

    def handle(self, *args, **kwargs):
        # Crear o obtener el grupo Facturas
        facturas_group, created = Group.objects.get_or_create(name='Facturas')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo Facturas creado'))
        else:
            self.stdout.write('Grupo Facturas ya existe')

        # Crear o obtener el grupo Presupuestos
        presupuestos_group, created = Group.objects.get_or_create(name='Presupuestos')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo Presupuestos creado'))
        else:
            self.stdout.write('Grupo Presupuestos ya existe')

        # Obtener el ContentType de Factura y Presupuesto
        factura_ct = ContentType.objects.get_for_model(Factura)
        presupuesto_ct = ContentType.objects.get_for_model(Presupuesto)

        # Obtener todos los permisos para Factura y asignarlos al grupo Facturas
        factura_permisos = Permission.objects.filter(content_type=factura_ct)
        facturas_group.permissions.set(factura_permisos)
        self.stdout.write(self.style.SUCCESS('Permisos asignados al grupo Facturas'))

        # Obtener todos los permisos para Presupuesto y asignarlos al grupo Presupuestos
        presupuesto_permisos = Permission.objects.filter(content_type=presupuesto_ct)
        presupuestos_group.permissions.set(presupuesto_permisos)
        self.stdout.write(self.style.SUCCESS('Permisos asignados al grupo Presupuestos'))