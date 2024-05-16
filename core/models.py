from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        abstract = True


class Presupuesto(BaseModel):
    monto = models.PositiveBigIntegerField()
    monto_original = models.PositiveBigIntegerField()


class Factura(BaseModel):
    cantidad = models.PositiveBigIntegerField()
    precio_unitario = models.PositiveBigIntegerField()
    descripcion = models.TextField()
    iva = models.BooleanField()
    subtotal = models.PositiveBigIntegerField(null=True, blank=True)
    total = models.PositiveBigIntegerField(null=True, blank=True)
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)


