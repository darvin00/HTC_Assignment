# test_health.py
import requests

def test_health():
    response = requests.get('http://192.168.29.24:8000/health')  
    assert response.status_code == 200
