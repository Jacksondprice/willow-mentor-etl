from app import create_app


def test_create_and_list():
    client = create_app().test_client()
    assert client.post("/api/classrooms", json={"name": "Unit"}).status_code == 201
    assert client.get("/api/classrooms").json[0]["name"] == "Unit"
