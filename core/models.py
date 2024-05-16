from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        abstract = True


class Presupuesto(BaseModel):
    presupuesto_id = models.CharField(max_length=100, unique=True)
    monto = models.FloatField()
    monto_original = models.FloatField()

    def  __str__(self) -> str:
        return f'{self.presupuesto_id}'


class Factura(BaseModel):
    pdf = models.FileField(upload_to='pdfs')
    cantidad = models.FloatField()
    precio_unitario = models.FloatField()
    descripcion = models.TextField()
    iva = models.BooleanField()
    subtotal = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.subtotal:
            self.subtotal = self.cantidad * self.precio_unitario
        if not self.total:
            self.total = self.subtotal if not self.iva else self.subtotal * 1.16
        super().save(*args, **kwargs)


    def  __str__(self) -> str:
        return f'{self.id}'
