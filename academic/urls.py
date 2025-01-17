from django.urls import path
from . import views


urlpatterns = [
    path('sessions/create/', views.session_list_create_update, name='session-list-create-update'),
    path('sessions/', views.session_list_create_update, name='session-list-create-update'),
    path('sessions/<int:pk>/update/', views.session_list_create_update, name='session-update'),
    path('sessions/<int:pk>/delete/', views.SessionDeleteView.as_view(), name='session-delete'),
]