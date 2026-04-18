from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    course: str
    active: bool

app = FastAPI()

@app.get("/")
async def root():
    return "Hello World!"

@app.get("/students/{student_id}")
async def register_student(student_id: int):
    return student_id
