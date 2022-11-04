from django import forms
from django.core import validators


from .models import (
    packages, 
    travellers,booking
    )
from django.urls import reverse,reverse_lazy
import datetime

class PackagesForm(forms.ModelForm):
    """
    customer Data Form for represent customer Data models in template
    """
    def __init__(self, *args, **kwargs):
        super(PackagesForm, self).__init__(*args, **kwargs)
        self.fields['pname'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'pname', 'placeholder': 'ادخل الحزمة'})
        self.fields['price_adult'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'pname', 'placeholder': 'اعلى قيمة'})
        self.fields['price_children'].widget.attrs.update(
            {'type': 'text', 'class': 'form-control', 'id': 'pname', 'placeholder': 'اقل قيمة'})
   
    class Meta:
        model = packages
        fields ="__all__"
     
            
 
class travellersForm(forms.ModelForm):
    """
    customer Data Form for represent customer Data models in template
    """
    def __init__(self, *args, **kwargs):
        super(travellersForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
                    {'type': 'text', 'class': 'form-control', 'id': 'name', 'placeholder': 'الاسم'})
        self.fields['email'].widget.attrs.update(
                    {'type': 'email', 'class': 'form-control', 'id': 'email', 'placeholder': 'البريد '})
        self.fields['confirm'].widget.attrs.update(
                    {"type":"checkbox",'class': 'form-check-input status', 'id': 'confirm', "checked":""})
        self.fields['state_name'].widget.attrs.update(
                    {'type': 'text', 'class': 'form-control', 'id': 'state_name', 'placeholder': 'اسم المدينة'})
        self.fields['mobile1'].widget.attrs.update(
                    {'type': 'text', 'class': 'form-control', 'id': 'mobile1', 'placeholder': 'رقم الجوال'})
        self.fields['passport'].widget.attrs.update(
                    {'type': 'text', 'class': 'form-control', 'id': 'passport', 'placeholder': 'رقم الجواز'})
        self.fields['address'].widget.attrs.update(
                    {'type': 'text', 'class': 'form-control', 'id': 'address', 'placeholder': 'العنوان'})
        self.fields['photo'].widget.attrs.update(
                    {'type': 'file', 'class': 'form-control', 'id': 'photo', 'placeholder': 'الصورة'})
        self.fields['status'].widget.attrs.update(
                    {'type': 'text', 'class': 'form-control', 'id': 'status', 'placeholder': 'حالة الطلب'})
   
    class Meta:
        model = travellers
        fields ="__all__"
   





class bookingForm(forms.ModelForm):
    """
    customer Data Form for represent customer Data models in template
    """
    def __init__(self, *args, **kwargs):
        super(bookingForm, self).__init__(*args, **kwargs)
        self.fields['traveller'].widget.attrs.update(  
            {'type': 'select', 'class': 'form-control', 'id': 'traveller', 'placeholder': 'اسم المسافر'})
        
        
        self.fields['travel_from'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'travel_from', 'placeholder': 'السفر من'})
        self.fields['travel_to'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'travel_to', 'placeholder': 'السفر إلى'})
        
        self.fields['state_note'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'state_note', 'placeholder': 'ملاحظة حالة الحجز'})
        self.fields['package'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'package', 'placeholder': 'الحزمة'})
        self.fields['no_of_adults'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'no_of_adults', 'placeholder': 'الا يمتلك نفقات خارجية'})
        self.fields['no_of_children'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'no_of_children', 'placeholder': 'لا يمتلك اطفال'})
        self.fields['from_date'].widget.attrs.update(  
            {'type': 'date', 'class': 'datepicker-dropdown form-control', 'id': 'from_date', 'placeholder': 'من تاريخ'})
        self.fields['to_date'].widget.attrs.update(  
            {'type': 'date', 'class': 'datepicker-dropdown form-control', 'id': 'to_date', 'placeholder': 'إلى تاريخ'})
        self.fields['total_amount'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'total_amount', 'placeholder': 'إجمالي المبلغ'})
        self.fields['adv_amount'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'adv_amount', 'placeholder': 'المبلغ المدفوع'})
        self.fields['tax'].widget.attrs.update(  
            {'type': 'number', 'class': 'form-control', 'id': 'tax', 'placeholder': 'الضريبة'})
        self.fields['total'].widget.attrs.update(  
            {'type': 'text', 'class': 'form-control', 'id': 'total', 'placeholder': 'الإجمالي النهائي'})
    class Meta:
        model = booking
        fields ="__all__"
  