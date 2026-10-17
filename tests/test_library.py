import pytest
from app.library import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Smart Library Management Platform"


def test_list_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_add_book(client):
    response = client.post(
        "/books",
        json={"title": "Cloud Computing", "author": "Alex"}
    )

    assert response.status_code == 201
    assert response.json["title"] == "Cloud Computing"
    assert response.json["available"] is True


def test_add_book_missing_fields(client):
    response = client.post("/books", json={"title": "Cloud Computing"})
    assert response.status_code == 400
