from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    grade: int


class StudentResponse(BaseModel):
    student_id: int
