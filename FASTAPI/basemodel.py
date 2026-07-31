from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()
class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/")
def create_user(user: User):
    return {
        "success": True,
        "message": "User created successfully.",
        "data": user
    }

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        errors.append({
            "field": ".".join(str(x) for x in err["loc"][1:]),  # body -> name => name
            "message": err["msg"],
            "type": err["type"],
            "input": err.get("input")
        })

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "errors": errors
        }
    )

@app.get("/")
def root():
    return {"message": "Hello Alamin"}

@app.get("/alamin")
def read_alamin():
    return {"message": "Hello Alamin"}
