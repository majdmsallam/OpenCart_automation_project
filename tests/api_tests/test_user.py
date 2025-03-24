import pytest

class TestUser:

    @pytest.mark.parametrize("data", [
        {
            "name": "majd Doe",
            "email": "khaled123.doe@example.com",
            "password": "Password123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "5",
            "birth_year": "1990",
            "firstname": "majd",
            "lastname": "Doe",
            "company": "Test Corp",
            "address1": "123 Test St",
            "address2": "Apt 4",
            "country": "United States",
            "zipcode": "12345",
            "state": "California",
            "city": "Los Angeles",
            "mobile_number": "1234567890"
        }
    ])
    def test_create_account(self,api_client, data):
        response = api_client.post("/createAccount", data=data)
        response_json = response.json()
        print(response_json)
        assert response_json["responseCode"] == 201
        assert response_json["message"] == "User created!"

    def test_delete_account(self, api_client):
        payload = {"email":"khaled123.doe@example.com", "password":"Password123"}
        response = api_client.delete("/deleteAccount", data=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["message"] == "Account deleted!"

    @pytest.mark.parametrize("data", [
        {
            "name": "majd sameh",
            "email": "update_get_details@example.com",
            "password": "Password123",
            "title": "Mr",
            "birth_date": "5",
            "birth_month": "5",
            "birth_year": "1980",
            "firstname": "majd",
            "lastname": "Doe",
            "company": "Test Corp",
            "address1": "123 Test St",
            "address2": "Apt 4",
            "country": "United States",
            "zipcode": "1235445",
            "state": "California",
            "city": "Los Angeles",
            "mobile_number": "1234567890"
        }
    ])
    def test_update_account(self, api_client, data):
        response = api_client.put("/updateAccount", data=data)
        response_json = response.json()
        assert response_json["responseCode"] == 200
        assert response_json["message"] == "User updated!"

    def test_get_user_details(self, api_client):
        payload= {"email":"update_get_details@example.com"}
        response = api_client.get("/getUserDetailByEmail", params=payload)
        response_json = response.json()
        print(response_json)
        assert response_json["responseCode"] == 200



