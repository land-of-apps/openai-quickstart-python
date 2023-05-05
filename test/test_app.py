# Run with: pytest -v
# See: https://docs.pytest.org/en/latest/usage.html#cmdline

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test to make a POST request to flask route / with form data animal='small dog'
# and assert that the response is a redirect to /?result=.
def test_index(client):
    response = client.post("/", data={"animal": "small dog"})
    assert response.status_code == 302
    assert response.headers["Location"].startswith("http://localhost/?result=")

# Test to make a GET request to flask route / with query param result='El Diablo'
# and assert that the response is a rendered template with the result variable
# set to 'El Diablo'.
def test_index_result(client):
    response = client.get("/?result=El Diablo")
    assert response.status_code == 200
    assert b"El Diablo" in response.data

