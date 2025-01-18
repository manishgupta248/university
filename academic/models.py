from django.db import models

# Create your models here.

# Create Academic Session model
class AcademicSession(models.Model):
    name = models.CharField(max_length=20, unique=True) # e.g. 2022_23_odd_semester
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
 
# Create Academic Department Model    
class Department(models.Model):
    FACULTY_CHOICES = [
        ('E&t', 'Engineering & Technology'),
        ('I&C', 'Informatic & Computing'),
        ('Sc', 'Science'),
        ('MAGT', 'Management Studies'),
        ('LMS', 'Languages & Media Studies'),
        ('LS', 'Life Sciences'),
        ('IS', 'Intrdisciplinary Studies'),
        ('CCSD', 'Community College for Skill Development'),
        ('OTHER', 'Others'),
    ]
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    faculty = models.CharField(max_length=10, choices=FACULTY_CHOICES, default='OTHER')

    def __str__(self):
        return self.name