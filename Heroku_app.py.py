from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn


app = FastAPI()

# temp database
fakedb = []

# course model to store courses
class Course(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None

# Home/welcome route
@app.get("/")
def read_root():
    return 8

# Get all courses
@app.get("/courses")
def get_courses():
    return {"coding:" "python"}

# get single course
@app.get("/courses/{course_id}")
def get_a_course(course_id: int):
    course = course_id - 1
    return fakedb[course]

# add a new course
@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]

# delete a course
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fakedb.pop(course_id-1)
    return {"task": "deletion successful"}

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.40", port=8000)
