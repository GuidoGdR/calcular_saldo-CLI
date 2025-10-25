# calcular_saldo-1-

//////////////////////////////////
// Software de uso libre /////////
//-----------------------/////////
//author:GdR             /////////
//guidodorego@gmail.com  /////////
//////////////////////////////////



programa para calcular saldos que se tendra en una fecha futura (sin interfaz grafica).
**************************************************************************************

Requiere una carpeta "config": dentro de la que podremos alojar el archivo "Liquidación diaria.csv" tal y como se descarga de la pagina de el banco.
---------------------------------------------------------------------------------------------------------------------------------------------------


Funcionamiento:
    Al iniciar el programa detectara automaticamente si existe o no el database.csv, de no existir intentara crearlo.
        *De no existir la carpeta config el programa se cerrara y pedira su creacion
    OPCIONES:
        1-Calcular el saldo que se tendra en una fecha x
            Solicita una fecha (La cual debe ser mayor a la fecha actual que marca el sistema), posteriormente
            suma todos los activos y le resta todos los pasivos que indican los registros son: posteriores a la 
            fecha actual y inferiores o iguales a la fecha solicitada

        2-Agregar un monto a la ficha de activos
            Solicita una fecha (La cual debe ser mayor a la fecha actual que marca el sistema), un monto (el cual
            debe ser positivo) y un ID o numero de liquidación.
            Posteriormente chequea que el numero de liquidacion no se encuentre ya en la base de datos:
            De no existir:
                pega la informacion dentro de el archivo database.csv
            De existir:
                Muestra cuales son los duplcados y da opciones para eliminar los registros duplicados existentes
                o los nuevos que estarian intentando de entrara a database.csv
        
        3-Agregar un monto a la ficha de activos
            Solicita una fecha (La cual debe ser mayor a la fecha actual que marca el sistema), un monto (de ser 
            positivo lo transforama en negativo) y un ID o numero de liquidación.
            Posteriormente chequea que el numero de liquidacion no se encuentre ya en la base de datos:
            De no existir:
                pega la informacion dentro de el archivo database.csv
            De existir:
                Muestra cuales son los duplcados y da opciones para eliminar los registros duplicados existentes
                o los nuevos que estarian intentando de entrara a database.csv
        
        4-Copiar info, de "liquidaciónes diarias" en la base de datos
            Copia la informacion de el archivo "Liquidaciónes diarias" (el cual el banco entrega tal como se 
            muestra en el archivo "Ejemplo-Liquidación diaria.csv") y la pega en el archivo database.csv
                De el archivo "Liquidación diaria.csv" el programa tomara los segmentos 0, 9 y 2 para obtener 
                la fecha, el monto y el numero de liquidacion (ID de transaccion)

        5-Mostrar info. de base de datos en pantalla
            muestra un listado con todos los registros que se encuentran en database.csv ordenados segun
            la fecha para posicionarlos desde el mas lejano en el futuro al mas lejano en el pasado.
 




