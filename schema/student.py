from schema.base import ma
from models.student import Student


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
