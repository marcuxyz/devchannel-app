def test_should_access_home_page(client):
    response = client.get('/')

    assert response.status_code == 200
    assert 'Home Page' in response.get_data(as_text=True)
