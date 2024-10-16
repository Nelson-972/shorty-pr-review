from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status


healthcheck_router = APIRouter()


@healthcheck_router.get('/healthcheck')
def healthcheck():
    return JSONResponse({'status': 'OK'}, status_code=status.HTTP_200_OK)