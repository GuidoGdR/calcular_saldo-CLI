#!/bin/python3

from datetime import datetime
from distutils.log import info
import time
import os
import csv


def limpiarpantalla():
    if os.name=="nt" or os.name=="dos":
        comando="cls"
        os.system(comando)

    elif os.name=="posix":
        comando="clear"
        os.system(comando)

def mostrarmenu():

    print("\t\tBienvenido\n")
    print("Por favor elija una opcion:\n")
    print("1-Calcular el saldo que se tendra en una fecha x")
    print("2-Agregar un monto a la ficha de activos")
    print("3-Agregar un monto a la ficha de pasivos")
    print('4-Copiar info. de "Liquidacion diaria" en "Ficha de activos"')
    print("9-Salir\n")

def Delistastr(lista, caracter):                    
    return caracter.join(map(str, lista))

def Escribirbasededatos(texto):                 #Escribe en la base de datos lo que le pasas en lugar de "texto"
    try:
        if os.name == "nt" or os.name=="dos":
            chequeoos='\\'
            
        elif os.name =="posix":
            chequeoos='/'

        with open(f"config{chequeoos}database.csv", "a", newline="")as archivoacsv:
            escritor=csv.writer(archivoacsv, delimiter=";")
            escritor.writerows(texto)

    except FileNotFoundError:
        print(f"\tError!!\nError de tipo:FileNotFoundError\nEl programa no detecta la carpeta config.\nDe no existir la carpeta config dentro de la carpeta raiz del programa por favor: Crearla y reiniciar el programa \n--------------------------------------")
        input("Presione ENTER para continuar\n")


    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        archivoacsv.close()

def Infodatabase():                                 #retorna una lista con listas de la info de la base de datos
    try:
        if os.name == "nt" or os.name=="dos":
            chequeoos='\\'
            
        elif os.name =="posix":
            chequeoos='/'

        onoffdatabase_close=1
        with open(f"config{chequeoos}database.csv", "r") as infodatabase:
            lector=csv.reader(infodatabase, delimiter=";")
            datoscopiados=[]

            for linea in lector:
                datoscopiados+=[linea]
            return datoscopiados

    except FileNotFoundError:
        onoffdatabase_close=0
        print('\tError!!\nError de tipo:FileNotFoundError\nNo se a encontrado el archivo "database.csv" necesario para la correcta ejecución de el programa')
        input("Presione ENTER para continuar\n")


    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        if onoffdatabase_close == 1:
            infodatabase.close()

        else:
            pass

def CalcularActivosfuturos(añoinput, mesinput, diainput):#se puede dividir o usar una funcion para acortar codigo (revsisar) #en base a la ficha de pasivos suma los pasivos anteriores a una fecha x 
    try:                                          #y posteriores a la fecha actual
        if os.name == "nt" or os.name=="dos":
            chequeoos='\\'
            
        elif os.name =="posix":
            chequeoos='/'
            
        fechaactual=datetime.now()
        diaactual=int(datetime.strftime(fechaactual,"%d"))
        mesactual=int(datetime.strftime(fechaactual,"%m"))
        añoactual=int(datetime.strftime(fechaactual,"%Y"))
        montoscopiados=0.0
        with open(f"config{chequeoos}database.csv", "r") as archivoP:
            lector=csv.reader(archivoP, delimiter=";")
            for linea in lector:
                añoleido=int(linea[0])
                mesleido=int(linea[1])
                dialeido=int(linea[2])
                montoleido=float(linea[3])

                if añoleido == añoactual:           #chequeo si la fecha en el archivo es de una fecha posterior a hoy (marcas "actual")

                    if mesleido == mesactual:                       #acutal

                        if dialeido >= diaactual:                   #actual

                            if añoleido == añoinput :
                                if mesleido == mesinput:
                                    if dialeido <= diainput:
                                        montoscopiados+=montoleido
                                elif mesleido < mesinput:
                                    montoscopiados+=montoleido
                            elif añoleido < añoinput:
                                montoscopiados+=montoleido



                    elif mesleido > mesactual:                      #actual

                        if añoleido == añoinput :
                            if mesleido == mesinput:
                                if dialeido <= diainput:
                                    montoscopiados+=montoleido
                            elif mesleido < mesinput:
                                montoscopiados+=montoleido
                        elif añoleido < añoinput:
                            montoscopiados+=montoleido

                elif añoleido > añoactual:                          #actual

                    if añoleido == añoinput :
                        if mesleido == mesinput:
                            if dialeido <= diainput:
                                montoscopiados+=montoleido
                        elif mesleido < mesinput:
                            montoscopiados+=montoleido
                    elif añoleido < añoinput:
                        montoscopiados+=montoleido

            return montoscopiados

    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        archivoP.close()

def CopiarLiquidaciones():                                #Retorna una lista con sublistas de año-mes-dia-monto-numerodeliquidacion
    try:
        if os.name == "nt" or os.name=="dos":
            chequeoos='\\'
            
        elif os.name =="posix":
            chequeoos='/'

        with open(f"config{chequeoos}Liquidación diaria.csv", "r") as archivoL:
            next(archivoL, None) #Evito la primera linea por ser encabezado
            lector=csv.reader(archivoL, delimiter=";")
            liquidacionescopiadas=[]
            
            for linea in lector:
                listadia=list(linea[0])
                listadia.pop()
                listadia.pop()
                listadia.pop()
                listadia.pop()
                listadia.pop()
                listadia.pop()
                listadia.pop()
                listadia.pop()
                diacopiado=Delistastr(listadia, "")
                
                listames=list(linea[0])         #Fechas
                listames.pop()
                listames.pop()
                listames.pop()
                listames.pop()
                listames.pop()
                listames.reverse()
                listames.pop()
                listames.pop()
                listames.pop()
                listames.reverse()
                mescopiado=Delistastr(listames,"")

                listaaño=list(linea[0])         #Fechas
                listaaño.reverse()
                listaaño.pop()
                listaaño.pop()
                listaaño.pop()
                listaaño.pop()
                listaaño.pop()
                listaaño.pop()
                listaaño.reverse()
                añocopiado=Delistastr(listaaño,"")

                listamonto=list(linea[9])
                if "." in linea[9]:             #Monto
                    listamonto.remove(".")
        
                    indice=listamonto.index(",")
                    listamonto.pop(indice)
                    listamonto.insert(indice,".")

                montocopiado=Delistastr(listamonto,"")
                
                numerodeliquidacion=str(linea[2])       #Numero de Liquidacion

                liquidacionescopiadas+=[[añocopiado, mescopiado, diacopiado, montocopiado, numerodeliquidacion]]

            return liquidacionescopiadas
    except FileNotFoundError as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\nEl arcivo 'Liquidación diaria.csv' no fue encontrado")
        print("Depositar el archivo 'Liquidación diaria.csv' dentro de la carpeta 'config' del programa")
        print (e)
        print("--------------------------------------")
        input("Presione ENTER para continuar\n")

    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        archivoL.close()

def Chequeoduplicados(listachica, listagrande): #Chequea si hay duplicados, de haberlos retorna cuales son sus num de indice en lista chica

    """
     _summary_
    
    por cada lindea de 'lista chica' chequea que no haya coinsidencias con 'lista grande'
    
    
    Args:
    listachica([[STR],[STR]]):Listas con strings
    
    listagrande([STR]): Lista de strings o un string solo dentro de una lista
    
    Returns:
        indicesderepetidos([INT]): Un entero que indica el indice(en 'listachica') del str repetido
        resultado1(False):Resultado por defecto que devuelve al no detectar duplicados
    
    """
    
    
    
    resultado1= False
    numerodeserierepe=[]
    indicesderepetidos=[]

    for linea in listachica:
        if linea in listagrande:
            numerodeserierepe+=[linea]

    if numerodeserierepe != []:
        for numero in numerodeserierepe:
            indicesderepetidos+=[listachica.index(numero)]
        indicesderepetidos.reverse()
        return indicesderepetidos

    else:
        return resultado1

def Solonumserie(listaenlista):            #retorna solo el numero de serie (le espesificamos la posicion en la que está) 
    solonumserieR=[]

    for linea in listaenlista:
        solonumserieR+=[linea[4]]           #establecemos que el numero de serie o numero unico está en la posicion 
    return solonumserieR

def Chequeoduplicados2(numliquidacion, listasdelistas):     #un contador que mide cuantas veces aparece un str en una lista de listas (revisar si funciona con listas sin estar dentro de listas)
    contador=0
    for lista in listasdelistas:
        if numliquidacion in lista:
            contador+=1
    return contador

def chequeodatabase():
    """
    _summary_
    Intenta abrir el archivo database.csv y de no poder ofrece crearlo.
    funciona en windows y linux
    pendiente:
    *el programa no crea la carpeta config, la cual debe tener dentro el archivo database.csv, se podria crear una utilidad con
    os para crear la carpeta y no tener que pedirle al usuario que la cree
    """
    try:
        if os.name == "nt" or os.name=="dos":
            chequeoos='\\'
            
        elif os.name =="posix":
            chequeoos='/'
            
        onoffdatabase_close=1
        with open(f"config{chequeoos}database.csv", "r") as infodatabase:
            pass

    except FileNotFoundError:
        onoffdatabase_close=0
        print('No se a encontrado el archivo "database.csv" necesario para el correcto funcionamiento')
        print("1- Crear archivo vacío\n2- Continuar")
        opcion=str(input("Elija una de las opciones:"))
        if opcion == "1" or opcion == "1-":
            try:
                with open(f"config{chequeoos}database.csv", "w") as infodatabase:
                    pass

            
            except FileNotFoundError as e:
                print(f"\tError!!\nError de tipo:{type(e).__name__}\nCrear la carpeta 'config' antes de reiniciar\n--------------------------------------")
                input("Presione ENTER para continuar\n")
            except Exception as e:
                print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
                input("Presione ENTER para continuar\n")

            finally:
                infodatabase.close()
                limpiarpantalla()

        else:
            limpiarpantalla()
            pass

    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        if onoffdatabase_close == 1:
            infodatabase.close()
        else:
            pass

def fecha_actualvsingresada():
    """
    _summary_
    solicita una fecha al usuario y la devuelve luego de controlar que sea futura a la fecha actual
    no admite: 0, meses mayores a 12 ni dias mayores a 33
    
    pendiente:
    *mejorar el limite de dias segun el mes del año selecciojado
    *agregar boton de cancelar

    Returns:
        lista con enteros:[año, mes, dia]
    """

    fechasolicitada=[]

    seguridadfechaposterior=0
    
    traba=1
#----------------------------------------------------------------------------------------Año
    while traba == 1:
        
        try:
            entrada=input ('Digite el año:') 
            añosolicitado=int(entrada)

            if añosolicitado >= año_actual:
              
                fechasolicitada+=[añosolicitado]
                
                if añosolicitado > año_actual:
                    seguridadfechaposterior=1
                traba=2
            else:
                print ("El año podria ser menor al que indica el sistema como actual, se requiere verificar los datos")

        except ValueError:
            print (f"Digite el año en formato numerico \nEj:{año_actual}")
            
        except Exception as e:
            print (f"   \tError!!\nError de tipo:{type(e).__name__}")
          
        finally:
            pass

#----------------------------------------------------------------------------------------Mes
    while traba == 2:
        try:
            entrada=input ('Digite el mes:') 
            messolicitado=int(entrada)

            if messolicitado >= mes_actual and messolicitado <= 12 or seguridadfechaposterior == 1 and messolicitado > 0 and messolicitado < 13:
                fechasolicitada+=[messolicitado]
            
                if messolicitado > mes_actual and seguridadfechaposterior == 0:
                    seguridadfechaposterior=1
                traba=3
        
            elif messolicitado == 0:
                print ("El mes no puede tener valor de 0")
                
            elif messolicitado > 12:
                print ("El mes no puede tener un valor mayor a 12")
            
            elif messolicitado < 0:
                print ("El mes solicitado no puede ser negativo") 
            else:
                print ("El mes podria ser menor al que indica el sistema como actual, se requiere verificar los datos")

        except ValueError:
            print (f"Digite el mes en formato numerico \nEj:{mes_actual}")
            
        except Exception as e:
            print (f"   \tError!!\nError de tipo:{type(e).__name__}")

#----------------------------------------------------------------------------------------Dia
    while traba == 3:
        
        try:
            entrada=input ('Digite el dia:') 
            diasolicitado=int(entrada)

            if diasolicitado >= dia_actual and diasolicitado < 33 or seguridadfechaposterior == 1 and diasolicitado > 0 and diasolicitado < 33:
                fechasolicitada+=[diasolicitado]
                return fechasolicitada
        
            elif diasolicitado == 0:
                print ("El dia no puede tener valor de 0")
            
            elif diasolicitado > 33:
                print("El dia no puede tener un valor mayor a 33")
                
            elif diasolicitado <0:
                print("El dia solicitado no puede ser negativo")
            
            else:
                print ("El dia podria ser menor al que indica el sistema como actual, se requiere verificar los datos")

        except ValueError:
            print (f"Digite el dia en formato numerico \nEj:{dia_actual}")
            
        except Exception as e:
            print (f"   \tError!!\nError de tipo:{type(e).__name__}")

def SolicitarNuevoA ():
    """
    _summary_
    Solicita un monto y controla que no sea menor que 0.01, un num. negativo o un str
    
    Returns:
        Float: Monto/saledo/$$$ par el Activo
    """

    while 1 == 1:
        try:
            montosolicitado=float(input("Digite el monto:"))
            if montosolicitado == 0:
                print ("El monto solicitado no puede ser 0")

            elif montosolicitado <= 0.009:
                print ("El monto solicitado no puede ser menor que 0.01")

            else:
                return montosolicitado
        
        except ValueError as e:
            print ("El programa no admite letras, ingrese el monto en numeros")
            pass
        
        except Exception as e:
            print (f"Error tipo:{type(e).__name__} \n", e)


def SolicitarNumLiquidacion():
    
    """
    _summary_
    Solicita un numero de liquidacion y controla que no sea 0, menor que 0 o que tenga letras

    Returns:
        _type_STR: _description_El numero de liquidacion solicitado(Ej:5871)
    """
    
    while 1 == 1:
        try:
            
            numerodeliquidacionsolicitado=int(input("Digite el numero de liquidacion:"))

        
            if numerodeliquidacionsolicitado <= 0:
                print("El numero de liquidacion no puede ser menor o igual a 0")
            
            else:
                numerodeliquidacionsolicitado=str(numerodeliquidacionsolicitado)
                return numerodeliquidacionsolicitado

        except ValueError as e:
            print(f'\tError!!\nEl numero de liquidacion no admite letras')

        except Exception:
            print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
            input("Presione ENTER para continuar\n")

def DepuradordeDuplicado(duplicados1, duplicados2, datoaescribir, datosexistentes):
    """
    DepuradordeDuplicado _summary_
    
    Chequea el informe de si hay duplicados y de haberlos da la opcion de:
    Cancelar la operacion
    Omitir nuevos duplicados
    Eliminar los registros ya existentes para evitar duplicados1

    duplicados1/duplicados2:
    Resultado de funcion 'Chequeoduplicados1(a, b)', informe sobre si hay duplicados
    
    Args:
        duplicados1 ([INT]/False): False/ Numero de index de los duplicados de los datos todavia no ingresados a la DB 
        duplicados2 ([INT]/False): False/ Numero de index de los duplicados en la DB 
        datoaescribir ([STR,STR,STR,STR,STR]): Lista con el registro a escribir indicando [año, mes, dia, monto, num de liquidacion(ID)] 
        datosexistentes ([[str,..][str,..]]): Lista con listas que contienen los registros originales
    """

    if duplicados1 == False and duplicados2 == False:
        Escribirbasededatos(datoaescribir)
    
    elif duplicados1 == False and duplicados2 != False or duplicados2 == False and duplicados1 != False:
        print ("Error al intentar chequear la existencia de duplicados")
        print ("la carga de datos se cancelara para intentar conservar la integridad de la base de datos")
        input ("Presione ENTER para continuar:")
    
    else:
        traba1=1
        print("Se encontraron numeros de liquidacion duplicados con respecto a la base de datos.")
        print("1-Omitir los NUEVOS importes duplicados\n2-Eliminar los importes duplicados EXISTENTES\n0-Para CANCELAR")
        print("H-Texto un poco mas extenso descriptivo de opciones")
        respuesta=str(input("1/2/0:"))
        print("\n\n")
        
        while traba1 == 1:
            
            if respuesta == "1":
                for i  in duplicados1:
                    datoaescribir.pop(i)
                Escribirbasededatos(datoaescribir)
                traba1=0
            
            elif respuesta == "2":
                for i  in duplicados2:
                    datosexistentes.pop(i)
                datosexistentes+=datoaescribir    
                
                Escribirbasededatos(datoaescribir)
                traba1=0
            
            elif respuesta == "0":                    
                onoffdeconfirmacion=0
                traba1=0
            
            elif respuesta == "H" or respuesta == "h":
                print("1-Elimina el/los registros nuevos que se detectar")
                
            else:
                print(f'\nOpcion"{respuesta}" no encontrada, cancelando carga.\n')

    if onoffdeconfirmacion == 1:
        print(f'Se a pegado la informacion en la base de datos correctamente')
        input("Presione ENTER para continuar\n")
        limpiarpantalla()
        
    else:
        print ("Se a Cancelado la carga de liquidacion en la base de datos.")
        input("Presione ENTER para continuar\n")
        limpiarpantalla()







print("//////////////////////////////////")
print("//\tSoftware de uso libre\t//")
print("//author:GdR\t\t\t   //")
print("//guidodorego@gmail.com\t\t   //")
print("/////////////////////////////////////")
print("//iconos de:https://www.flaticon.es//")
print("/////////////////////////////////////")
#time.sleep(1)
limpiarpantalla()

onoff=1

fecha_actual=datetime.now()
dia_actual=int(datetime.strftime(fecha_actual,"%d"))
mes_actual=int(datetime.strftime(fecha_actual,"%m"))
año_actual=int(datetime.strftime(fecha_actual,"%Y"))



chequeodatabase()

while onoff==1:
    mostrarmenu()
    cursor=str(input("Elija una de las opciones:"))

    if cursor=="1" or cursor=="1-":   #Calcular el saldo que se tendra en una fecha x
        limpiarpantalla()
        print("1-Calcular el saldo que se tendra en una fecha x\n\n")

        fechaenlista=fecha_actualvsingresada()
        
        añosolicitado=fechaenlista[0]
        messolicitado=fechaenlista[1]
        diasolicitado=fechaenlista[2]
        
        
        activofuturo=CalcularActivosfuturos(añosolicitado, messolicitado, diasolicitado)

        print("Segun la base de datos:\n\n")
        print(f"En la fecha:{diasolicitado}/{messolicitado}/{añosolicitado}")
        print("-------------------------------------")
        print(f"El monto total de la cuenta será de:${activofuturo:.2f}")
        input("Presione ENTER para continuar\n")
        limpiarpantalla()

    elif cursor=="2" or cursor=="2-": #Agregar un monto a la ficha de activos
        limpiarpantalla()
        print("2-Agregar un monto a la ficha de activos\n\n")

        fechaenlista=fecha_actualvsingresada()
        
        añosolicitado=fechaenlista[0]
        messolicitado=fechaenlista[1]
        diasolicitado=fechaenlista[2]

        montosolicitado=SolicitarNuevoA()
        
        numerodeliquidacionsolicitado=SolicitarNumLiquidacion()
        
        tablap=[numerodeliquidacionsolicitado]

        infodatabase=Infodatabase()
        solonumliquidacionDB=Solonumserie(infodatabase)
        
        
        print (solonumliquidacionDB)
        print (tablap)
        
        duplicados=Chequeoduplicados(solonumliquidacionDB, tablap)

        print("//////////////////////////////")
        
        print (duplicados)
        input("AA")

        if duplicados == False:
            pass
            datos_a_pegar=[[añosolicitado, messolicitado, diasolicitado, montosolicitado, numerodeliquidacionsolicitado]]
            Escribirbasededatos(datos_a_pegar)  
            print(f'Se a pegado "{datos_a_pegar}" correctamente')
            input("Presione ENTER para continuar\n")
            limpiarpantalla()
        
        else:
            
            pass




    elif cursor=="3" or cursor=="3-": #Agregar un monto a la ficha de pasivos
        limpiarpantalla()
        print("3-Agregar un monto a la ficha de pasivos\n\n")

        añosolicitado=int(input("Digite el año:"))
        messolicitado=int(input("Digite el mes:"))
        diasolicitado=int(input("Digite el dia:"))
        montosolicitado=-1*float(input("Digite el monto:"))
        numerodeliquidacionsolicitado=str(input("Digite el numero de liquidacion:"))

        datos_a_pegar=[[añosolicitado, messolicitado, diasolicitado, montosolicitado, numerodeliquidacionsolicitado]]

        Escribirbasededatos(datos_a_pegar)

        print(f'Se a pegado "{datos_a_pegar}" correctamente')
        input("Presione ENTER para continuar\n")
        limpiarpantalla()

    elif cursor=="4" or cursor=="4-": #Copiar info. de "Liquidacion diaria" en "Ficha de activos"
        onoffdeconfirmacion=1

        liquidacionescopiadas=CopiarLiquidaciones()
        infodatabasecopiada=Infodatabase()
        Solonumserie(liquidacionescopiadas)
        Solonumserie(infodatabasecopiada)

        duplicados=Chequeoduplicados(liquidacionescopiadas, infodatabasecopiada)
        print(duplicados)

        if duplicados == False:
            Escribirbasededatos(liquidacionescopiadas)
        
        else:
            print("Se encontraron numeros de liquidacion duplicados con respecto a la base de datos.")
            print("1-Para omitir los importes duplicados\n0-Para cancelar")
            respuesta=input("1/0:")                             #se podra cambiar el nombre respuesta por cursor?,  Revisar
            print("\n")
            if respuesta == "1":                                  #posibilidad de recortar codigo,                Revisar
                for i  in duplicados:
                    liquidacionescopiadas.pop(i)
                Escribirbasededatos(liquidacionescopiadas)               #TESTEAR YA!!
            elif respuesta == "0":                                   #Misma posibilidad de recortar                     
                onoffdeconfirmacion=0
            else:
                print(f'Opcion"{respuesta}" no encontrada, cancelando carga.')
                onoffdeconfirmacion=0

        if onoffdeconfirmacion == 1:
            print(f'Se a pegado el contenido de "Liquidaciones" en la base de datos correctamente')
            input("Presione ENTER para continuar\n")
            limpiarpantalla()
        else:
            print ("Se a Cancelado la carga de liquidacion en la base de datos.")
            input("Presione ENTER para continuar\n")
            limpiarpantalla()

    elif cursor=="9" or cursor=="9-": #Salir
        limpiarpantalla()
        print("9-Salir\n\n")
        print("Buenas noches")
        time.sleep(1)
        onoff=0

    else:           #Error cursor fuera de los parametros
        limpiarpantalla()
        print(f'Opcion "{cursor}" no encontrada.')



