# forms.py
from django import forms
from .models import Add_WarehouseItem

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Add_WarehouseItemForm(forms.ModelForm):
    class Meta:
        model = Add_WarehouseItem
        fields = ['name', 'quantity', 'Price', 'description']





