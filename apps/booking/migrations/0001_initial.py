# Generated by Django 3.2.13 on 2022-10-26 19:56

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
                ('price_adult', models.CharField(max_length=100, verbose_name='اعلى سعر')),
                ('price_children', models.CharField(max_length=100, verbose_name='اصغر سعر')),
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
                ('confirm', models.BooleanField(max_length=255, verbose_name='التاكيد')),
                ('state_name', models.CharField(max_length=255, verbose_name='اسم المدينة')),
                ('mobile1', models.CharField(max_length=255, verbose_name='الجوال1 ')),
                ('passport', models.CharField(max_length=255, verbose_name='رقم الجواز')),
                ('address', models.CharField(max_length=255, verbose_name='العنوان')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='الصورة')),
                ('status', models.CharField(max_length=255, verbose_name='الحالة الاجتماعيو')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_note', models.TextField(verbose_name='ملاحظة حالة الحجز')),
                ('no_of_adults', models.BooleanField(verbose_name='لا يوجد بالغين')),
                ('no_of_children', models.BooleanField(verbose_name='لا يوجد اطفال')),
                ('from_date', models.DateTimeField(verbose_name='من تاريخ')),
                ('to_date', models.DateTimeField(verbose_name='إلى تاريخ')),
                ('travel_from', models.CharField(max_length=255, verbose_name='السفر من')),
                ('travel_to', models.CharField(max_length=255, verbose_name='السفر إلى')),
                ('total_amount', models.CharField(max_length=255, verbose_name='اجمالي المبلغ')),
                ('adv_amount', models.CharField(max_length=255, verbose_name='المبلغ المدفوع')),
                ('total', models.CharField(max_length=255, verbose_name='الاجمالي النهائي')),
                ('tax', models.CharField(max_length=25, verbose_name='الضريبة')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.packages')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.state', verbose_name='حالة الحجز')),
                ('traveller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.travellers')),
            ],
            options={
                'ordering': ['traveller'],
            },
        ),
    ]
