from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to DevOps Lab"}

@app.get("/hello")
def hello():
    return {"message": "Hello Students"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}