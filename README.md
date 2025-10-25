# 🔮 `calcular_saldo-CLI` - Proyector de Saldos Futuros

**Programa de consola (CLI) para estimar saldos financieros en una fecha futura a partir de registros de transacciones.**

---

## 🚀 Requisitos y Configuración Inicial

Para que el programa funcione, es necesario crear una carpeta llamada `config` en el directorio raíz del proyecto.

Dentro de esta carpeta `config`, podrás alojar el archivo de liquidación bancaria, el cual debe nombrarse:

* **`Liquidación diaria.csv`**: Archivo que se descarga directamente de la página del banco.

> ⚠️ **Nota Importante:**
> Si la carpeta `config` no existe, el programa **se cerrará** y solicitará su creación para poder continuar.

---

## ⚙️ Funcionamiento General

Al iniciar, el programa realiza una verificación:

1.  **Verificación de Base de Datos:** Detecta automáticamente la existencia del archivo `database.csv`.
2.  **Creación (si es necesario):** Si `database.csv` no existe, el programa intentará crearlo.

---

## 📝 Opciones del Programa

El sistema presenta un menú con las siguientes funcionalidades:

### 1. Calcular Saldo a una Fecha Específica 🗓️

* **Solicita:** Una **fecha futura** (debe ser mayor a la fecha actual del sistema).
* **Proceso:** Suma todos los **activos** y resta todos los **pasivos** registrados cuyas fechas sean:
    * Posteriores a la fecha actual.
    * Inferiores o iguales a la fecha solicitada.

### 2. Agregar un Monto a la Ficha de Activos (Ingreso) ➕

* **Solicita:**
    * Una **fecha futura** (mayor a la fecha actual).
    * Un **monto positivo**.
    * Un **ID** o **Número de Liquidación**.
* **Verificación de Duplicados:** Chequea si el Número de Liquidación ya existe en `database.csv`.
    * **Si NO existe:** Pega la información en `database.csv`.
    * **Si SÍ existe:**
        * Muestra los registros duplicados.
        * Ofrece opciones para **eliminar** los registros duplicados existentes o **descartar** el nuevo registro.

### 3. Agregar un Monto a la Ficha de Pasivos (Egreso) ➖

* **Solicita:**
    * Una **fecha futura** (mayor a la fecha actual).
    * Un **monto** (si es positivo, se transforma internamente a negativo).
    * Un **ID** o **Número de Liquidación**.
* **Verificación de Duplicados:** Chequea si el Número de Liquidación ya existe en `database.csv`.
    * **Si NO existe:** Pega la información en `database.csv`.
    * **Si SÍ existe:**
        * Muestra los registros duplicados.
        * Ofrece opciones para **eliminar** los registros duplicados existentes o **descartar** el nuevo registro.

### 4. Copiar Información de "Liquidaciones Diarias" a la Base de Datos 🔄

Esta opción automatiza la carga de datos bancarios.

* **Origen:** Lee la información del archivo **`Liquidación diaria.csv`** (el cual tiene un formato similar al del archivo de ejemplo: `Ejemplo-Liquidación diaria.csv`).
* **Destino:** Pega la información extraída en **`database.csv`**.
* **Campos Relevantes (Índices CSV):** El programa toma los siguientes segmentos del archivo de origen para construir el registro:
    * **Segmento 0:** Fecha
    * **Segmento 9:** Monto
    * **Segmento 2:** Número de Liquidación (ID de Transacción)

### 5. Mostrar Información de la Base de Datos en Pantalla 📊

* Muestra un listado de **todos los registros** contenidos en `database.csv`.
* Los registros se muestran **ordenados por fecha**, desde el más lejano en el **futuro** hasta el más lejano en el **pasado**.

---

## 🛠️ Estructura de Datos

La información de saldos y transacciones se gestiona a través del archivo:

* **`database.csv`**: Almacena los registros de transacciones (activos/pasivos) para el cálculo de saldos.

