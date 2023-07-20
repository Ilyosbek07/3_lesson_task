from django.db import models
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


week=[('Monday', 'Monday'),
      ('Tuesday', 'Tuesday'),
      ('Wednesday', 'Wednesday'),
      ('Thursday', 'Thursday'),
      ('Friday', 'Friday'),
      ('Saturday', 'Saturday'),
      ('Sunday', 'Sunday')]


class Position(models.Model):
    name = models.CharField(max_length=100)
class Responsibility(models.Model):
    task = models.CharField(max_length=400)

class Manager(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    work_days = MultiSelectField(choices=week, max_choices=2, max_length=50,blank=True,null=True)
    start_of_working_hours = models.TimeField()
    end_of_working_hours = models.TimeField()
    image = models.ImageField(upload_to='images_of_staff/')
    phone_number = PhoneNumberField()
    location = models.CharField(max_length=100)
    responsibilities = models.ManyToManyField(Responsibility)
    biography = RichTextField()

class Representative(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='images_of_staff/')
    phone_number = PhoneNumberField()
    description = models.TextField()

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images_of_volunteers/')
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    file = models.FileField(upload_to='resume_files_of_volunteers/')



# -------------------------------- --------------------------------


class WorkingType(models.Model):
    name = models.CharField(max_length=100)

class Salary(models.Model):
    cash = models.FloatField()
    currency = models.CharField(max_length=100)
    other = models.CharField(max_length=100)

class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    type = models.ForeignKey(WorkingType, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    salaries = models.ManyToManyField(Salary)
    description = RichTextField()

class Resume(models.Model):
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.DO_NOTHING)
    phone_number = PhoneNumberField()
    file = models.FileField(upload_to='resume_files/')



# -------------------------------- -----------------------------------

class Result(models.Model):
    in_numbers = models.IntegerField()
    year = models.IntegerField()
    time_interval = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='other_images/')

class SocialMediaPost(models.Model):
    link = models.URLField()
    image = models.ImageField(upload_to='images_of_social_media_posts/')
