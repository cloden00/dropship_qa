import requests

def test_supplier_api_check():
    r = requests.get('https://fakestoreapi.com/products/1')

    assert r.status_code == 200 

