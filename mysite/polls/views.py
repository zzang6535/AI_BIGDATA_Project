from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib import messages

from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Count

from .models import Question
from .forms import LoginForm, LoadForm

import csv

# Create your views here.
def index(request) :
    order_list = Question.objects.all()

    context = {
        'order_list': order_list
    }

    return render(request, 'polls/index.html', context)

def history(request) :
    order_list = Question.objects.order_by()
    context = {
        'order_list': order_list,
    }
    return render(request, 'polls/index.html', context)

def cart(request) :
    li = request.POST.get("p")
    order_list = Question.objects.order_by()
    context = {
        'order_list': order_list,
        'li' : li,
    }
    return render(request, 'polls/cart.html', context)


# 회원가입
class UserRegistrationView(CreateView):
    model = get_user_model()
    # form_class = UserRegistrationForm
    success_url = '/article/'


# 로그인
class UserLoginView(LoginView):
    template_name = 'polls/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)

