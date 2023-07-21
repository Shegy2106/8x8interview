import requests
from ..config.test_data import TEST_DATA

def test_call_local_api():
    url = "http://localhost:8000/get_phone_details/"

    data = {
        "ANI": TEST_DATA["ANI"]
    }

    response = requests.post(url, json=data)  # Use json parameter instead of data

    assert response.status_code == 200
    assert response.json()["countryCode"] == TEST_DATA["countryCode"]
    assert response.json()["countryPrefix"] == TEST_DATA["countryPrefix"]
    assert response.json()["e164"] == TEST_DATA["e164"]