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

# Test 1: Current format
test_data_1 = {
    "name": "JOÃO DA SILVA SANTOS",
    "email": "joodasilvasantos@gmail.com",
    "cpf": "12345678900",
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

print("Testing current format...")
try:
    response = requests.post(API_URL, json=test_data_1, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print()
except Exception as e:
    print(f"Error: {e}")
    print()

# Test 2: With customer object
test_data_2 = {
    "customer": {
        "name": "JOÃO DA SILVA SANTOS",
        "email": "joodasilvasantos@gmail.com",
        "cpf": "12345678900",
        "phone": "11999999999"
    },
    "paymentMethod": "PIX",
    "amount": 11868,
    "items": [{
        "title": "Regularizar Débitos",
        "quantity": 1,
        "unitPrice": 11868,
        "tangible": False
    }]
}

print("Testing with customer object...")
try:
    response = requests.post(API_URL, json=test_data_2, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print()
except Exception as e:
    print(f"Error: {e}")
    print()

# Test 3: Minimal format
test_data_3 = {
    "name": "JOÃO DA SILVA SANTOS",
    "email": "joodasilvasantos@gmail.com",
    "cpf": "12345678900",
    "phone": "11999999999",
    "paymentMethod": "PIX",
    "amount": 11868
}

print("Testing minimal format...")
try:
    response = requests.post(API_URL, json=test_data_3, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print()
except Exception as e:
    print(f"Error: {e}")
    print()

# Test 4: With Bearer token
headers_bearer = {
    'Authorization': f'Bearer {SECRET_KEY}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

print("Testing with Bearer token...")
try:
    response = requests.post(API_URL, json=test_data_1, headers=headers_bearer, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print()
except Exception as e:
    print(f"Error: {e}")
    print()