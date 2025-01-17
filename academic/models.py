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