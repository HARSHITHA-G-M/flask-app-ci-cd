from app.app import app  # 👈 import the actual Flask app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask CI/CD Pipeline!" in response.data

