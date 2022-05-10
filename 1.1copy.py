# \n <> \t []

from datetime import datetime

import time
import os
import csv



def limpiarpantalla():
    if os.name=="nt" or os.name=="dos":
        comando="cls"
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
        with open("config\database.csv", "a", newline="")as archivoacsv:
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
        onoffdatabase_close=1
        with open("config\database.csv", "r") as infodatabase:
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
        fechaactual=datetime.now()
        diaactual=int(datetime.strftime(fechaactual,"%d"))
        mesactual=int(datetime.strftime(fechaactual,"%m"))
        añoactual=int(datetime.strftime(fechaactual,"%Y"))
        montoscopiados=0.0
        with open("config\database.csv", "r") as archivoP:
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
        with open("config\Liquidación diaria.csv", "r") as archivoL:
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

    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        archivoL.close()

def Chequeoduplicados(listachica, listagrande): #Chequea si hay duplicados, de haberlos retorna cuales son sus num de indice en lista chica
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
    try:
        onoffdatabase_close=1
        with open("config\database.csv", "r") as infodatabase:
            pass

    except FileNotFoundError:
        onoffdatabase_close=0
        print('No se a encontrado el archivo "database.csv" necesario para el correcto funcionamiento')
        print("1- Crear archivo vacío\n2- Continuar")
        opcion=str(input("Elija una de las opciones:"))
        if opcion == "1" or opcion == "1-":
            try:
                with open("config\database.csv", "w") as infodatabase:
                    pass

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

        añosolicitado=int(input("Digite el año:"))
        messolicitado=int(input("Digite el mes:"))
        diasolicitado=int(input("Digite el dia:"))
        
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

        añosolicitado=int(input("Digite el año:"))
        messolicitado=int(input("Digite el mes:"))
        diasolicitado=int(input("Digite el dia:"))
        montosolicitado=float(input("Digite el monto:"))                 #REVISAR
        numerodeliquidacionsolicitado=str(input("Digite el numero de liquidacion:")) #Es una especie de numero de serie para no repetir datos

        infodatabase=Infodatabase()
        v=Chequeoduplicados2(numerodeliquidacionsolicitado, infodatabase)



        datos_a_pegar=[[añosolicitado, messolicitado, diasolicitado, montosolicitado, numerodeliquidacionsolicitado]]

        Escribirbasededatos(datos_a_pegar)

        print(f'Se a pegado "{datos_a_pegar}" correctamente')
        input("Presione ENTER para continuar\n")
        limpiarpantalla()

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
                print(f'Opcion"{respuesta}" no encontrada.')
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



