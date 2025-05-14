import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_healthcheck():
    response = client.get("/healthcheck/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "detail": "Service healthy",
    }


@pytest.mark.asyncio
async def test_home_with_parameters():
    response = client.get("/?name=Recruto&message=Давай дружить")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Hello Recruto!" in response.text
    assert "Давай дружить!" in response.text


@pytest.mark.asyncio
async def test_home_without_parameters():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Hello Guest!" in response.text
    assert "Welcome!" in response.text


@pytest.mark.asyncio
async def test_home_invalid_parameters():
    response = client.get("/?name=12312ADASDWAEDQWDA&message=Test")
    assert response.status_code == 200
    assert "Hello 12312ADASDWAEDQWDA!" in response.text
    assert "Test!" in response.text
