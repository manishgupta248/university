from django import forms
import academic.models as models
#from .models import (AcademicSession, Department, Program, 
#                    ProgramSemester, Course, Syllabus)

# Create Academic Session form
class AcademicSessionForm(forms.ModelForm):
    class Meta:
        model = models.AcademicSession
        fields = ['name', 'start_date', 'end_date', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
#=======================================================================
# Create Department form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['name', 'code', 'faculty']
        widgets = {
            'faculty': forms.Select(attrs={'class': 'form-control'}),
        }
#==========================================================================
class ProgramForm(forms.ModelForm):
    class Meta:
        model = models.Program
        fields =['name', 'duration', 'level', 'intake']
        widgets = {
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
        }
#========================================================================
class ProgramSemesterForm(forms.ModelForm):
    class Meta:
        model = models.ProgramSemester
        fields = ['program', 'session', 'semester']
        widgets = {
            'program': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
        }
 #==========================================================================
class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['name', 'code', 'credit', 'nature', 'type']
        widgets = {
            'credit': forms.Select(attrs={'class': 'form-control'}),
            'nature': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }       
#=============================================================================
class SyllabusForm(forms.ModelForm):
    class Meta:
        model = models.Syllabus
        fields = ['course', 'upload_syllabus']
        widgets = { 
            'course': forms.Select(attrs={'class': 'form-control'}), 
            'upload_syllabus': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
#======================================================================
class AllocateSubjectsForm(forms.Form):
    program_semester = forms.ModelChoiceField(queryset=models.ProgramSemester.objects.all(), label="Program Semester")
    subjects = forms.ModelMultipleChoiceField(
        queryset=models.Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Subjects",
        to_field_name="name"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subjects'].queryset = models.Course.objects.all()
        self.fields['subjects'].label_from_instance = lambda obj: f"{obj.name} ({obj.code})"
#==========================================================================================
        