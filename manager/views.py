from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView

from manager.forms import ListaForm, ItemForm
from . import models
# Create your views here.


def index(request):
    return render(request, 'home.html')


def listas(request):
    data = models.Lista.objects.filter(
        estado=True
    )
    context = {
        'listas': data
    }
    return render(request, 'listas.html', context)


def items(request):
    data = models.Item.objects.filter(
        estado=True
    )
    context = {
        'items': data
    }
    return render(request, 'items.html', context)


class FormMixin(CreateView):
    template_name = 'form.html'
    kind = ''
    action = 'Crear'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kind'] = self.kind
        context['action'] = self.action
        return context


class ListaCreateView(FormMixin):
    form_class = ListaForm
    model = models.Lista
    success_url = '/listas'
    kind = 'Lista'


class ItemCreateView(FormMixin):
    form_class = ItemForm
    model = models.Item
    success_url = '/items'
    kind = 'Item'


class ListaListView(ListView):
    context_object_name = 'listas'
    template_name = 'listas.html'
    model = models.Lista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('hola, soy la clase')
        return context


def borrar_lista(request, id):
    lista = models.Lista.objects.get(
        id=id
    )
    lista.estado = False
    lista.save()
    return redirect('listas')


def borrar_item(request, id):
    lista = models.Item.objects.get(
        id=id
    )
    lista.estado = False
    lista.save()
    return redirect('items')


class ListaUpdateView(ListaCreateView, UpdateView):
    action = 'Actualizar'


class ItemUpdateView(ItemCreateView, UpdateView):
    action = 'Actualizar'

