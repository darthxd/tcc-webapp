from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    rm = models.CharField(max_length=5)
    birthdate = models.DateField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    biometry = models.CharField(max_length=5, blank=True)
    is_in_school = models.BooleanField(default=False)