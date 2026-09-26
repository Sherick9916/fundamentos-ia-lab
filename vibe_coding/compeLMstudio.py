import requests
import json
import matplotlib.pyplot as plt

# URL de la API pública
url = 'https://fakestoreapi.com/products'

def fetch_products():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            products = response.json()
            return products
        else:
            print(f"Error al obtener productos: {response.status_code}")
            return []
    
    except Exception as e:
        print(f"Error al obtener los productos: {e}")
        return []

def calculate_average_price(products):
    if not products:
        return 0.0
    
    total_price = sum(product['price'] for product in products)
    count = len(products)
    average_price = total_price / count
    return average_price

def find_min_max_and_average(products):
    if not products:
        return None, None, None
    
    min_product = min(products, key=lambda x: x['price'])
    max_product = max(products, key=lambda x: x['price'])
    average_product = calculate_average_price(products)
    
    return min_product, max_product, average_product

def main():
    # Obtener los productos desde la API pública
    products = fetch_products()
    
    if not products:
        print("No se han obtenido productos")
        return
    
    # Calcular el precio promedio
    average_price = calculate_average_price(products)
    print(f"El precio promedio de todos los productos es: {average_price}")
    
    # Extraer y calcular los precios mínimos y máximos
    min_product, max_product, average_product = find_min_max_and_average(products)
    if min_product is not None:
        print(f"El precio mínimo de los primeros 5 productos es: ${min_product['price']:.2f}")
    if max_product is not None:
        print(f"El precio máximo de los primeros 5 productos es: ${max_product['price']:.2f}")
    
    # Generar un gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar([product['title'] for product in products], [product['price'] for product in products])
    plt.title('Precio de los primeros 5 productos')
    plt.xlabel('Nombre del producto')
    plt.ylabel('Precio')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()