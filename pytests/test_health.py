# test_health.py
import requests

def test_health():
    response = requests.get('http://54.149.196.104:8000/health')  
    assert response.status_code == 200
