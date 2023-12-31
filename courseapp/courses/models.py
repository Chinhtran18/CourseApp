from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering =['-id']

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100, unique=True)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    class Meta:
        unique_together=('subject', 'category')

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='lessons/%Y/%m')
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag', blank=True, related_name='lessons')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject','course')

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



