# Generated by Django 3.2.13 on 2022-10-23 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='booking',
        ),
        migrations.DeleteModel(
            name='packages',
        ),
        migrations.DeleteModel(
            name='state',
        ),
        migrations.DeleteModel(
            name='travellers',
        ),
    ]
