import logging
from fastapi import FastAPI
from shorty.routes.shorty import shorty_router

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(shorty_router)



