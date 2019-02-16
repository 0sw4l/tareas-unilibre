from django import forms
from . import models


class ListaForm(forms.ModelForm):
    class Meta:
        model = models.Lista
        fields = '__all__'


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'

