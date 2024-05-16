from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        abstract = True


class Presupuesto(BaseModel):
    monto = models.PositiveBigIntegerField()
    monto_original = models.PositiveBigIntegerField()

    def  __str__(self) -> str:
        return f'{self.id}'


class Factura(BaseModel):
    pdf = models.FileField(upload_to='pdfs')
    cantidad = models.PositiveBigIntegerField()
    precio_unitario = models.PositiveBigIntegerField()
    descripcion = models.TextField()
    iva = models.BooleanField()
    subtotal = models.PositiveBigIntegerField(null=True, blank=True)
    total = models.PositiveBigIntegerField(null=True, blank=True)
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.subtotal:
            self.subtotal = self.cantidad * self.precio_unitario
        if not self.total:
            self.total = self.subtotal if not self.iva else self.subtotal * 1.16
        super().save(*args, **kwargs)


    def  __str__(self) -> str:
        return f'{self.id}'
