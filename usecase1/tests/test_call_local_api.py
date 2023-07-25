from fastapi.testclient import TestClient

from ..config.test_data import TEST_DATA
from usecase1.src.phone_lookup_api import app  

client = TestClient(app)

def test_call_local_api():
    url = "http://localhost:8000/get_phone_details/"

    data = {
        "ANI": TEST_DATA["ANI"]
    }

    response = client.post(url, json=data)  

    assert response.status_code == 200
    assert response.json()["countryCode"] == TEST_DATA["countryCode"]
    assert response.json()["countryPrefix"] == TEST_DATA["countryPrefix"]
    assert response.json()["e164"] == TEST_DATA["e164"]