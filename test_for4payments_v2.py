#!/usr/bin/env python3
import requests
import json

# Test different data formats with For4Payments API
API_URL = "https://app.for4payments.com.br/api/v1/transaction.purchase"
SECRET_KEY = "048a81ec-560b-4e3e-bb97-abd49cb02a46"

headers = {
    'Authorization': SECRET_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Test with valid CPF and required fields
test_data = {
    "name": "JOÃO DA SILVA SANTOS",
    "email": "joodasilvasantos@gmail.com",
    "cpf": "11144477735",  # Valid CPF format
    "phone": "11999999999",
    "paymentMethod": "PIX",
    "amount": 11868,
    "items": [{
        "title": "Regularizar Débitos",
        "quantity": 1,
        "unitPrice": 11868,
        "tangible": False
    }]
}

print("Testing with valid CPF...")
try:
    response = requests.post(API_URL, json=test_data, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Success! Transaction ID: {data.get('id')}")
        print(f"PIX Code: {data.get('pixCode', 'Not found')}")
        print(f"QR Code: {data.get('pixQrCode', 'Not found')}")
    print()
except Exception as e:
    print(f"Error: {e}")
    print()

# Test with different amount formats
test_data_2 = {
    "name": "JOÃO DA SILVA SANTOS",
    "email": "joodasilvasantos@gmail.com",
    "cpf": "11144477735",
    "phone": "11999999999",
    "paymentMethod": "PIX",
    "amount": 1000,  # R$ 10.00
    "items": [{
        "title": "Regularizar Débitos",
        "quantity": 1,
        "unitPrice": 1000,
        "tangible": False
    }]
}

print("Testing with smaller amount...")
try:
    response = requests.post(API_URL, json=test_data_2, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Success! Transaction ID: {data.get('id')}")
        print(f"PIX Code: {data.get('pixCode', 'Not found')}")
        print(f"QR Code: {data.get('pixQrCode', 'Not found')}")
    print()
except Exception as e:
    print(f"Error: {e}")
    print()