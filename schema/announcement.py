from schema.base import ma
from models.announcement import Announcement


class AnnouncementSchema(ma.ModelSchema):
    class Meta:
        model = Announcement
