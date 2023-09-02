from fastapi import FastAPI
from inventory.api_router import v1_api_router

SWAGGER_UI_PARAMETERS = {
    "operationsSorter": "method",
    "defaultModelsExpandDepth": -1,
    "displayRequestDuration": True,
    "filter": True,
    "persistAuthorization": True,
    "syntaxHighlight.theme": "monokai"
}


app = FastAPI(swagger_ui_parameters=SWAGGER_UI_PARAMETERS)

app.include_router(v1_api_router)
