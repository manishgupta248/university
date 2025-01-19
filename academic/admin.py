from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
import academic.models as models

# Register your models here.

class AcademicSessionResource(resources.ModelResource):
    class Meta:
        model = models.AcademicSession

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = models.Department

class ProgramResource(resources.ModelResource):
    class Meta:
        models = models.Program

class ProgramSemesterResource(resources.ModelResource):
    class Meta:
        models = models.ProgramSemester

class CourseResource(resources.ModelResource):
    class Meta:
        models = models.Course

class SyllabusResource(resources.ModelResource):
    class Meta:
        models = models.Syllabus

@admin.register(models.AcademicSession)
class AcademicSessionAdmin(ImportExportModelAdmin):
    resource_class = AcademicSessionResource
    list_display = ('name', 'is_active', 'start_date', 'end_date')
    search_fields = ('name', 'is_active')
    list_filter = ('is_active', 'start_date', 'end_date')
    ordering = ('-name',)

@admin.register(models.Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
    list_display = ('name', 'code', 'faculty')
    search_fields = ('name', 'code', 'faculty')
    list_filter = ('faculty',)
    ordering = ('name',)

@admin.register(models.Program)
class ProgramAdmin(ImportExportModelAdmin):
    resource_class = ProgramResource
    list_display = ('name', 'duration', 'level', 'intake')
    search_fields = ('name',  'duration', 'level', 'intake')
    list_filter = ('level',)
    ordering = ('level',)

@admin.register(models.ProgramSemester)
class ProgramSemesterAdmin(ImportExportModelAdmin):
    resource_class = ProgramSemesterResource
    list_display = ('program', 'semester', 'session')
    search_fields = ('program', 'semester', 'session')
    list_filter = ('program', 'semester', 'session',)
    ordering = ('program',)

@admin.register(models.Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    list_display = ('name', 'code', 'type', 'credit', 'nature')
    search_fields = ('name', 'code', 'type', 'credit', 'nature')
    list_filter = ('type', 'credit', 'nature',)
    ordering = ('code',)

@admin.register(models.Syllabus)
class SyllabusAdmin(ImportExportModelAdmin):
    resource_class = SyllabusResource
    list_display = ('course', 'upload_syllabus', 'updated_at')
