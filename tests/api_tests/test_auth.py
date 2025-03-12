import pytest

class TestAuth:

    def test_login_valid_credentials(self,api_client):
        payload = {"email":"testvalid@example.com", "password":"validlogin"}
        response = api_client.post("/verifyLogin",data=payload)

        response_json = response.json()

        assert response_json.get("responseCode") == 200
        assert response_json.get("message") == "User exists!"


    def test_login_invalid_credentials(self,api_client):
        payload = {"email":"testinvalid@example.com", "password":"invalidlogin"}
        response = api_client.post("/verifyLogin",data=payload)

        response_json = response.json()

        assert response_json.get("responseCode") == 404
        assert response_json.get("message") == "User not found!"


    def test_login_without_pass(self,api_client):
        payload = {"email":"testvalid@example.com"}
        response = api_client.post("/verifyLogin",data=payload)
        response_json = response.json()

        assert response_json.get("responseCode") == 400
        assert response_json.get("message") == "Bad request, email or password parameter is missing in POST request."


    def test_del_req_to_login(self, api_client):
        response = api_client.delete("/verifyLogin")
        response_json = response.json()

        assert response_json.get("responseCode") == 405
        assert response_json.get("message") == "This request method is not supported."
