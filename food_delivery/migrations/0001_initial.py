# Generated by Django 3.1.2 on 2020-11-04 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('order_done', models.BooleanField(default=False)),
                ('order_items', models.ManyToManyField(to='food_delivery.OrderItem')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_delivery.restaurant')),
            ],
        ),
    ]
