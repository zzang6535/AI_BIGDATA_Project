from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib import messages

from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Question
from .forms import LoginForm, LoadForm

import csv

# Create your views here.
def index(request) :
    order_list = Question.objects.order_by()
    context = {
        'order_list': order_list,
    }
    return render(request, 'polls/index.html', context)

def load(request) :
    isFirst = True

    if request.method == 'POST' :
        form = LoadForm(request.POST)
        if form.is_valid() :
            ord = None
        with open(form.data['filename']) as f:
                reader = csv.reader(f)
                for row in reader:
                    if isFirst:
                        isFirst = False
                        continue

                    ord = Question(order_id=row[0],
                                   user_id=row[1],
                                   order_number=row[3],
                                   order_dow=row[4],
                                   order_hour_of_day=row[5],
                                   days_since_prior_order=row[6],
                                   product_id=row[7],
                                   add_to_cart_order=row[8],
                                   reordered=row[9],
                                   product_name=row[10],
                                   aisle_id=row[11],
                                   department_id=row[12],
                                   department=row[13],
                                   aisle=row[14])

                    ord.save()

    return render(request, 'polls/index.html')


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

