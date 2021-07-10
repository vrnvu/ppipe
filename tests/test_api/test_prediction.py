from wikiqueue.webservice.core import config


def test_prediction(test_client) -> None:
    response = test_client.post(
        "/api/prediction/predict",
        json={"value": 1},
        headers={"token": str(config.API_KEY)},
    )
    assert response.status_code == 200
    # assert "value" in response.json()
    # assert "currency" in response.json()


def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/prediction/predict", json={}, headers={"token": str(config.API_KEY)}
    )
    assert response.status_code == 422
