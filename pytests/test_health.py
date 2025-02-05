# test_health.py
import requests

def test_health():
    response = requests.get('http://34.212.25.129:8000/health')  
    assert response.status_code == 200
