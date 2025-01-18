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
