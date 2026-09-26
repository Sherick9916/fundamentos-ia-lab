# Reto Integrador: Serie Temporal de Temperatura

## Decisiones de Arquitectura
* **Fuente de datos:** Se utilizó la API pública de Open-Meteo para obtener datos históricos (2023) de temperatura diaria en la ciudad de Manizales.
* **Estructura:** Se optó por una arquitectura modular (5 archivos) separando la extracción (`api_client.py`), el procesamiento con Pandas (`preprocessing.py`), la lógica predictiva (`model.py`), la evaluación (`evaluation.py`) y la orquestación (`app.py`). Esto facilita el mantenimiento y escalabilidad.
* **Separación de datos:** Se respetó estrictamente la flecha del tiempo, dividiendo el dataset en 80% entrenamiento y 20% prueba de forma secuencial, evitando la filtración de datos futuros en el pasado.

## Uso de la IA (Vibe Coding)
La Inteligencia Artificial se utilizó en este reto como herramienta de aumentación para:
1. **Generación de Boilerplate:** Acelerar la escritura de la estructura básica de los scripts y la configuración de Matplotlib.
2. **Implementación de Fórmulas:** Facilitar la escritura de las funciones matemáticas para el cálculo del MAE (Error Absoluto Medio) y RMSE (Raíz del Error Cuadrático Medio) utilizando Numpy.
3. **Manejo de Pandas:** Agilizar la limpieza de datos nulos y la asignación correcta del índice temporal en el DataFrame.

## Resultados
El modelo predictivo de Media Móvil (ventana de 7 días) logró superar al modelo base de persistencia, reduciendo los márgenes de error MAE y RMSE, como se evidencia en las pruebas de ejecución.