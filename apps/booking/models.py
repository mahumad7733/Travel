# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
import datetime
class state(models.Model):
    name_state= models.CharField("اسم الحالة", max_length=20)
    def __str__(self):
        return str(self.pk)+"-"+self.name_state  
class packages(models.Model):
    pname= models.CharField("pname",max_length=100) 
    price_adult= models.CharField("اعلى سعر",max_length=100) 
    price_children= models.CharField("اصغر سعر",max_length=100) 
    def __str__(self):
        return self.pname


class travellers(models.Model):
    name= models.CharField( "الاسم ",max_length=255)
    email= models.CharField( "الايميل",max_length=255)
    confirm= models.BooleanField( "التاكيد",max_length=255)
    state_name= models.CharField( "اسم المدينة",max_length=255)
    mobile1= models.CharField( "الجوال1 ",max_length=255)
    passport = models.CharField( "رقم الجواز",max_length=255)
    address= models.CharField( "العنوان",max_length=255)
    photo= models.ImageField( "الصورة",blank=True,null=True)
    status= models.CharField( "الحالة الاجتماعي",max_length=255)
    def __str__(self):
        return ""+self.name
    class Meta:
        ordering = ['name']

# Create your models here.
class booking(models.Model):
    traveller= models.ForeignKey(travellers,on_delete=models.CASCADE)  
    state_note= models.TextField("ملاحظة حالة الحجز")
    package= models.ForeignKey(packages,on_delete=models.CASCADE)
    no_of_adults= models.BooleanField(verbose_name="لا يوجد بالغين")  
    no_of_children= models.BooleanField(verbose_name="لا يوجد اطفال")  
    from_date= models.DateTimeField("من تاريخ") 
    to_date= models.DateTimeField("إلى تاريخ")
    travel_from= models.CharField("السفر من",max_length=255)
    travel_to= models.CharField("السفر إلى",max_length=255)
    total_amount= models.CharField("اجمالي المبلغ",max_length=255)  
    adv_amount= models.CharField("المبلغ المدفوع",max_length=255)
    total= models.CharField("الاجمالي النهائي",max_length=255)  
    tax= models.CharField("الضريبة",max_length=25)  
    state= models.ForeignKey(state,on_delete=models.CASCADE,verbose_name="حالة الحجز")
    created_at= models.DateField("Created",null=True,auto_now_add=True)   
    def __str__(self):
        return ""+self.state_note
    class Meta:
        ordering = ['traveller']

# public website
class destination(models.Model):
    name_dist = models.CharField("الوجهات",max_length=50)
    image_file = models.ImageField("الصورة",upload_to='images')
    image_url = models.URLField()

