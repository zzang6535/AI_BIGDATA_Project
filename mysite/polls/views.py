from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib import messages

from django.shortcuts import render
from django.urls import reverse
from django.db.models import Count

from .models import UserType, Products, Basket

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
        if len(Products.objects.all()) == 0:
            p_first = True
            with open('grocery_products.csv') as f:
                prd = None
                i = 0
                reader = csv.reader(f)
                for row in reader:
                    if p_first:
                        p_first = False
                        continue
                    prd = Products(product_id=row[0],
                                   product_name=row[1],
                                   aisle_id=row[2],
                                   department_id=row[3])
                    prd.save()
                    i += 1
                    if i == 20:
                        break

        product_list = Products.objects.order_by()
        context = {
            "product_list": product_list
        }
        return render(request, 'polls/index.html', context)

def history(request) :
    li = request.POST.get("p")
    return render(request, 'polls/history.html')

def cart(request) :
    if request.POST:

        form = request.POST['product_id']
    #temp = Products.objects.filter(product_id = form.data.get('field'))
        temp = Products.objects.get(product_id = int(form))
    #temp = get_object_or_404(Products, product_id = form.data.get('field'))
        bsk = Basket(user_id=temp.product_id,
                     product_id=temp.product_id,
                     product_name=temp.product_name,
                     aisle_id=temp.aisle_id)
        bsk.save()
    basket_list = Basket.objects.order_by()
    context = {
        "basket_list": basket_list
    }
    return render(request, 'polls/cart.html',context)

def product(request):
    product_list = Products.objects.order_by()
    context = {
        'product_list' : product_list
    }
    return render(request, 'polls/list.html', context)

# 로그인
class UserLoginView(LoginView):
    template_name = 'polls/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)

