import logging
import requests
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from fastapi import Request

logger = logging.getLogger(__name__)
shorty_router = APIRouter()


@shorty_router.post('/tiny_shortening')
async def shorten_link(request: Request):
    """
    S No async support
    J No docstring
    J No logging
    M Not following restFul naming conventions (resource/actions) in URL + coupling with provider
    J No input validation
    J Passing body directly from the request
    J Wrong status codes
    J Secret commited and not hidden
    J No correct exception handling
    M Leak in exception details
    M Lack of details in some exceptions for validation
    M Business logic in the router module
    J No response validation
    J Headers and Body in the same code
    M No abstraction of the http client
    M No code organisation
    M No type hinting
    """
    body = await request.json()

    if 'url' not in body:
        raise HTTPException(status_code=500)

    try:
        headers = {'Authorization': 'Bearer 7Mouwis7Xz5zml4XU63pvDuzYIOJrLyWvV8LTLSDBkimeA9eU5zTJ4z1FYBI'}
        session = requests.Session()
        response = session.post('https://api.tinyurl.com/create', json=body, headers=headers)
        return JSONResponse({'short_url': response.json()['data']['tiny_url']}, status_code=200)

    except:
        raise HTTPException(
            status_code=500,
            detail=f'Tiny URL call failed. With following details headers={headers}, body={body}'
        )
