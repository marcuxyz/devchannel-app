from pytest import fixture

from app import create_app


@fixture
def client():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()

    with app.test_client() as client:
        db.create_all()
        
        yield client

        db.session.remove()
        db.drop_all()
