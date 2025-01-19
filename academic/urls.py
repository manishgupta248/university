from django.urls import path
from . import views


urlpatterns = [
    path('sessions/create/', views.session_list_create_update, name='session-list-create-update'),
    path('sessions/', views.session_list_create_update, name='session-list-create-update'),
    path('sessions/<int:pk>/update/', views.session_list_create_update, name='session-update'),
    path('sessions/<int:pk>/delete/', views.SessionDeleteView.as_view(), name='session-delete'),
    #------------------------------------------
    path('departments/', views.department_list_create_update, name='department-list-create-update'),
    path('departments/create/', views.department_list_create_update, name='department-list-create-update'),
    path('departments/<int:pk>/update/', views.department_list_create_update, name='department-update'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),
    #----------------------------------------------------
    path('programs/', views.program_list_create_update, name='program-list-create-update'),
    path('programs/create/', views.program_list_create_update, name='program-list-create-update'),
    path('programs/<int:pk>/update/', views.program_list_create_update, name='program-update'),
    path('programs/<int:pk>/delete/', views.ProgramDeleteView.as_view(), name='program-delete'),
    #--------------------------------------------------------
    path('program_semester/', views.program_semester_list_create_update, name='program-semester-list-create-update'),
    path('program_semester/create/', views.program_semester_list_create_update, name='program-semester-list-create-update'),
    path('program_semester/<int:pk>/update/', views.program_semester_list_create_update, name='program-semester-update'),
    path('program_semester/<int:pk>/delete/', views.ProgramSemesterDeleteView.as_view(), name='program-semester-delete'),
    #----------------------------------------------------------------
    path('courses/', views.course_list_create_update, name='course-list-create-update'),
    path('courses/create/', views.course_list_create_update, name='course-list-create-update'),
    path('courses/<int:pk>/update/', views.course_list_create_update, name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),
    #---------------------------------------------------------------------
    path('syllabus/', views.syllabus_list_create_update, name='syllabus-list-create-update'),
    path('syllabus/create/', views.syllabus_list_create_update, name='syllabus-list-create-update'),
    path('syllabus/<int:pk>/update/', views.syllabus_list_create_update, name='syllabus-update'),
    path('syllabus/<int:pk>/delete/', views.SyllabusDeleteView.as_view(), name='syllabus-delete'),
    #--------------------------------------------------------------------
    path('allocate_subjects/', views.allocate_subjects, name='allocate-subjects'),


]