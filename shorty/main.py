import logging

from fastapi import FastAPI

from shorty.routes.shorty import shorty_router
from shorty.routes.healthcheck import healthcheck_router


logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(healthcheck_router)
app.include_router(shorty_router)



