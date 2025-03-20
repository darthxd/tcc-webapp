from django.db import models

courses = (
    ('DS','Desenvolvimento de sistemas'),
    ('DDI','Design de interiores'),
    ('MEC','Mecânica'),
    ('CV','Comunicações visuais'),
    ('QUI','Química'),
    ('MAT','Médio/Matemática'),
    ('BIO','Médio/Biologia'),
    ('DG','Design gráfico'),
    ('ADM','Administração'),
    ('EDF','Edificações'),
    ('LOG','Logística')
)

grades = (
    ('1Y','1° Ano'),
    ('2Y','2° Ano'),
    ('3Y','3° Ano')
)

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    rm = models.CharField(max_length=5)
    birthdate = models.DateField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    student_course = models.CharField(max_length=3,choices=courses)
    student_grade = models.CharField(max_length=2,choices=grades)
    photo = models.ImageField(upload_to="img/", blank=True)
    biometry = models.CharField(max_length=5, blank=True)
    is_in_school = models.BooleanField(default=False)