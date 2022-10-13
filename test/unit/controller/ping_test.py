from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


class TestPingController:

    @staticmethod
    def test_ping(client: TestClient) -> None:
        response = client.get(url="/ping")
        assert response.status_code == HTTP_200_OK
