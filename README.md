# Proyecto Final - Predicción de Churn

Este proyecto tiene como objetivo entrenar y desplegar un modelo de Machine Learning para predecir si un cliente abandona o no el servicio. La base de datos utilizada contiene información de clientes como edad, país, género, balance, número de productos, tipo de tarjeta, salario estimado, entre otras variables.

## Base de datos

Se utilizó la base de datos `Customer-Churn-Records.csv`.

La base contiene 10,000 registros y 18 columnas relacionadas con clientes de un banco.

## Variable cualitativa seleccionada

La variable que se eligió para predecir fue:

`Exited`

Esta variable indica si un cliente abandonó el servicio o no.

- `0`: el cliente no abandonó el servicio.
- `1`: el cliente sí abandonó el servicio.

Esta variable es cualitativa/binaria porque clasifica a los clientes en dos categorías.

## Modelo utilizado

Se entrenó un modelo de clasificación usando `RandomForestClassifier`.

Para evaluar el modelo, se utilizó un `train-test split`, separando los datos en entrenamiento y prueba.

El modelo entrenado se guardó en el archivo:

`model.pkl`

También se generó el archivo:

`umbral.json`

## Estructura del proyecto

El repositorio está organizado usando programación orientada a objetos. Cada archivo tiene una función específica:

- `database.py`: carga la base de datos.
- `model.py`: prepara los datos, entrena el modelo y guarda el archivo `model.pkl`.
- `score.py`: archivo utilizado por Azure para recibir datos y regresar predicciones.
- `deployer.py`: contiene información del despliegue realizado en Azure.
- `main.py`: ejecuta el flujo principal del proyecto.
- `requirements.txt`: contiene las librerías necesarias.
- `Customer-Churn-Records.csv`: base de datos utilizada.
- `model.pkl`: modelo entrenado.
- `umbral.json`: archivo con el umbral utilizado.
- `Model.ipynb`: notebook usado durante el desarrollo del modelo.

## Despliegue en Azure

El modelo fue desplegado en Azure Machine Learning usando un endpoint en línea.

Nombre del endpoint:

`apifinal8`

Nombre de la implementación:

`modelo-1`

El tráfico fue asignado al 100% a la implementación `modelo-1`.

## Prueba de la API

La API se probó desde la pestaña de prueba de Azure usando un JSON de entrada.

La respuesta obtenida fue:

`[0.9944933385275183]`

Esto demuestra que el endpoint respondió correctamente desde la nube.

## Cómo correr el proyecto

Primero se instalan las librerías necesarias:

```bash
pip install -r requirements.txt
