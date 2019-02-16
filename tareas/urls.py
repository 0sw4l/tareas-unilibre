"""tareas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from manager.views import index, listas, ListaListView, items, ListaCreateView, ItemCreateView, borrar_lista, \
    borrar_item, ListaUpdateView, ItemUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('listas/', listas, name='listas'),
    path('items/', items, name='items'),
    path('crear_lista/', ListaCreateView.as_view(), name='crear_lista'),
    path('crear_item/', ItemCreateView.as_view(), name='crear_item'),
    path('eliminar_lista/<int:id>/', borrar_lista, name='eliminar_lista'),
    path('eliminar_item/<int:id>/', borrar_item, name='eliminar_item'),

    path('modificar_lista/<int:pk>/', ListaUpdateView.as_view(), name='modificar_lista'),
    path('modificar_item/<int:pk>/', ItemUpdateView.as_view(), name='modificar_item'),

]
