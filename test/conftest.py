import pytest
from fastapi.testclient import TestClient
from app import create_app


@pytest.fixture
def client() -> TestClient:
    fast_app = create_app()
    return TestClient(fast_app)
