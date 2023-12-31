from django.db import models
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class NewsCategory(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class NewsTag(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=125)
    picture = models.ImageField()
    description = RichTextField()
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.DO_NOTHING,
        related_name='category'
    )
    tag = models.ManyToManyField(
        NewsTag,
        related_name='news_tag'
    )


class UserDevice(models.Model):
    device_id = models.CharField(max_length=55)
    news_id = models.ForeignKey(
        News,
        on_delete=models.CASCADE
    )


class FAQTag(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    name = models.CharField(max_length=125)
    phone = PhoneNumberField()
    message = models.TextField()
    tag = models.ForeignKey(
        FAQTag,
        on_delete=models.CASCADE,
        related_name='faq_tag'
    )

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=125)
    phone = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=125)
    phone = PhoneNumberField()
    email = models.EmailField()
    occupation = models.CharField(max_length=125)
    description = RichTextField()
    work_time = models.CharField(max_length=125)
    instagram = models.URLField()
    def __str__(self):
        return self.name
