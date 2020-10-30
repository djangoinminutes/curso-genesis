from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count, Avg, Q
import random
import datetime
from django import forms
import time
import os

# Reporte

from core.views import Reporte
from reportlab.lib.pagesizes import letter,landscape,portrait,A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm, cm
from reportlab.lib import colors


@importmodelos
@importforeign
@importforms

# Create your views here.
@modelospadre

@modeloshijo

@loadhijos

# General de Reportes
def Acomoda(datos,datos_reporte,primeralinea,titulo=False,datos_titulo=[]):

    numeroLineas = datos_reporte[0]
    pagina = datos_reporte[2]
    salto = datos_reporte[1]
    maxlineas = datos_reporte[3]

    nuevapagina = False
    if pagina == 1:
        # encabezado
        Encabezado(datos,pagina)
        salto = 0
        pagina += 1
    if numeroLineas >= maxlineas:
        nuevapagina = True
        numeroLineas = 0
        maxlineas = 50
        datos.append([0])
    if nuevapagina:
        # encabezado
        Encabezado(datos,pagina)
        salto = 0
        pass
    if titulo:
        numeroLineas += 1
        salto += 0.5    	
        datos.append([1,['Helvetica-Bold',9,colors.black],[datos_titulo[0][1],primeralinea-salto],datos_titulo[0][0],'c'])
        numeroLineas += 1
        salto += 0.4
        # Fecha
        if datos_titulo[1][0]:
            datos.append([3,['Helvetica',8,colors.red],[datos_titulo[1][1],primeralinea-salto],'c'])
            salto += 0.5
            numeroLineas += 1
        # Linea superior de columnas
        datos.append([4,[datos_titulo[2],primeralinea-salto,datos_titulo[3],primeralinea-salto,datos_titulo[4]]])    
        salto += 0.4
        # Columnas
        pos = 0
        for col in range(0,len(datos_titulo[5]),2):
            datos.append([1,['Helvetica-Bold',9,colors.black],[datos_titulo[5][col],primeralinea-salto],datos_titulo[5][col+1],'l'])
            pos+=2
        salto += 0.2
        # Linea inferior de columnas
        datos.append([4,[datos_titulo[2],primeralinea-salto,datos_titulo[3],primeralinea-salto,datos_titulo[4]]])    
        numeroLineas += 2
        salto += 0.5

    datos_reporte[0] =  numeroLineas
    datos_reporte[1] = salto 
    datos_reporte[2] = pagina 
    datos_reporte[3] = maxlineas 

def Encabezado(datos,pagina):

    anchologo=@anchologo
    altologo=@altologo
    posxlogo=@posxlogo
    posylogo=@posylogo
    posxnombre=@posxnombre
    posynombre=@posynombre
    iniciolineax=@iniciolineax
    finallineax=@finallineax
    iniciolineay=@iniciolineay
    grosorlinea=@grosorlineaencabezado
    piex=@piex
    piey=@piey
    lineapiex = @lineapiex
    lineapiey=@lineapiey
    nombre = '@nombre'

    logo = None
    try:
        cd = os.getcwd()
        logo = cd + '/core/static/core/img/logo.png'
    except:
        pass     

    datos.append([2,logo,[posxlogo,posylogo],[anchologo,altologo]])       
    datos.append([1,['Helvetica',20,colors.black],[posxnombre,posynombre],nombre,'c'])
    datos.append([4,[iniciolineax,iniciolineay,finallineax, iniciolineay,grosorlinea]])
    # Pie
    datos.append([1,['Helvetica',8,colors.black],[piex,piey],'Pag. ' + str(pagina),'c'])
    datos.append([4,[iniciolineax,lineapiey,lineapiex,lineapiey,grosorlinea]])    