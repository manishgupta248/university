from django import forms
from .models import AcademicSession, Department, Program, ProgramSemester

# Create Academic Session form
class AcademicSessionForm(forms.ModelForm):
    class Meta:
        model = AcademicSession
        fields = ['name', 'start_date', 'end_date', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
#=======================================================================
# Create Department form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code', 'faculty']
        widgets = {
            'faculty': forms.Select(attrs={'class': 'form-control'}),
        }
#==========================================================================
class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields =['name', 'duration', 'level', 'intake']
        widgets = {
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
        }
#========================================================================
class ProgramSemesterForm(forms.ModelForm):
    class Meta:
        model = ProgramSemester
        fields = ['program', 'session', 'semester']
        widgets = {
            'program': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
        }
        


        