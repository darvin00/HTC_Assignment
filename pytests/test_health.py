# test_health.py
import requests

def test_health():
    response = requests.get('http://54.149.140.148:8000/health')  
    assert response.status_code == 200
