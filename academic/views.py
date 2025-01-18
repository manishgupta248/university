from django.shortcuts import render, redirect
from .models import AcademicSession, Department, Program, ProgramSemester, Course
from .forms import AcademicSessionForm, DepartmentForm, ProgramForm, ProgramSemesterForm, CourseForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView, DetailView
from django.urls import reverse_lazy

# Create your views here.
def session_list_create_update(request, pk=None):
    if pk:
        academic_session = get_object_or_404(AcademicSession, pk=pk)
    else:
        academic_session = None

    if request.method == 'POST':
        if academic_session:
            form = AcademicSessionForm(request.POST, instance=academic_session)
        else:
            form = AcademicSessionForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('session-list-create-update')

    else:
        if academic_session:
            form = AcademicSessionForm(instance=academic_session)
        else:
            form = AcademicSessionForm()

    academic_sessions = AcademicSession.objects.all()
    return render(request, 'academic/session_list_create_update.html', {'form': form, 'academic_sessions': academic_sessions, 'edit_academic_session': academic_session})

class SessionDeleteView(DeleteView):
    model = AcademicSession
    template_name = "academic/session_delete.html"
    success_url = reverse_lazy('session-list-create-update')

#=======================================================================================S
def department_list_create_update(request, pk=None):
    if pk:
        department = get_object_or_404(Department, pk=pk)
    else:
        department = None

    if request.method == 'POST':
        if department:
            form = DepartmentForm(request.POST, instance=department)
        else:
            form = DepartmentForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('department-list-create-update')

    else:
        if department:
            form = DepartmentForm(instance=department)
        else:
            form = DepartmentForm()

    departments = Department.objects.all()
    return render(request, 'academic/department_list_create_update.html', {'form': form, 'departments': departments, 'edit_department': department})  

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "academic/department_delete.html"
    success_url = reverse_lazy('department-list-create-update')  
#===================================================================================
def program_list_create_update(request, pk=None):
    if pk:
        program = get_object_or_404(Program, pk=pk)
    else:
        program = None

    if request.method == 'POST':
        if program:
            form = ProgramForm(request.POST, instance=program)
        else:
            form = ProgramForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('program-list-create-update')

    else:
        if program:
            form = ProgramForm(instance=program)
        else:
            form = ProgramForm()

    programs = Program.objects.all()
    return render(request, 'academic/program_list_create_update.html', {'form': form, 'programs': programs, 'edit_department': program})  

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "academic/program_delete.html"
    success_url = reverse_lazy('program-list-create-update') 
#====================================================================================
def program_semester_list_create_update(request, pk=None):
    if pk:
        program_semester = get_object_or_404(ProgramSemester, pk=pk)
    else:
        program_semester = None

    if request.method == 'POST':
        if program_semester:
            form = ProgramSemesterForm(request.POST, instance=program_semester)
        else:
            form = ProgramSemesterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('program-semester-list-create-update')

    else:
        if program_semester:
            form = ProgramSemesterForm(instance=program_semester)
        else:
            form = ProgramSemesterForm()

    program_semesters = ProgramSemester.objects.all()
    return render(request, 'academic/program_semester_list_create_update.html', {'form': form, 'program_semesters': program_semesters, 'edit_program_semester': program_semester})

class ProgramSemesterDeleteView(DeleteView):
    model = ProgramSemester
    template_name = "academic/program_semester_delete.html"
    success_url = reverse_lazy('program-semester-list-create-update')
#====================================================================================
def course_semester_list_create_update(request, pk=None):
    if pk:
        course = get_object_or_404(Course, pk=pk)
    else:
        course = None

    if request.method == 'POST':
        if course:
            form = CourseForm(request.POST, instance=course)
        else:
            form = CourseForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('course-list-create-update')

    else:
        if course:
            form = CourseForm(instance=course)
        else:
            form = CourseForm()

    courses = Course.objects.all()
    return render(request, 'academic/course_list_create_update.html', {'form': form, 'courses': courses, 'edit_course': course})

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "academic/course_delete.html"
    success_url = reverse_lazy('course-list-create-update')
