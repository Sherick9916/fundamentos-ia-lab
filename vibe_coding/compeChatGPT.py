import requests
import matplotlib.pyplot as plt

# URL de la API pública
URL = "https://fakestoreapi.com/products"

# Realizamos la petición GET a la API
respuesta = requests.get(URL)

# Validamos que la respuesta de red sea correcta
if respuesta.status_code == 200:
    # Convertimos la respuesta JSON en una lista de diccionarios
    productos = respuesta.json()

    # Extraemos el precio de cada producto
    precios = [producto["price"] for producto in productos]

    # Calculamos las estadísticas
    precio_promedio = sum(precios) / len(precios)
    precio_maximo = max(precios)
    precio_minimo = min(precios)

    # Imprimimos los resultados
    print(f"Precio promedio: ${precio_promedio:.2f}")
    print(f"Precio máximo: ${precio_maximo:.2f}")
    print(f"Precio mínimo: ${precio_minimo:.2f}")

    # Tomamos solamente los primeros 5 productos para el gráfico
    primeros_5 = productos[:5]

    # Extraemos sus títulos y precios
    titulos = [producto["title"] for producto in primeros_5]
    precios_5 = [producto["price"] for producto in primeros_5]

    # Creamos el gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(titulos, precios_5)

    # Añadimos título y etiquetas
    plt.title("Precio de los primeros 5 productos")
    plt.xlabel("Producto")
    plt.ylabel("Precio ($)")

    # Rotamos los títulos para facilitar su lectura
    plt.xticks(rotation=45, ha="right")

    # Ajustamos automáticamente los márgenes
    plt.tight_layout()

    # Mostramos el gráfico
    plt.show()

else:
    # Si la API no devuelve 200, mostramos el código recibido
    print(f"Error al consultar la API. Código HTTP: {respuesta.status_code}")