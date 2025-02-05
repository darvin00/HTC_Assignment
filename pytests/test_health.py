# test_health.py
import requests

def test_health():
    response = requests.get('http://18.236.161.197:8000/health')  
    assert response.status_code == 200
