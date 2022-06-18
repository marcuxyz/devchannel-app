from pytest import fixture

from app import create_app


@fixture
def client():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()
    return app.test_client()
