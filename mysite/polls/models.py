from django.db import models
from django import forms

# Create your models here.
class Question(models.Model) :
    order_id = models.IntegerField()
    user_id = models.IntegerField()
    order_number = models.IntegerField()
    order_dow = models.IntegerField()
    order_hour_of_day = models.IntegerField()
    days_since_prior_order = models.IntegerField()
    product_id = models.IntegerField()
    add_to_cart_order = models.IntegerField()
    reordered = models.BooleanField()
    product_name = models.CharField(max_length = 200)
    aisle_id = models.IntegerField()
    department_id = models.IntegerField()
    department = models.CharField(max_length = 200)
    aisle = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.order_id)


class LoadForm(forms.Form) :
    filename = forms.CharField(label = 'filename', max_length = 100)
