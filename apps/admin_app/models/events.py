from django.db import models
from ckeditor.fields import RichTextField

class EventType(models.Model):
    name = models.CharField(max_length=300)

class Event(models.Model):
    title = models.CharField(max_length=100)
    event_type = models.ForeignKey("admin_app.EventType", on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    description = RichTextField()
    image = models.ImageField(upload_to='event_images/')
    video = models.FileField(upload_to='event_videos/')
    view_count = models.IntegerField(default=0)

