from django.shortcuts import render
from django.views.generic.base import TemplateView

from reportlab.lib.pagesizes import letter,landscape,portrait,A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm, cm
from reportlab.lib import colors

import os
import time

#@[p_core_view_01]

class CorePageView(TemplateView):
    template_name = "core/home.html"
#@[p_core_view_02]

    def get_context_data(self, **kwargs):
        context = super(CorePageView, self).get_context_data(**kwargs)
#@[p_core_view_03]
        return context       

#@[p_core_view_04]

class Reporte():

    def __init__(self,archivo,pagina,orientacion,datos_detalle,cols=[]):
        self.canvas = canvas.Canvas(archivo,pagesize=pagina)
        if orientacion == 'portrait':
            self.canvas.setPageSize( portrait(pagina) )
        else:
            self.canvas.setPageSize( landscape(pagina) )
        width, height = pagina
        self.estilos = getSampleStyleSheet()
        self.ancho, self.alto = pagina

        self.datos_detalle = datos_detalle
        self.cols = cols

    def posicion(self, x, y, unidad=mm):
        x,y = x*unidad, self.alto - y*unidad
        return x,y

    def linea(self,x1,y1,x2,y2,unidad=mm):
        ''' Dibuja una linea '''
        self.canvas.line(x1*unidad, y1*unidad,x2*unidad, y2*unidad)
        pass

    def logo(self,datos):

        logo = datos[1]
        posx = float(datos[2][0])
        posy = float(datos[2][1])
        width = int(datos[3][0])
        height = int(datos[3][1])

        ''' logo y nombre de empresa'''
        self.canvas.saveState()
        self.canvas.drawImage(logo,posx*cm,posy*cm,width*cm,height*cm)
        self.canvas.restoreState()        

    def imagen(self,datos):

        img = datos[1]
        posx = float(datos[2][0])
        posy = float(datos[2][1])
        width = float(datos[3][0])
        height = float(datos[3][1])

        ''' logo y nombre de empresa'''
        self.canvas.saveState()
        self.canvas.drawImage(img,posx*cm,posy*cm,width*cm,height*cm)
        self.canvas.restoreState()       

    def texto(self,datos):

        font = ([datos[1][0],datos[1][1]])
        color = datos[1][2]
        nombre = datos[3]
        posxn = float(datos[2][0])
        posyn = float(datos[2][1])
        align = datos[4]

        self.canvas.saveState()
        self.canvas.setFont(font[0], int(font[1]))
        self.canvas.setFillColor(color)
        if align =='c':
            self.canvas.drawCentredString(posxn*cm,posyn*cm, nombre)
        elif align =='r':
            self.canvas.drawRightString(posxn*cm,posyn*cm, nombre)
        else:
            self.canvas.drawString(posxn*cm,posyn*cm, nombre)
        self.canvas.restoreState()

    def fecha(self,datos):
        font = ([datos[1][0],datos[1][1]])        
        color = datos[1][2]        
        posx = float(datos[2][0])        
        posy = float(datos[2][1])        
        align = datos[3]

        self.canvas.saveState()
        self.canvas.setFont(font[0], int(font[1]))
        self.canvas.setFillColor(color)
        if align =='c':
            self.canvas.drawCentredString(posx*cm,posy*cm,time.strftime("%d/%m/%y%y"))
        else:
            self.canvas.drawString(posx*cm,posy*cm,time.strftime("%d/%m/%y%y"))
        self.canvas.restoreState()

    def datos(self,datos):

        posxn = float(datos[1][0])
        posyn = float(datos[1][1])
        dato = datos[2]
        font = ([datos[3],datos[4]])
        print('font',font)
        self.canvas.saveState()
        self.canvas.setFont(font[0], int(font[1]))
        self.canvas.drawString(posxn*cm,posyn*cm, dato)
        self.canvas.restoreState()

    def encabezado(self,datos_encabezado):

        logo = datos_encabezado[1]
        posx = float(datos_encabezado[2][0])
        posy = float(datos_encabezado[2][1])
        width = int(datos_encabezado[3][0])
        height = int(datos_encabezado[3][1])
        font = ([datos_encabezado[4][0],datos_encabezado[4][1]])
        color = datos_encabezado[4][2]
        nombre = datos_encabezado[4][3]
        posxn = float(datos_encabezado[5][0])
        posyn = float(datos_encabezado[5][1])
        posxli = float(datos_encabezado[6][0])
        posyli = float(datos_encabezado[6][1])
        posxlf = float(datos_encabezado[6][2])
        posylf = float(datos_encabezado[6][3])

        ''' logo y nombre de empresa'''
        self.canvas.saveState()
        cd = os.getcwd()
        try:
            logo = cd + '/core/static/core/img/logo.png'
            self.canvas.drawImage(logo,posx*cm,posy*cm,width*cm,height*cm)
        except:
            pass

        self.canvas.setFont(font[0], int(font[1]))
        self.canvas.setFillColor(color)
        self.canvas.drawCentredString(posxn*cm,posyn*cm, nombre)
        self.linea(posxli, posyli,posxlf, posylf,cm)
        self.canvas.restoreState()

    def pie(self,datos_pie,unidad=mm):

        font = ([datos_pie[1][0],datos_pie[1][1]])
        posxli = float(datos_pie[2][0])
        posyli = float(datos_pie[2][1])
        posxlf = float(datos_pie[2][2])
        posylf = float(datos_pie[2][3])
        posxn = float(datos_pie[3][0])
        posyn = float(datos_pie[3][1])
        numero = int(datos_pie[4])
        self.canvas.saveState()
        self.canvas.setFont(font[0], int(font[1]))
        self.canvas.setLineWidth(.1)
        self.linea(posxli, posyli,posxlf, posylf,cm)
        self.canvas.drawRightString(posxn*cm,posyn*cm,'Pag. ' + str(numero))
        self.canvas.restoreState()

    def titulo(self,datos_titulo):
        font = ([datos_titulo[1][0],datos_titulo[1][1]])        
        color = datos_titulo[1][2]        
        posx = float(datos_titulo[2][0])        
        posy = float(datos_titulo[2][1])        
        titulo = datos_titulo[3][0]

        self.canvas.saveState()
        self.canvas.setFont(font[0], int(font[1]))
        self.canvas.setFillColor(color)
        self.canvas.drawCentredString(posx*cm,posy*cm,titulo)
        self.canvas.restoreState()


    def columnas(self,datos_columnas):

        font = ([datos_columnas[1][0],datos_columnas[1][1]])
        color = datos_columnas[1][2]
        cols=[]        
        for i in range(2,len(datos_columnas)):
            cols.append(datos_columnas[i])        

        self.canvas.saveState()
        self.canvas.setFont(font[0],font[1])
        self.canvas.setFillColor(color)
        for col in cols:
            posx = float(col[0])
            posy = float(col[1])
            nombre = col[2]
            
            self.canvas.drawString(posx*cm,posy*cm,nombre)

        self.canvas.restoreState()

    def lineas(self,datos):

        self.canvas.saveState()

        x1 = float(datos[1][0])
        y1 = float(datos[1][1])
        x2 = float(datos[1][2])
        y2 = float(datos[1][3])
        grosor = float(datos[1][4])

        self.canvas.setLineWidth(grosor)
        self.linea(x1,y1,x2,y2,cm)

        self.canvas.restoreState()

    def detalle(self):

        for obj in self.datos_detalle:
            if obj[0] == 0:
                self.canvas.showPage()
            if obj[0] == 1:
                self.texto(obj)
            if obj[0] == 2:
                self.logo(obj)
            if obj[0] == 8:
                self.imagen(obj)
            if obj[0] == 4:
                self.lineas(obj)
            if obj[0] == 5:
                self.datos(obj)
            if obj[0] == 7:
                self.lineas(obj)
            if obj[0] == 3:
                self.fecha(obj)
            if obj[0] == 6:
                posx= obj[0]
                posy= obj[1]
                self.canvas.drawString(posx*cm,posy*cm,str(obj[2]))
    
    def grabar(self):
        self.canvas.save()