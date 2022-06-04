from flask import url_for

def test_should_access_home_page(client):
    response = client.get(url_for('home.index'))

    assert response.status_code == 200
    assert 'Dev Channel' in response.get_data(as_text=True)
