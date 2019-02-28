from django.db import models

# Create your models here.

class Products(models.Model) :
    product_id = models.IntegerField()
    product_name = models.CharField(max_length = 200)
    aisle_id = models.IntegerField()
    department_id = models.IntegerField()

class UserType(models.Model):
    user_id = models.IntegerField()
    user_grade = models.IntegerField()

class Aisle(models.Model):
    aisle_id = models.IntegerField()
    aisle = models.CharField(max_length = 200)

class Orders(models.Model):
    order_id = models.IntegerField()
    user_id = models.IntegerField()
    order_number = models.IntegerField()
    order_dow = models.IntegerField()
    order_hour_of_day = models.IntegerField()
    days_since_prior_order = models.IntegerField()

class Basket(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    aisle_id = models.IntegerField()

class History(models.Model):
    user_id = models.IntegerField()
    product_name = models.CharField(max_length=200)


class Association(models.Model):
    aisle_id = models.IntegerField()
    user_pick = models.CharField(max_length = 200)
    recommend_id = models.IntegerField()
    recommend = models.CharField(max_length = 200)