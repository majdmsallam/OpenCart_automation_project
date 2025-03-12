import pytest

class TestProducts:

    def test_get_all_products(self, api_client):
        response = api_client.get("/productsList")
        response_json = response.json()

        assert response_json.get("responseCode") == 200

    def test_post_to_all_products(self, api_client):
        response = api_client.post("/productsList")
        response_json = response.json()

        assert response_json.get("responseCode") == 405
        assert response_json.get("message") == "This request method is not supported."

    @pytest.mark.parametrize("search_term", ["top", "tshirt", "jean"])
    def test_search_product(self, api_client, search_term):
        payload = {"search_product": search_term}
        response = api_client.post("/searchProduct", data=payload)
        response_json = response.json()
        print(response_json)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert len(response_json["products"]) > 0, "No products found for search term"

    def test_search_without_product(self, api_client):
        response = api_client.post("/searchProduct")
        response_json = response.json()

        assert response_json.get("responseCode") == 400
        assert response_json.get("message") == "Bad request, search_product parameter is missing in POST request."

