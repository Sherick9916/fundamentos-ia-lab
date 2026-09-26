import requests
import matplotlib.pyplot as plt

# URL de la API pública de FakeStoreAPI
url = 'https://fakestoreapi.com/products'

# Realizar la petición HTTP GET a la API
response = requests.get(url)

# Valida que la respuesta de red sea correcta (código 200)
if response.status_code == 200:
    # Extraer el precio de todos los productos
    prices = [product['price'] for product in response.json()]
    
    # Calcular el precio promedio
    promedio = sum(prices) / len(prices)
    
    # Calcular el precio máximo
    maximo = max(prices)
    
    # Calcular el precio mínimo
    minimo = min(prices)

    # Imprimir los resultados
    print('Precio promedio:', promedio)
    print('Precio máximo:', maximo)
    print('Precio mínimo:', minimo)

    # Generar un gráfico de barras para los primeros 5 productos
    # Extraer el título y el precio de los primeros 5 productos
    titulos = [product['title'] for product in response.json()[:5]]
    precios = [product['price'] for product in response.json()[:5]]

    # Crear el gráfico
    plt.bar(titulos, precios)
    plt.title('Títulos y Precios de los Primeros 5 Productos')
    plt.xlabel('Título')
    plt.ylabel('Precio')
    plt.xticks(rotation=90)  # Rotar los ejes x para visualizar mejor los títulos
    plt.tight_layout()  # Ajustar el layout para que los títulos queden dentro del gráfico
    plt.show()

else:
    print('Error al obtener la respuesta de la API:', response.status_code)