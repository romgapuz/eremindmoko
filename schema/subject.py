from schema.base import ma
from models.subject import Subject


class SubjectSchema(ma.ModelSchema):
    class Meta:
        model = Subject
