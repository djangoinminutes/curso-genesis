from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BusquedaForm(forms.Form):
	texto = forms.CharField(max_length=50)
