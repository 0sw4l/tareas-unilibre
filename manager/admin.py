from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'descripcion',
        'fecha',
        'usuario',
        'estado'
    ]
    list_filter = [
        'estado',
        'usuario'
    ]
    search_fields = [
        'descripcion',
        'nombre'
    ]


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'descripcion',
        'fecha',
        'estado',
        'lista'
    ]
    list_filter = [
        'lista',
        'estado'
    ]

