import pytest
from fastapi.testclient import TestClient
from shorty.main import app



@pytest.mark.asyncio
@pytest.mark.parametrize('payload', [{'url': 'http://www.google.com'}])
async def test_short_links(payload):
    """
    J No Type hinting
    M No mocking on the client - actually reaching the provider
    M Only happy path
    J No testing of the return status
    J No checking of the actual response content
    """

    client = TestClient(app=app)
    response = client.post(url='/tiny_shortening', json=payload)
    assert response
