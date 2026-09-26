import requests # type: ignore
import json
import time

# LM Studio simula la API de OpenAI y corre por defecto en el puerto 1234
url = "http://localhost:1234/v1/chat/completions"
headers = {"Content-Type": "application/json"}

payload = {
    "model": "local-model", # LM Studio ignora el nombre, usa el que esté cargado
    "messages": [
        {"role": "system", "content": "Actúa como un desarrollador Python senior."},
        {"role": "user", "content": "Escribe un script en Python que consuma la API pública 'https://fakestoreapi.com/products', valide que la respuesta de red sea correcta (código 200). Luego, extrae el precio de todos los productos, calcula e imprime el precio promedio, el precio máximo y el precio mínimo. Finalmente, genera un gráfico de barras (usando matplotlib) mostrando el título y el precio de los primeros 5 productos de la lista. Incluye comentarios explicando el código."}
    ],
    "temperature": 0.7
}

print("Consultando a LM Studio localmente...")
start_time = time.time()

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    
    data = response.json()
    end_time = time.time()
    
    print("\n--- RESPUESTA DE LM STUDIO ---")
    print(data['choices'][0]['message']['content'])
    print(f"\n[Tiempo de respuesta: {round(end_time - start_time, 2)} segundos]")

except Exception as e:
    print(f"Error al conectar con LM Studio: {e}\n¿Aseguraste darle a 'Start Server' en LM Studio?")