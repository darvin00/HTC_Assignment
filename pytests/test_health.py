# test_health.py
import requests

def test_health():
<<<<<<< HEAD
    response = requests.get('http://34.212.182.222:8000/health')  
=======
    response = requests.get('http://34.212.182.222:5000/health')  
>>>>>>> 8c509e9 (updated)
    assert response.status_code == 200
