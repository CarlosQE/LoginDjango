from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
