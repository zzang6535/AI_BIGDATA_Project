from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib import messages

from django.shortcuts import render
from django.urls import reverse
from django.db.models import Count

from .models import UserType

from .forms import LoginForm

import csv

# Create your views here.
def index(request) :
    if request.user.username and request.user.username != 'admin':
        Grade = UserType.objects.get(id=int(request.user.username))

        context = {
            'Grade': Grade
        }

        return render(request, 'polls/index.html', context)

    else :
        return render(request, 'polls/index.html')

def history(request) :
    li = request.POST.get("p")
    return render(request, 'polls/history.html')

def cart(request) :
    li = request.POST.get("p")

    return render(request, 'polls/cart.html')


# 로그인
class UserLoginView(LoginView):
    template_name = 'polls/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)

