from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count

from .models import Question, LoadForm

import csv

# Create your views here.
def index(request) :
    isFirst = True
#
#    if request.method == 'POST' :
#        form = LoadForm(request.POST)
#        if form.is_valid() :
#            ord = None
#    with open('raw.csv') as f:
#    reader = csv.reader('raw.csv')

    with open('raw.csv', 'r') as data_file:
        data = csv.reader(data_file, delimiter=',')
        for row in data:
            if isFirst:
                isFirst = False
                continue
            ord = Question(order_id = row[0],
                       user_id = row[1],
                       order_number = row[3],
                       order_dow = row[4],
                       order_hour_of_day = row[5],
                       days_since_prior_order = row[6],
                       product_id = row[7],
                       add_to_cart_order = row[8],
                       reordered = row[9],
                       product_name = row[10],
                       aisle_id = row[11],
                       department_id = row[12],
                       department = row[13],
                       aisle = row[14],
                       )
            ord.save()

        order_list = Question.objects.all()
        #    d = order_list.distinct("user_id")
        #    print(d)
        #    for order in order_list:
        #        if order not in d:
        #            order.delete()

        context = {
            'order_list': order_list
        }

        return render(request, 'polls/index.html', context)
#            order_list = Question.objects.all()
#            d = order_list.distinct('latitude', 'longitude')
#            for order in order_list.iterator():
'''          if ((ord.order_id == order.order_id) & (ord.user_id == order.user_id)):
            order.delete()
            continue'''
'''    duplicate_id = Question.objects.values('user_id').annotate(id_count=Count('user_id')).filter(id_count__gt=1)
    for data in duplicate_id:
        user_id = data['user_id']
        Question.objects.filter(user_id=user_id).order_by()[1:].delete()'''

#    d = order_list.distinct("user_id")
#    print(d)
#    for order in order_list:
#        if order not in d:
#            order.delete()

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

