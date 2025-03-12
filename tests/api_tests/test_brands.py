import pytest

class TestBrands:

    def test_get_all_brands(self, api_client):
        response = api_client.get("/brandsList")
        response_json = response.json()

        assert response_json.get("responseCode") == 200

    def test_put_to_all_products(self, api_client):
        response = api_client.put("/productsList")
        response_json = response.json()

        assert response_json.get("responseCode") == 405
        assert response_json.get("message") == "This request method is not supported."
