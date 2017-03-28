from schema.base import ma
from models.exam import Exam


class ExamSchema(ma.ModelSchema):
    class Meta:
        model = Exam
