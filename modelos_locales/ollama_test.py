import requests # type: ignore
import json
import time

# Ollama por defecto corre en el puerto 11434
url = "http://localhost:11434/api/generate"

# Asegúrate de poner el nombre del modelo exacto que descargaste en el paso 3.1
payload = {
    "model": "llama3.2", 
    "prompt": "Actúa como un desarrollador Python senior. Escribe un script en Python que consuma la API pública 'https://fakestoreapi.com/products', valide que la respuesta de red sea correcta (código 200). Luego, extrae el precio de todos los productos, calcula e imprime el precio promedio, el precio máximo y el precio mínimo. Finalmente, genera un gráfico de barras (usando matplotlib) mostrando el título y el precio de los primeros 5 productos de la lista. Incluye comentarios explicando el código.",
    "stream": False # False para que nos devuelva toda la respuesta de una vez
}

print("Consultando a Ollama localmente...")
start_time = time.time()

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()
    
    data = response.json()
    end_time = time.time()
    
    print("\n--- RESPUESTA DE OLLAMA ---")
    print(data['response'])
    print(f"\n[Tiempo de respuesta: {round(end_time - start_time, 2)} segundos]")

except Exception as e:
    print(f"Error al conectar con Ollama: {e}")