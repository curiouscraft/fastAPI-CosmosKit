from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.routes import router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()

# CORS settings
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    print(exc.errors())
    for error in exc.errors():
        error_detail = {"message": f'{error["loc"][1]} {error["msg"]}'}
        errors.append(error_detail)
    return JSONResponse(status_code=422, content=errors)

app.include_router(router)

