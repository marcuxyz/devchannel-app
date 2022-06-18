from flask import url_for

from app.models import Channel
from app.extensions import db



def test_should_access_home_page(client):
    response = client.get(url_for("home.index"))

    assert response.status_code == 200
    assert "Dev Channel" in response.get_data(as_text=True)
    assert "Sign in" in response.get_data(as_text=True)
    assert "Sign up" in response.get_data(as_text=True)
    assert "Add Channel" in response.get_data(as_text=True)
    assert "Add Programing Language" in response.get_data(as_text=True)
    assert (
        "&COPY;Dev Channel todos os direitos reservados. 2022"
        in response.get_data(as_text=True)
    )

def test_should_view_channels(client):
    channel = Channel(name='Marcus Pereira', url='https://youtube.com',
    description='Um canal que fala sobre desenvolvimento web utilizando Python',
    country='br', video='https://youtube.com', image=b'marcuspereira.jpg')
    db.session.add(channel)
    db.session.commit()

    response = client.get(url_for("home.index"))
   
    assert 'Marcus Pereira' in response.get_data(as_text=True)
