import requests
import random

def test_supplier_api_check():
    response = requests.get('https://fakestoreapi.com/products/1')

    assert response.status_code == 200 

    product = response.json()

    # randomizer = random.randint(-150, 150)
    # product['price'] = randomizer

    print (f"\nPRICE = {product['price']}")

    assert product['price'] > 0 