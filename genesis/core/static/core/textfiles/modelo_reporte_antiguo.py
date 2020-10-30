class Reporte@modelo():
    def __init__(self,archivo):
        self.canvas = canvas.Canvas(archivo,pagesize=@size)
        self.canvas.setPageSize( @orientacion(@size) )
        width, height = letter
        # self.canvas.setPageSize( (height, width) )
        self.estilos = getSampleStyleSheet()
        self.ancho, self.alto = @size

    def posicion(self, x, y, unidad=mm):
        x,y = x*unidad, self.alto - y*unidad
        return x,y

    def linea(self,x1,y1,x2,y2,unidad=mm):
        ''' Dibuja una linea '''
        self.canvas.line(x1*unidad, y1*unidad,x2*unidad, y2*unidad)
        pass

    def encabezado(self):
        ''' logo y nombre de empresa'''
        self.canvas.saveState()
        cd = os.getcwd()
        try:
            logo = cd + '/core/static/core/img/logo.png'
            # logo = @logo
            self.canvas.drawImage(logo,@logox*cm,@logoy*cm,1.5*cm,1.5*cm)
        except:
            pass
        # nombre = @proyecto
        self.canvas.setFont('Helvetica-Bold', 30)
        self.canvas.setFillColor(colors.black)
        self.canvas.drawCentredString(@nombrex*cm,@nombrey*cm, '@proyecto')
        self.linea(1, @lineaencabezadoy,@lineaencabezadox, @lineaencabezadoy,cm)
        self.canvas.restoreState()

    def pie(self,numero=1,unidad=mm):
        ''' Numero de pagina '''
        self.canvas.saveState()
        self.canvas.setFont('Helvetica', 8)
        self.canvas.setLineWidth(.1)
        self.linea(1, @lineapiey,@lineapiex, @lineapiey,cm)
        self.canvas.drawRightString(@pagenumberx*cm,@pagenumbery*cm,'Pag. ' + str(numero))
        self.canvas.restoreState()

    def columnas(self,titulo='@titulolista'):
        ''' despliega las columnas de datos '''
        self.canvas.saveState()
        self.canvas.setFont('Helvetica', 24)
        self.canvas.setFillColor(colors.black)
        self.canvas.drawCentredString(@titulox*cm,@tituloy*cm,titulo)
        self.canvas.setFont('Helvetica', 12)
        self.canvas.setFillColor(colors.red)
        self.canvas.drawCentredString(@fechax*cm,@fechay*cm,time.strftime("%d/%m/%y%y"))
        self.canvas.setLineWidth(.3)
        self.linea(1,@lineacolumnasy,@lineacolumnasx,@lineacolumnasy,cm)
        self.canvas.setFillColor(colors.black)
@columnas
        self.linea(1,@lineacolumnaiy,@lineacolumnaix,@lineacolumnaiy,cm)
        self.canvas.restoreState()
        
    def detalle(self):
        pagina = 1
        lista = []

        lista = @modelo.objects.all()
        numeroLineas = 0
        salto = 0
        primeralinea=@primeralineapp
        nuevapagina = False
        maxlineas = @numerolineaspp

        # lista1 = []
        # for i in range(100):
        #     for p in lista:
        #         lista1.append(p)

        for obj in lista:
            if pagina == 1:
                self.encabezado()
                self.columnas('@titulolista')
                pagina+=1
            if numeroLineas == maxlineas:
                nuevapagina=True
            if nuevapagina:
                self.canvas.showPage()
                self.encabezado()
                self.pie(pagina,mm)
                numeroLineas=0
                salto=0.5
                pagina+=1
                nuevapagina=False
                maxlineas=@numerolineassp
                primeralinea=@primeralineasp 
            self.canvas.setFont('Helvetica', 10)         
@campos 
            salto+=0.5
            numeroLineas+=1            

    def grabar(self):
        self.canvas.save()

