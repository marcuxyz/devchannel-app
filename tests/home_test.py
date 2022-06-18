from flask import url_for

from tests.factories.channel_factory import ChannelFactory

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
    channel = ChannelFactory.create()

    response = client.get(url_for("home.index"))
  
    assert channel.name in response.get_data(as_text=True)
