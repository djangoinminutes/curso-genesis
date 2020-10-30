from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@importmodelos


#@[p_import_01]

class @modeloForm(forms.Form):

#@[p_form_01]
@campos

#@[p_form_02]

@widgets

#@[p_form_03]

    def clean(self):

#@[p_cleaned_data_01]
        cleaned_data = super(@modeloForm, self).clean()
#@[p_cleaned_data_02]
