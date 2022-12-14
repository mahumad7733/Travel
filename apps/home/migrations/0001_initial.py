# Generated by Django 3.2.13 on 2022-10-23 20:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100, verbose_name='pname')),
                ('price_adult', models.CharField(max_length=100, verbose_name='price_adult')),
                ('price_children', models.CharField(max_length=100, verbose_name='price_children')),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_state', models.CharField(max_length=20, verbose_name='اسم الحالة')),
            ],
        ),
        migrations.CreateModel(
            name='travellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم ')),
                ('email', models.CharField(max_length=255, verbose_name='الايميل')),
                ('confirm', models.CharField(max_length=255, verbose_name='التاكيد')),
                ('state_name', models.CharField(max_length=255, verbose_name='اسم المدينة')),
                ('mobile', models.CharField(max_length=255, verbose_name='الجوال2')),
                ('address', models.CharField(max_length=255, verbose_name='العنوان')),
                ('photo', models.CharField(max_length=255, verbose_name='الصورة')),
                ('status', models.CharField(max_length=255, verbose_name='الحالة الاجتماعيو')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_adults', models.BooleanField(verbose_name='لا يوجد بالغين')),
                ('no_of_children', models.BooleanField(verbose_name='لا يوجد اطفال')),
                ('from_date', models.DateTimeField(verbose_name='من تاريخ')),
                ('to_date', models.DateTimeField(verbose_name='إلى تاريخ')),
                ('total_amount', models.CharField(max_length=255, verbose_name='اجمالي المبلغ')),
                ('adv_amount', models.CharField(max_length=255, verbose_name='المبلغ المدفوع')),
                ('total', models.CharField(max_length=255, verbose_name='الاجمالي النهائي')),
                ('tax', models.CharField(max_length=25, verbose_name='الضريبة')),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 10, 23, 23, 40, 25, 301150))),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.packages')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.state')),
                ('traveller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.travellers')),
            ],
        ),
    ]
