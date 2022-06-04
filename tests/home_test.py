from app import create_app
from pytest import fixture

def test_should_access_home_page():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert 'Home Page' in response.get_data(as_text=True)