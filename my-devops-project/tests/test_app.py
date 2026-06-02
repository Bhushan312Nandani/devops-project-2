from app import app


def test_home_page_returns_ok():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps Learning App' in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['service'] == 'devops-learning'


def test_version_endpoint():
    client = app.test_client()
    response = client.get('/version')
    assert response.status_code == 200
    data = response.get_json()
    assert data['version'] == 'v2.0'
    assert data['build'] == 'github-actions'


def test_info_endpoint():
    client = app.test_client()
    response = client.get('/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['service'] == 'DevOps Learning App'
    assert '/health' in data['endpoints']
