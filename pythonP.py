
from tkinter import *
import math
import numpy as np
from tkinter.messagebox import *
matDatos = np.array
matResultados = np.array
perimetro = 0
sumaAnguloAjustado = 0
sumaProyNorte = 0
sumaProyEste = 0
sumaAjusteProyNorte=0
sumaAjusteProyEste=0
sumaProyNAjustada=0
sumaProyEAjustada=0
norte=0
este=0

def BtnIniciarPresinado():
    global matDatos
    global matResultados
    if(varNomTrab.get() == "" or varUbicacion.get() == "" or varNumDelta.get() == ""):
        showinfo("Error", "Ingrese Datos Completos")
    else:
        deltas = int(varNumDelta.get())
        matriz = [[0.0 for x in range(7)] for y in range(deltas)]
        matDatos = np.array(matriz)
        matriz2 = [[0.0 for x in range(14)] for y in range(deltas)]
        matResultados = np.array(matriz2)
        varContador.set("0")
"""
    matDatos[0][0] = int(1)
    matDatos[0][1] = int(2)
    matDatos[0][2] = int(144)
    matDatos[0][3] = int(29)
    matDatos[0][4] = int(12)
    matDatos[0][5] = (matDatos[0][2]) + ((matDatos[0][3]) / 60) + ((matDatos[0][4]) / 3600)
    matDatos[0][6] = float(48.511)
    matResultados[0][0] = int(matDatos[0][0])
    matResultados[0][1] = int(matDatos[0][1])
    matResultados[0][2] = float(matDatos[0][5])
    matResultados[0][4] = float(matDatos[0][6])

    matDatos[1][0] = int(2)
    matDatos[1][1] = int(3)
    matDatos[1][2] = int(260)
    matDatos[1][3] = int(41)
    matDatos[1][4] = int(55)
    matDatos[1][5] = (matDatos[1][2]) + ((matDatos[1][3]) / 60) + ((matDatos[1][4]) / 3600)
    matDatos[1][6] = float(48.177)
    matResultados[1][0] = int(matDatos[1][0])
    matResultados[1][1] = int(matDatos[1][1])
    matResultados[1][2] = float(matDatos[1][5])
    matResultados[1][4] = float(matDatos[1][6])

    matDatos[2][0] = int(3)
    matDatos[2][1] = int(4)
    matDatos[2][2] = int(214)
    matDatos[2][3] = int(45)
    matDatos[2][4] = int(10)
    matDatos[2][5] = (matDatos[2][2]) + ((matDatos[2][3]) / 60) + ((matDatos[2][4]) / 3600)
    matDatos[2][6] = float(52.181)
    matResultados[2][0] = int(matDatos[2][0])
    matResultados[2][1] = int(matDatos[2][1])
    matResultados[2][2] = float(matDatos[2][5])
    matResultados[2][4] = float(matDatos[2][6])

    matDatos[3][0] = int(4)
    matDatos[3][1] = int(5)
    matDatos[3][2] = int(278)
    matDatos[3][3] = int(10)
    matDatos[3][4] = int(30)
    matDatos[3][5] = (matDatos[3][2]) + ((matDatos[3][3]) / 60) + ((matDatos[3][4]) / 3600)
    matDatos[3][6] = float(80.475)
    matResultados[3][0] = int(matDatos[3][0])
    matResultados[3][1] = int(matDatos[3][1])
    matResultados[3][2] = float(matDatos[3][5])
    matResultados[3][4] = float(matDatos[3][6])

    matDatos[4][0] = int(5)
    matDatos[4][1] = int(1)
    matDatos[4][2] = int(269)
    matDatos[4][3] = int(51)
    matDatos[4][4] = int(47)
    matDatos[4][5] = (matDatos[4][2]) + ((matDatos[4][3]) / 60) + ((matDatos[4][4]) / 3600)
    matDatos[4][6] = float(60.165)
    matResultados[4][0] = int(matDatos[4][0])
    matResultados[4][1] = int(matDatos[4][1])
    matResultados[4][2] = float(matDatos[4][5])
    matResultados[4][4] = float(matDatos[4][6])

    decimales = 267 + (59) / 60 + ((10) / 3600)
    matResultados[0][2] = 360 - (decimales - matDatos[0][5])"""

def limpiarDatos():
    varPosDelta.set("")
    varFinDelta.set("")
    varGrados.set("")
    varMinutos.set("")
    varSegundos.set("")
    varDistancia.set("")

def BtnIngresarPresinado():
    global matDatos
    global matResultados
    if (varPosDelta.get() == "" or varFinDelta.get() == "" or varGrados.get() == "" or varMinutos.get() == "" or varSegundos.get() == "" or varDistancia.get() == ""):
        showinfo("Error", "Ingrese Datos Completos")
    else:
        contador = int(varContador.get())
        deltas = int(varNumDelta.get())
        if(contador < deltas):
            matDatos[contador][0] = int(varPosDelta.get())
            matDatos[contador][1] = int(varFinDelta.get())
            matDatos[contador][2] = int(varGrados.get())
            matDatos[contador][3] = int(varMinutos.get())
            matDatos[contador][4] = int(varSegundos.get())
            matDatos[contador][5] = (matDatos[contador][2]) + ((matDatos[contador][3]) / 60) + ((matDatos[contador][4]) / 3600)
            matDatos[contador][6] = float(varDistancia.get())

            matResultados[contador][0] = int(varPosDelta.get())
            matResultados[contador][1] = int(varFinDelta.get())
            matResultados[contador][2] = matDatos[contador][5]
            matResultados[contador][4] = float(varDistancia.get())

            varContador.set(str(contador+1))
            limpiarDatos()
            if(contador+1 == deltas):
                showinfo("OK", "Ingrese Datos Vistos desde el Primer Delta Hasta El Ultimo")
                varPosDelta.set(matDatos[0][0])
                varFinDelta.set(matDatos[deltas-1][0])
                varGrados.set("")
                varMinutos.set("")
                varSegundos.set("")
                varDistancia.set("XXXX")
        elif(contador == deltas):
            grados = int(varGrados.get())
            minutos = int(varMinutos.get())
            segundos = int(varSegundos.get())
            decimales = grados + (minutos) / 60 + ((segundos) / 3600)
            matResultados[0][2] = 360 - (decimales - matDatos[0][5])
            showinfo("OK", "Datos Completados Correctamente")
            limpiarDatos()
        else:
            showinfo("Error", "Datos Completos")
def BtnProcesarPresinado():
    global sumaProyNorte
    global sumaProyEste
    global sumaAjusteProyNorte
    global sumaAjusteProyEste
    global sumaProyNAjustada
    global sumaProyEAjustada
    global norte
    global este
    norte = float(varCoorNorte.get())
    este = float(varCoorEste.get())

    deltas = int(varNumDelta.get())
    cadena = "TRABAJO: "+ varNomTrab.get()+"   UBICACION LEVANTAMIENTO: "+varUbicacion.get()+"\n"
    cadena = cadena + "El Cierre angular es: " + str(sumaAngulosCorregidos()) + "\n"
    cadena = cadena + "Suma de Angulos es: " + str(sumaAngulos()) + "\n"
    errorGrados = sumaAngulos()-sumaAngulosCorregidos()
    cadena = cadena + "El error es: " + str(errorGrados) + "\n"
    errorSegundos = errorGrados*3600
    cadena = cadena + "El error en segundos es: " + str(errorSegundos) + "\n"
    ajuste = -1.0*errorSegundos/deltas
    cadena = cadena + "El ajuste es: "+ str(ajuste) + "\n"


    calcAjusteAngulos(ajuste)
    calcPerimetro()
    calcAzimut()
    calcAjusteProyeccion()

    cadena = cadena + "Suma de Proyeccion Norte es: " + str(sumaProyNorte) + "\n"
    cadena = cadena + "Suma de Proyeccion Este es: " + str(sumaProyEste) + "\n"
    cadena = cadena + "Suma del ajuste de Proyeccion Norte es : " + "{0:.4f}".format(sumaAjusteProyNorte) + "\n"
    cadena = cadena + "Suma del ajuste de Proyeccion Este es : " +"{0:.4f}".format(sumaAjusteProyEste) + "\n"
    cadena = cadena + "Suma de Proyeccion Norte Ajustada es: " + "{0:.4f}".format(sumaProyNAjustada) + "\n"
    cadena = cadena + "Suma de Proyeccion Este Ajustada es: " + "{0:.4f}".format(sumaProyEAjustada) + "\n"

    cadena = cadena + "Direccion Error es: " + "{0:.4f}".format(math.atan(sumaProyEste/sumaProyNorte)) + "\n"

    errorLineaTotal = math.sqrt((sumaProyNorte*sumaProyNorte)+(sumaProyEste*sumaProyEste))
    cadena = cadena + "Error Linea Total es: " + "{0:.4f}".format(errorLineaTotal) + "\n"

    sumaDistancias = 0
    for i in range(0, len(matDatos)):
        sumaDistancias += matResultados[i][4]
    precision =sumaDistancias /errorLineaTotal
    cadena = cadena + "Precision es: " + "{0:.4f}".format(precision) + "\n"


    varAreaTexto.set(cadena)
    print(matResultados)

    imprimirResultados()

def imprimirResultados():
    global matDatos
    global matResultados
    texto0 = ""
    texto1 = ""
    texto2 = ""
    texto3 = ""
    texto4 = ""
    texto5 = ""
    texto6 = ""
    texto7 = ""
    texto8 = ""
    texto9 = ""
    texto10 = ""
    texto11 = ""
    texto12 = ""
    texto13 = ""

    for i in range(0,len(matDatos)):
        texto0 = texto0 + str(int(matResultados[i][0])) + "\n"
        texto1 = texto1 + str(int(matResultados[i][1])) + "\n"
        texto2 = texto2 + "{0:.4f}".format(matResultados[i][2]) + "\n"
        texto3 = texto3 + "{0:.4f}".format(matResultados[i][3]) + "\n"
        texto4 = texto4 + "{0:.4f}".format(matResultados[i][4]) + "\n"
        texto5 = texto5 + "{0:.4f}".format(matResultados[i][5]) + "\n"
        texto6 = texto6 + "{0:.4f}".format(matResultados[i][6]) + "\n"
        texto7 = texto7 + "{0:.4f}".format(matResultados[i][7]) + "\n"
        texto8 = texto8 + "{0:.4f}".format(matResultados[i][8]) + "\n"
        texto9 = texto9 + "{0:.4f}".format(matResultados[i][9]) + "\n"
        texto10 = texto10 + "{0:.4f}".format(matResultados[i][10]) + "\n"
        texto11 = texto11 + "{0:.4f}".format(matResultados[i][11]) + "\n"
        texto12 = texto12 + "{0:.3f}".format(matResultados[i][12])+ "\n"
        texto13 = texto13 + "{0:.3f}".format(matResultados[i][13]) + "\n"

    varAreaTexto0.set(texto0)
    varAreaTexto1.set(texto1)
    varAreaTexto2.set(texto2)
    varAreaTexto3.set(texto3)
    varAreaTexto4.set(texto4)
    varAreaTexto5.set(texto5)
    varAreaTexto6.set(texto6)
    varAreaTexto7.set(texto7)
    varAreaTexto8.set(texto8)
    varAreaTexto9.set(texto9)
    varAreaTexto10.set(texto10)
    varAreaTexto11.set(texto11)
    varAreaTexto12.set(texto12)
    varAreaTexto13.set(texto13)

def sumaAngulosCorregidos():
    resp = varPoligonial.get()
    deltas = int(varNumDelta.get())
    if(resp == "si" or resp == "SI"):
        return(int(180*(deltas+2)))
    elif(resp == "no" or resp == "NO"):
        return(int(180*(deltas-2)))
    else:
        showinfo("Error", "Respuesta Incorrecta, debe ser si o no")

def sumaAngulos():
    global matDatos
    global matResultados
    resp = 0
    for i in range(0,len(matDatos)):
        resp = resp + matResultados[i][2]
    return resp
def calcAjusteAngulos(ajuste):
    global matDatos
    global matResultados
    global sumaAnguloAjustado
    for i in range(0, len(matDatos)):
        matResultados[i][3] = matResultados[i][2] + (ajuste / 3600.0)
        sumaAnguloAjustado += matResultados[i][3]

def calcPerimetro():
    global perimetro
    for i in range(0,len(matDatos)):
        perimetro += matResultados[i][4]

def calcAzimut():
    global sumaProyNorte
    global sumaProyEste
    global matDatos
    global matResultados
    for i in range(0, len(matDatos)):
        if i == 0:
            matResultados[i][5] = matDatos[i][5]
        if i > 0:
            azimut = matResultados[i - 1][5] + matResultados[i][3]
            if azimut > 180.0:
                azimut = azimut - 180
            else:
                azimut = azimut + 180
            if azimut > 360.0:
                azimut = azimut - 360.0
            matResultados[i][5] = azimut
        # calaculo de proyecciones
        proyNorte = matResultados[i][4] * (math.cos(math.pi * matResultados[i][5] / 180))
        matResultados[i][6] = proyNorte
        proyEste = matResultados[i][4] * (math.sin(math.pi * matResultados[i][5] / 180))
        matResultados[i][7] = proyEste
        sumaProyNorte += proyNorte
        sumaProyEste += proyEste

def calcAjusteProyeccion():
    global sumaAjusteProyNorte
    global sumaAjusteProyEste
    global perimetro
    global sumaProyNAjustada
    global sumaProyEAjustada
    global sumaProyNorte
    global sumaProyEste
    global norte
    global este

    for i in range(0, len(matDatos)):
        ajusteProyNorte = sumaProyNorte * (matResultados[i][4] / perimetro) * -1
        matResultados[i][8] = ajusteProyNorte

        ajusteProyEste = sumaProyEste * (matResultados[i][4] / perimetro) * -1
        matResultados[i][9] = ajusteProyEste

        sumaAjusteProyNorte += ajusteProyNorte
        sumaAjusteProyEste += ajusteProyEste
        suma = 0

        # proyeccion ajustada
        proyNAjustada = matResultados[i][6] + matResultados[i][8]
        sumaProyNAjustada += proyNAjustada
        matResultados[i][10] = proyNAjustada

        proyEAjustada = matResultados[i][7] + matResultados[i][9]
        sumaProyEAjustada += proyEAjustada
        matResultados[i][11] = proyEAjustada

        # coordenadas finales
        norte = norte + matResultados[i][10]
        matResultados[i][12] = norte
        este = este + matResultados[i][11]
        matResultados[i][13] = este


#***************************************************************************
#*****************************CREACION VENTANA******************************
#***************************************************************************
ventana=Tk()
ventana.title("Proyecto")
ventana.geometry("800x700")
ventana.resizable(width=False,height=False)



#***************************************************************************
#*********************Creacion Variables a Referenciar**********************
#***************************************************************************
varNomTrab = StringVar()
varUbicacion = StringVar()
varNumDelta = StringVar()
varPosDelta = StringVar()
varFinDelta = StringVar()
varGrados = StringVar()
varMinutos = StringVar()
varSegundos = StringVar()
varDistancia = StringVar()
varCoorNorte = StringVar()
varCoorEste = StringVar()
varPoligonial = StringVar()
varContador = StringVar()
varInformacion = StringVar()
varAreaTexto = StringVar()

varAreaTexto0 = StringVar()
varAreaTexto1 = StringVar()
varAreaTexto2 = StringVar()
varAreaTexto3 = StringVar()
varAreaTexto4 = StringVar()
varAreaTexto5 = StringVar()
varAreaTexto6 = StringVar()
varAreaTexto7 = StringVar()
varAreaTexto8 = StringVar()
varAreaTexto9 = StringVar()
varAreaTexto10 = StringVar()
varAreaTexto11 = StringVar()
varAreaTexto12 = StringVar()
varAreaTexto13 = StringVar()
#************************************************
#*****************Creacion Labels****************
#************************************************
label = Label(ventana,text="NOMBRE DEL TRABAJO",anchor="w",font='Helvetica 10 bold').place(x = 10, y = 5)
label = Label(ventana,text="UBICACION LEVANTAMIENTO",anchor="w",font='Helvetica 10 bold').place(x = 310, y = 5)
label = Label(ventana,text="NUMERO DELTAS",anchor="w",font='Helvetica 10 bold').place(x = 610, y = 5)

label = Label(ventana,text="Delta_Inicio",anchor="w",font='Helvetica 10 bold').place(x = 35, y = 100)
label = Label(ventana,text="Delta_Fin",anchor="w",font='Helvetica 10 bold').place(x = 170, y = 100)
label = Label(ventana,text="Grados",anchor="w",font='Helvetica 10 bold').place(x = 310, y = 100)
label = Label(ventana,text="Minutos",anchor="w",font='Helvetica 10 bold').place(x = 435, y = 100)
label = Label(ventana,text="Segundos",anchor="w",font='Helvetica 10 bold').place(x = 560, y = 100)
label = Label(ventana,text="Distancia",anchor="w",font='Helvetica 10 bold').place(x = 695, y = 100)

label = Label(ventana,text="Coordenada_Norte",anchor="w",font='Helvetica 10 bold').place(x = 70, y = 195)
label = Label(ventana,text="Coordenada_Este",anchor="w",font='Helvetica 10 bold').place(x = 340, y = 195)
label = Label(ventana,text="Poligonal Angulos Externos? SI/NO",anchor="w",font='Helvetica 10 bold').place(x = 560, y = 195)

label = Label(ventana,text="RESULTADOS",anchor="w",font='Helvetica 10 bold').place(x = 355, y = 290)
text = Label(ventana, height=15, width=50,bg="#FFFFFF",textvariable = varAreaTexto).place(x = 10, y = 450)
#***********************************************
label = Label(ventana,text="1",anchor="w",font='Helvetica 10 bold').place(x = 13, y = 315)
label = Label(ventana,text="2",anchor="w",font='Helvetica 10 bold').place(x = 43, y = 315)
label = Label(ventana,text="3",anchor="w",font='Helvetica 10 bold').place(x = 85, y = 315)
label = Label(ventana,text="4",anchor="w",font='Helvetica 10 bold').place(x = 145, y = 315)
label = Label(ventana,text="5",anchor="w",font='Helvetica 10 bold').place(x = 205, y = 315)
label = Label(ventana,text="6",anchor="w",font='Helvetica 10 bold').place(x = 265, y = 315)
label = Label(ventana,text="7",anchor="w",font='Helvetica 10 bold').place(x = 325, y = 315)
label = Label(ventana,text="8",anchor="w",font='Helvetica 10 bold').place(x = 385, y = 315)
label = Label(ventana,text="9",anchor="w",font='Helvetica 10 bold').place(x = 445, y = 315)
label = Label(ventana,text="10",anchor="w",font='Helvetica 10 bold').place(x = 505, y = 315)
label = Label(ventana,text="11",anchor="w",font='Helvetica 10 bold').place(x = 565, y = 315)
label = Label(ventana,text="12",anchor="w",font='Helvetica 10 bold').place(x = 625, y = 315)
label = Label(ventana,text="13",anchor="w",font='Helvetica 10 bold').place(x = 685, y = 315)
label = Label(ventana,text="14",anchor="w",font='Helvetica 10 bold').place(x = 745, y = 315)

label = Label(ventana,text="1: Posicion Origen",anchor="w",font='Helvetica 10 bold').place(x = 400, y = 450)
label = Label(ventana,text="2: Posicion Destino",anchor="w",font='Helvetica 10 bold').place(x = 400, y = 470)
label = Label(ventana,text="3: Horizontal",anchor="w",font='Helvetica 10 bold').place(x = 400, y = 490)
label = Label(ventana,text="4: Horizontal Corregido",anchor="w",font='Helvetica 10 bold').place(x = 400, y = 510)
label = Label(ventana,text="5: Distancia",anchor="w",font='Helvetica 10 bold').place(x = 400, y = 530)
label = Label(ventana,text="6: Azimut",anchor="w",font='Helvetica 10 bold').place(x = 400, y = 550)
label = Label(ventana,text="7: Proyeccion Norte",anchor="w",font='Helvetica 10 bold').place(x = 400, y = 570)
label = Label(ventana,text="8: Proyeccion Este",anchor="w",font='Helvetica 10 bold').place(x = 580, y = 450)
label = Label(ventana,text="9: Ajuste Proyeccion Norte",anchor="w",font='Helvetica 10 bold').place(x = 580, y = 470)
label = Label(ventana,text="10: Ajuste Proyeccion Este",anchor="w",font='Helvetica 10 bold').place(x = 580, y = 490)
label = Label(ventana,text="11: Proyeccion Norte Ajustada",anchor="w",font='Helvetica 10 bold').place(x = 580, y = 510)
label = Label(ventana,text="12: Proyeccion Este Ajustada",anchor="w",font='Helvetica 10 bold').place(x = 580, y = 530)
label = Label(ventana,text="13: Nortes",anchor="w",font='Helvetica 10 bold').place(x = 580, y = 550)
label = Label(ventana,text="14: Estes",anchor="w",font='Helvetica 10 bold').place(x = 580, y = 570)


text = Label(ventana, height=6, width=2,bg="#FFFFFF",textvariable = varAreaTexto0).place(x = 10, y = 350)
text = Label(ventana, height=6, width=2,bg="#FFFFFF",textvariable = varAreaTexto1).place(x = 40, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto2).place(x = 70, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto3).place(x = 130, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto4).place(x = 190, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto5).place(x = 250, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto6).place(x = 310, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto7).place(x = 370, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto8).place(x = 430, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto9).place(x = 490, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto10).place(x = 550, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto11).place(x = 610, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto12).place(x = 670, y = 350)
text = Label(ventana, height=6, width=7,bg="#FFFFFF",textvariable = varAreaTexto13).place(x = 730, y = 350)


label = Label(ventana,text="Dato Ingresado: ",anchor="w",font='Helvetica 10',textvariable = varInformacion).place(x = 450, y = 155)
label = Label(ventana,text="0",anchor="w",font='Helvetica 10 bold',textvariable = varContador).place(x = 550, y = 155)


#************************************************
#****************Creacion  Entrys****************
#************************************************
eNomTrab = Entry(ventana,width = 20,textvariable = varNomTrab).place(x = 20, y = 30)
eUbicacion = Entry(ventana,width = 20,textvariable = varUbicacion).place(x = 340, y = 30)
eNumDelta = Entry(ventana,width = 3,textvariable = varNumDelta).place(x = 655, y = 30)

ePosDelta = Entry(ventana,width = 8,textvariable = varPosDelta).place(x = 50, y = 125)
eFinDelta = Entry(ventana,width = 8,textvariable = varFinDelta).place(x = 180, y = 125)
eGrados = Entry(ventana,width = 8,textvariable = varGrados).place(x = 310, y = 125)
eMinutos = Entry(ventana,width = 8,textvariable = varMinutos).place(x = 440, y = 125)
eSegundos = Entry(ventana,width = 8,textvariable = varSegundos).place(x = 570, y = 125)
eDistancia = Entry(ventana,width = 8,textvariable = varDistancia).place(x = 700, y = 125)

eCoorNorte  = Entry(ventana,width = 8,textvariable = varCoorNorte).place(x = 100, y = 220)
eCoorEste  = Entry(ventana,width = 8,textvariable = varCoorEste).place(x = 370, y = 220)
ePoligonial  = Entry(ventana,width = 8,textvariable = varPoligonial).place(x = 640, y = 220)
#************************************************
#****************Creacion  Buttons***************
#************************************************
btnIniciar = Button(ventana, height = 1,width = 7,text="Iniciar",command=BtnIniciarPresinado).place(x = 370, y = 60)
btnIngresar = Button(ventana, height = 1,width = 7,text="Ingresar",command=BtnIngresarPresinado).place(x = 370, y = 155)
btnProcesar = Button(ventana, height = 1,width = 7,text="Procesar",command=BtnProcesarPresinado).place(x = 370, y = 250)

ventana.mainloop()


