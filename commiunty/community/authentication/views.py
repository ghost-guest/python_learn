from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import User
from .forms import SignUpForm
# Create your views here.

class UserSignupView(CreateView):
    """
    用户注册
    """
    model = User
    form_class = SignUpForm
    template_name = 'authentication/signup.html'
    def form_valid(self, form):
        '''
        保存并登陆用户，重定向主页
        '''
        user = form.save()
        login(self.request, user)
        return redirect("home")
        