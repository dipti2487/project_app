from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    comment=models.TextField()

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    DEVOPS='DEV'
    PYTHON='PY'
    DJANGO='DJ'
    REACT_JS='RJ'
    JAVASCRIPT='JS'
    SELECT_COURSES_CHOICES=[
    (DEVOPS, 'devops'),
    (PYTHON, 'python'),
    (DJANGO, 'django'),
    (REACT_JS, 'react_js'),
    (JAVASCRIPT, 'javascript'),
    ]
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length = 254)
    password=models.CharField(('password'), max_length=128, help_text = "Please enter valid password.")
    select_courses=models.CharField(max_length=10, choices=SELECT_COURSES_CHOICES, default=DEVOPS, null=True, blank=True)

    def __str__(self):
        return self.select_courses
