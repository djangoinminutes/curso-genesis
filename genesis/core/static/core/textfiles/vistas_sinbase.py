from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

#@[p_importmodelos_02]


from django.db.models import Sum, Count, Avg, Q
import random
import datetime

#@[p_importforms_02]

#@[p_modelosinbase_01]

# Create your views here.
class HomeView(TemplateView):
#@[p_home_01]
    template_name = '@aplicacion/home.html'
#@[p_home_02]

class @modeloView(FormView):
#@[p_@modeloview_01]
    template_name = '@aplicacion/@modelo.html'
    form_class = @modeloForm
#@[p_@modeloview_02]

    def get_success_url(self):
#@[p_@modelosuccess_01]
        return reverse_lazy('core:home')
#@[p_@modelosuccess_01]

    def post(self,request,*args,**kwargs):
#@[p_@modelopost_01]
        form = self.form_class(request.POST,request.FILES)
#@[p_@modelopost_02]
        if form.is_valid():
#@[p_@modelopost_03]
            cleaned_data = form.cleaned_data
#@[p_@modelopost_04]

        return render(request, '@aplicacion/@modelo.html', {'form': form@context})

#@[p_modelosinbase_02]
