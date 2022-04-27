import pytest
import static.static as st
from core.http_methods import HttpMethod
from contract.user_contract import Contract


def test_sucess_create_new_user():
    body = Contract()
    response = HttpMethod.post(st.HOST, st.HEADER, body.get())
    
    assert response.status_code == 200

def test_error_create_new_user_invalid_id():
    body = Contract()
    response = HttpMethod.post(st.HOST, st.HEADER, body.get("error_id"))
    response_body = response.json()
    
    assert response.status_code == 500 and response_body["message"] == "something bad happened"

def test_consult_valid_user():
    body = Contract()
    url = f'{st.HOST}/{body.contract["username"]}'
    response = HttpMethod.get(url, st.HEADER)
    
    assert response.status_code == 200

def test_consult_invalid_user():
    url = f'{st.HOST}/{None}'
    response = HttpMethod.get(url, st.HEADER)
    response_body = response.json()
    
    assert response.status_code == 404 and response_body["message"] == "User not found"

def test_update_valid_user():
    body = Contract()
    url = f'{st.HOST}/{body.contract["username"]}'
    response = HttpMethod.put(url, st.HEADER, body.get())
    response_body = response.json()

    assert response.status_code == 200 and response_body["message"] == str(body.contract["id"])