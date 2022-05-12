#\n <> \t []

from datetime import datetime
from logging import exception
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

def Escribirpasivo(texto):
    try:
        with open("config\Ficha de pasivos.csv", "a", newline="") as archivopcsv:
            escritor=csv.writer(archivopcsv, delimiter=";")
            escritor.writerows(texto)

    except FileNotFoundError:
        print(f"\tError!!\nError de tipo:FileNotFoundError\nEl programa no detecta la carpeta config.\nDe no existir la carpeta config dentro de la carpeta raiz del programa por favor: Crearla y reiniciar el programa \n--------------------------------------")
        input("Presione ENTER para continuar\n")


    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        archivopcsv.close()

def Escribiractivo(texto):
    try:
        with open("config\Ficha de activos.csv", "a", newline="")as archivoacsv:
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

def Delistastr(lista, caracter):
    return caracter.join(map(str, lista))

def Pasivosfuturos(añoinput, mesinput, diainput): #en base a la ficha de pasivos suma los pasivos anteriores a una fecha x 
    try:                                          #y posteriores a la fecha actual
        fechaactual=datetime.now()
        diaactual=int(datetime.strftime(fechaactual,"%d"))
        mesactual=int(datetime.strftime(fechaactual,"%m"))
        añoactual=int(datetime.strftime(fechaactual,"%Y"))
        montoscopiados=0.0
        with open("config\Ficha de pasivos.csv", "r") as archivoP:
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

def Activosfuturos(añoinput, mesinput, diainput): #en base a la ficha de activos suma los activos anteriores a una fecha x
    try:                                          #y posteriores a la fecha actual
        fechaactual=datetime.now()
        diaactual=int(datetime.strftime(fechaactual,"%d"))
        mesactual=int(datetime.strftime(fechaactual,"%m"))
        añoactual=int(datetime.strftime(fechaactual,"%Y"))
        montoscopiados=0.0
        with open("config\Ficha de activos.csv", "r") as archivoA:
            lector=csv.reader(archivoA, delimiter=";")
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
        archivoA.close()






print("//////////////////////////////////")
print("//\tSoftware de uso libre\t//")
print("//\t\t\t\t//")
print("//\t\t\t\t//")
print("//\t\tGdR\t\t//")
print("//     \tguidodorego@gmail.com   //")
print("//////////////////////////////////")
#time.sleep(2)
limpiarpantalla()

onoff=1

fecha_actual=datetime.now()
dia_actual=int(datetime.strftime(fecha_actual,"%d"))
mes_actual=int(datetime.strftime(fecha_actual,"%m"))
año_actual=int(datetime.strftime(fecha_actual,"%Y"))



while onoff==1:
    mostrarmenu()
    cursor=str(input("Elija una de las opciones:"))


    if cursor=="1":   #Calcular el saldo que se tendra en una fecha x
        limpiarpantalla()
        print("1-Calcular el saldo que se tendra en una fecha x\n\n")

        añosolicitado=int(input("Digite el año:"))
        messolicitado=int(input("Digite el mes:"))
        diasolicitado=int(input("Digite el dia:"))
        
        pasivo=Pasivosfuturos(añosolicitado, messolicitado, diasolicitado)
        activo=Activosfuturos(añosolicitado, messolicitado, diasolicitado)
        pn=activo-pasivo

        print("Segun la base de datos:\n\n")
        print(f"En la fecha:{diasolicitado}/{messolicitado}/{añosolicitado}")
        print("-------------------------------------")
        print(f"El monto total de la cuenta será de:${pn:.2f}")
        input("Presione ENTER para continuar\n")
        limpiarpantalla()

    elif cursor=="2": #Agregar un monto a la ficha de activos
        limpiarpantalla()
        print("2-Agregar un monto a la ficha de activos\n\n")

        añosolicitado=int(input("Digite el año:"))
        messolicitado=int(input("Digite el mes:"))
        diasolicitado=int(input("Digite el dia:"))
        montosolicitado=float(input("Digite el monto:"))

        datos_a_pegar=[[añosolicitado, messolicitado, diasolicitado, montosolicitado]]

        Escribiractivo(datos_a_pegar)

        print(f'Se a pegado "{datos_a_pegar}" correctamente')
        input("Presione ENTER para continuar\n")
        limpiarpantalla()

    elif cursor=="3": #Agregar un monto a la ficha de pasivos
        limpiarpantalla()
        print("3-Agregar un monto a la ficha de pasivos\n\n")

        añosolicitado=int(input("Digite el año:"))
        messolicitado=int(input("Digite el mes:"))
        diasolicitado=int(input("Digite el dia:"))
        montosolicitado=float(input("Digite el monto:"))

        datos_a_pegar=[[añosolicitado, messolicitado, diasolicitado, montosolicitado]]

        Escribirpasivo(datos_a_pegar)

        print(f'Se a pegado "{datos_a_pegar}" correctamente')
        input("Presione ENTER para continuar\n")
        limpiarpantalla()

    elif cursor=="4": #Copiar info. de "Liquidacion diaria" en "Ficha de activos"
        try:
            with open("config\Liquidación diaria.csv", "r") as archivolcsv:
                next(archivolcsv, None) #Evito la primera linea por ser encabezado
                lector=csv.reader(archivolcsv, delimiter=";")
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
                    diacopiado=int(Delistastr(listadia, ""))

                    listames=list(linea[0])
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
                    mescopiado=int(Delistastr(listames,""))

                    listaaño=list(linea[0])
                    listaaño.reverse()
                    listaaño.pop()
                    listaaño.pop()
                    listaaño.pop()
                    listaaño.pop()
                    listaaño.pop()
                    listaaño.pop()
                    listaaño.reverse()
                    añocopiado=int(Delistastr(listaaño,""))

                    listamonto=list(linea[9])

                    if "." in linea[9]:
                        listamonto.remove(".")
        
                        indice=listamonto.index(",")
                        listamonto.pop(indice)
                        listamonto.insert(indice,".")

                    montocopiado=float(Delistastr(listamonto,""))
                    liquidacionescopiadas+=[[añocopiado,mescopiado, diacopiado, montocopiado]]

                Escribiractivo(liquidacionescopiadas)
                print(f'Se a pegado el contenido de "Liquidaciones" correctamente en "Ficha de activos"')
                input("Presione ENTER para continuar\n")
                limpiarpantalla()

        except Exception as e:
            print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
            input("Presione ENTER para continuar\n")

        finally:
            archivolcsv.close()

    elif cursor=="9": #Salir
        limpiarpantalla()
        print("9-Salir\n\n")
        print("Buenas noches")
        time.sleep(1)
        onoff=0

    else:           #Error cursor fuera de los parametros
        limpiarpantalla()
        print(f'Opcion "{cursor}" no encontrada.')



