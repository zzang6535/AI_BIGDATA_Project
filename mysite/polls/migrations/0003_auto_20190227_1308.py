# Generated by Django 2.1.7 on 2019-02-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_aisle_association_orders_products_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=200)),
                ('aisle_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
