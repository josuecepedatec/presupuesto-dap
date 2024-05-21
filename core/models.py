from django.db import models
from django.core.exceptions import ValidationError


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        abstract = True


class Area(BaseModel):
    nombre = models.CharField(max_length=100)

    def  __str__(self) -> str:
        return self.nombre


class SubArea(BaseModel):
    nombre = models.CharField(max_length=100)

    def  __str__(self) -> str:
        return self.nombre


class Proveedor(BaseModel):
    nombre = models.CharField(max_length=100)

    def  __str__(self) -> str:
        return self.nombre


class TipoDeGasto(BaseModel):
    nombre = models.CharField(max_length=100)

    def  __str__(self) -> str:
        return self.nombre


class Presupuesto(BaseModel):
    presupuesto_id = models.CharField(max_length=100, unique=True)
    monto = models.FloatField()
    monto_original = models.FloatField()

    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)
    sub_area = models.ForeignKey(SubArea, null=True, on_delete=models.SET_NULL)
    proveedor = models.ForeignKey(Proveedor, null=True, on_delete=models.SET_NULL)
    tipo_de_gasto = models.ForeignKey(TipoDeGasto, null=True, on_delete=models.SET_NULL)

    cantidad = models.FloatField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField(null=True, blank=True)
    lleva_iva = models.BooleanField()
    iva = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    the_learning_gate = models.IntegerField(default=0)
    aula_virtual = models.IntegerField(default=0)
    live = models.IntegerField(default=0)
    en_linea = models.IntegerField(default=0)
    posgrados_presencial = models.IntegerField(default=0)
    posgrados_en_linea = models.IntegerField(default=0)

    total2 = models.IntegerField(null=True, blank=True)

    s1_0700399A03 = models.IntegerField(default=0)
    s1_0870399A06 = models.IntegerField(default=0)
    s1_0700399A31 = models.IntegerField(default=0)
    s1_0705103A00 = models.IntegerField(default=0)
    s1_0875103A00 = models.IntegerField(default=0)

    s2_0700399A03 = models.IntegerField(default=0)
    s2_0870399A06 = models.IntegerField(default=0)
    s2_0700399A31 = models.IntegerField(default=0)
    s2_0705103A00 = models.IntegerField(default=0)
    s2_0875103A00 = models.IntegerField(default=0)

    def  __str__(self) -> str:
        return f'{self.presupuesto_id}'

    def clean(self):
        if self.total2 != 100:
            raise ValidationError('Total2 (No mayor a 100%) es diferente a 100%')

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario

        if self.lleva_iva:
            self.iva = self.subtotal * 0.16
            self.total = self.subtotal * 1.16
        else:
            self.total = self.subtotal

        self.total2 = self.the_learning_gate + self.aula_virtual + self.live + self.en_linea + self.posgrados_presencial + self.posgrados_en_linea



        self.s1_0700399A03 = self.aula_virtual + self.live
        self.s1_0870399A06 = self.en_linea
        self.s1_0700399A31 = self.the_learning_gate
        self.s1_0705103A00 = self.posgrados_presencial
        self.s1_0875103A00 = self.posgrados_en_linea

        self.s2_0700399A03 = self.s1_0700399A03 * self.total
        self.s2_0870399A06 = self.s1_0870399A06 * self.total
        self.s2_0700399A31 = self.s1_0700399A31 * self.total
        self.s2_0705103A00 = self.s1_0705103A00 * self.total
        self.s2_0875103A00 = self.s1_0875103A00 * self.total
        
        self.clean()

        super().save(*args, **kwargs)


class Factura(BaseModel):
    pdf = models.FileField(upload_to='pdfs')
    cantidad = models.FloatField()
    precio_unitario = models.FloatField()
    descripcion = models.TextField()
    iva = models.BooleanField()
    subtotal = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)

    proveedor = models.ForeignKey(Proveedor, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.subtotal:
            self.subtotal = self.cantidad * self.precio_unitario
        if not self.total:
            self.total = self.subtotal if not self.iva else self.subtotal * 1.16
        super().save(*args, **kwargs)


    def  __str__(self) -> str:
        return f'{self.id}'
