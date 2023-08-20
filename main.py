from fastapi import FastAPI

SWAGGER_UI_PARAMETERS = {
    "operationsSorter": "method",
    "defaultModelsExpandDepth": -1,
    "displayRequestDuration": True,
    "filter": True,
    "persistAuthorization": True,
    "syntaxHighlight.theme": "monokai"
}


app = FastAPI(swagger_ui_parameters=SWAGGER_UI_PARAMETERS)


@app.get("/")
async def root():
    return {"message": "hello world"}
