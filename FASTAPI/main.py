from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Alamin"}

@app.get("/alamin")
def read_alamin():
    return {"message": "Hello Alamin"}

@app.get("/alamin/{name}")
def read_alamin_name(name: str):
    return {"message": f"Hello {name}"}