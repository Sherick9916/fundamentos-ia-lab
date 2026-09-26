# Parcial 1 - Laboratorio: Fundamentos de IA para el Desarrollo de Software Aumentado

**Curso:** Fundamentos de Inteligencia Artificial - Ingeniería de Sistemas  
**Propósito:** Usar modelos de IA como herramientas de aumentación dentro del ciclo de vida clásico del desarrollo de software.

## 👥 Integrantes del Equipo
* Ricardo Granados Estrada

## 📂 Estructura del Repositorio
Este repositorio documenta nuestra ruta de aprendizaje práctico, pasando desde los fundamentos teóricos hasta el desarrollo de una solución real con Inteligencia Artificial:

* `/mapa_mental`: Relación de conceptos esenciales de IA, modelos y arquitecturas.
* `/cartografia_modelos`: Matriz comparativa del ecosistema actual de modelos de IA[cite: 1].
* `/modelos_locales`: Evidencias y scripts de ejecución de modelos locales (Ollama y LM Studio) consumidos vía API[cite: 1].
* `/vibe_coding`: Comparativa empírica resolviendo un mismo problema con modelos generalistas locales, de código locales y en la nube[cite: 1].
* `/serie_temporal`: Reto integrador (aplicación modular en Python) que consume una API pública y predice temperaturas usando Pandas y IA[cite: 1].
* `/evidence`: Capturas de pantalla, consumo de recursos y gráficas de los resultados obtenidos[cite: 1].

## ⚙️ Requisitos Previos
Para ejecutar los scripts de este repositorio, es necesario instalar las dependencias de Python listadas en el proyecto[cite: 1]. Ejecute el siguiente comando en la terminal:
```bash
pip install -r requirements.txt
```
Cómo ejecutar el Reto Integrador (Serie Temporal)
La aplicación principal se conecta a la API histórica de Open-Meteo, procesa los datos de temperatura de Manizales (2023) y genera predicciones comparando un modelo de media móvil contra un baseline de persistencia[cite: 1].

Para ejecutar el proyecto, ingrese a la carpeta correspondiente e inicie la aplicación principal:

cd serie_temporal
python app.py

Al finalizar la ejecución en consola, el sistema desplegará automáticamente la gráfica comparativa de la serie temporal