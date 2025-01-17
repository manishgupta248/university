from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, LoginView, CustomPasswordChangeView, UserUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'), 
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
]
