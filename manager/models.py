from django.db import models
# Create your models here.


class Lista(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    descripcion = models.TextField()
    fecha = models.DateTimeField(
        auto_now_add=True
    )
    usuario = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    estado = models.BooleanField(
        default=False
    )

    def __str__(self):
        return '{}] {} - {}'.format(
            self.id,
            self.nombre,
            self.usuario
        )


class Item(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    descripcion = models.TextField()
    fecha = models.DateTimeField(
        auto_now_add=True
    )
    estado = models.BooleanField(
        default=False
    )
    lista = models.ForeignKey(
        Lista,
        on_delete=models.CASCADE
    )


