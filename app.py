from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title="REST API Users from NUTRIFIT",
    openapi_tags=tags_metadata
)

app.include_router(user)