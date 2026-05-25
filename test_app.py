from app import app

client = app.test_client()

def test_home():
    response = client.get('/')
    assert response.status_code == 200

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'UP'

def test_add():
    response = client.get('/add/10/20')
    assert response.status_code == 200
    assert response.json['result'] == 30