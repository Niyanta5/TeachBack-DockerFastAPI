from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from schemas import StudentResponse, Student

app = FastAPI()


students = []


@app.post("/students/", response_model=StudentResponse)
def create_student(student: Student):
    global students
    next_student_id = len(students) + 1
    students.append(
        {
            "student_id": next_student_id,
            "name": student.name,
            "age": student.age,
            "grade": student.grade,
        }
    )

    return {"student_id": next_student_id}


@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    for student in students:
        if student["student_id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/students/", response_model=List[Student])
def read_students():
    return students
