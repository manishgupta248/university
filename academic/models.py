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
#===================================================================================== 
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
#================================================================================
class Program(models.Model):
    LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('PhD', 'Doctoral'),
        ('PGD', 'Post Graduate Diploma'),
        ('DIP', 'Diploma'),
        ('CRT', 'Certificate'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 7)])
    level = models.CharField(max_length=6, choices=LEVEL_CHOICES, default='UG')
    intake = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
#=================================================================================
class ProgramSemester(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='semesters')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='semesters')
    semester = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 9)])
    class Meta: 
        unique_together = ('program', 'semester', 'session') 
    def __str__(self): 
        return f"{self.program.name} - Semester - {self.semester} ({self.session.name} )"
#=========================================================================================
class Course(models.Model):
    NATURE_CHOICES = [
        ('Theory', 'Theory'),
        ('Lab', 'Lab'),
        ('Project', 'Project'),
        ('Seminar', 'Seminar'),
        ('Workshop', 'Workshop'),
        ('Training', 'Training'),
        ('Other', 'Other'),
    ]
    TYPE_CHOICES =[
        ('DS','Dicipline Specific'),
        ('AEC','Ability Enhancement Course'),
        ('VAC','Value Added Course'),
        ('Elective','Value Added Course'),
        ('Other','Other'),
    ]
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    credit = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(0, 21)])
    nature = models.CharField(max_length=8, choices=NATURE_CHOICES, default='Theory')
    type = models.CharField(max_length=12, choices=TYPE_CHOICES, default='DS')
    program_semesters = models.ManyToManyField(ProgramSemester, related_name='subjects', blank=True)

    def __str__(self):
        return self.name