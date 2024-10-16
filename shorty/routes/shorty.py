import logging
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from fastapi import Request
from shorty.clients import TinyUrlClient

logger = logging.getLogger(__name__)


shorty_router = APIRouter()

"""
Absence of docstrings is on purpose in the whole codebase
No typing annotation as well
No logging
"""

@shorty_router.post('/shorten_my_links')
async def shorten_link(request: Request):
    """
    Not following restFul naming conventions (resource/actions) in URL
    No Validation
    Wrong status codes
    No correct exception handling
    Lack of details
    Business logic in the router module
    """
    body = await request.json()
    if 'url' not in body:
        raise HTTPException(status_code=500)

    try:
        short_url = await short_the_url(body['url'])
    except:
        raise HTTPException(status_code=500)

    return JSONResponse({'short_url': short_url}, status_code=200)


async def short_the_url(url):
    """
    Shouldn't be here
    No error handling (what if data isn't here)
    """
    tiny_url_client = TinyUrlClient()
    shorten_url = tiny_url_client.shorten(url)
    return shorten_url['data']['tiny_url']