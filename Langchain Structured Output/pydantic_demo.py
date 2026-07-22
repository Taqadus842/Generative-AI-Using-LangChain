from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = "taqadus"
    age:Optional[int]=None
    email:EmailStr
    cgpa: float =Field(gt=0,lt=10)

new_student = Student(age=22,email='taqadus75@gmail.com',cgpa=3)

print(new_student.name)
print(new_student.age)
print(new_student.email)
print(new_student.cgpa)