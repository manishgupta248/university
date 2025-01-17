from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from .forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, self.template_name, {'form': form})
    
class CustomPasswordChangeView(PasswordChangeView): 
    success_url = reverse_lazy('password_change_done') 
    template_name = 'registration/password_change.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['email', 'mobile_number']
    template_name = 'registration/update_user.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

