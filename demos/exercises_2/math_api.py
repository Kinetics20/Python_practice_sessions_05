from fastapi import FastAPI, HTTPException
from math import sin, cos, pow

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Math API"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}

@app.get("/power")
def power(base: float, exponent: float):
    return {"result": pow(base, exponent)}

@app.get("/sin")
def sine(angle_degrees: float):
    from math import radians
    angle_radians = radians(angle_degrees)
    return {"result": sin(angle_radians)}

@app.get("/cos")
def cosine(angle_degrees: float):
    from math import radians
    angle_radians = radians(angle_degrees)
    return {"result": cos(angle_radians)}
