# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView,CreateView,View,UpdateView,DeleteView
from django.urls import reverse
from django.db.models import Q ,Max
from django.http import QueryDict
from django.shortcuts import get_object_or_404

from django_datatables_view.base_datatable_view import BaseDatatableView 

from django.contrib import messages
from django.db.models import Subquery
from django.db import connection
from django.forms import modelformset_factory
from django.db.models import F
from django.db import transaction, IntegrityError

from django.utils.html import format_html
from django.views.decorators.csrf import csrf_protect
from .models import (packages, travellers  ,booking   )
from .forms import (
   PackagesForm, travellersForm,bookingForm
)  





################# Start PackageView Data View ##############
class PackageView(CreateView):
    """
    Outgoing Order Type View for create new Outgoing Order Type
    """
    def get(self, request, *args, **kwargs):
        
        context = {
            'form': '',
            'url': '',
            'title_form': _('packages '),
            'title_list': _('packages'),
            }
       
        if 'id' in request.GET.keys():
            if request.GET.get('id'):
                try:
                    data=packages.objects.filter(pk=request.GET.get('id'))
                    

                    result={'status':1,'data':serializers.serialize('json',data)}
                except:
                   pass
            else:
                
                result={'status':0,'data':''}
            return JsonResponse(result)
        else:
            
            context = {
                'form': PackagesForm(),
                'url': reverse('packages'),
                'title_form': _('packages'),
                'title_list': _('packages'),
                }
            

            return render(request, 'booking/packages.html', context)

    def post(self, request, *args, **kwargs):
        form = PackagesForm(request.POST)
        if request.POST.get('id'):
            data=get_object_or_404(packages,pk=int(request.POST.get('id')))
            form=PackagesForm(request.POST,instance=data)

        if form.is_valid():
           
            obj = form.save()
            obj.save()
            if request.POST.get('id'):
                if obj.id:
                    msg="تم التعديل بنجاح"
                    result={'status':1,'message':msg}
                else:
                    msg="هناك خطاء"
                    result={'status':2,'message':msg}
            else:
                if obj.id:
                    msg="تم الحفظ بنجاح"
                    result={'status':1,'message':msg}
                else:
                    msg="هناك خطاء"
                    result={'status':2,'message':msg}
        else:
            result={'status':0,'error':form.errors.as_json()}
        return JsonResponse(result)
          
    def delete(self, request,*args, **kwargs):
        pk=int(QueryDict(request.body).get('id'))
        if pk:
            try:
                data=get_object_or_404(packages,pk=pk)
                data.delete()
                msg=message.delete_successfully()
                result={'status':1,'message':msg}
            except:
                msg=message.delete_error()
                result={'status':0,'message':msg}
        else:
            msg=message.delete_error()
            result={'status':0,'message':msg}
        return JsonResponse(result)

################# End PackageView Data View ##############

################# Satrt Customer Data List Json ##############
class packagesJson(BaseDatatableView):
    """List Customer Groups
    Returns:
        [json] --
    """
    model = packages
    columns = [
        'id',  
        "pname",
        "price_adult",
        "price_children",
        'action',
        
    ]
    order_columns = [
        'id',  
        "pname",
        "price_adult",
        "price_children",
        'action',
 
    ]
    
    count = 0
    def get_initial_queryset(self):
        
        return self.model.objects.all()
        
        
    def render_column(self, row, column):
        """Render Column For Datatable
        """
        if column == "id":
            self.count += 1
            return self.count

        if column == "action":
            return '<button type="button" class="btn btn-icon btn-success edit feather icon-check-circle" id="test" data-bs-toggle="modal" data-bs-target="#exampleModal"></button><button type="button" class="btn btn-icon btn-danger delete feather icon-trash-2" id="test" data-bs-toggle="modal" data-bs-target="#confirmModal">'
                    
        else:
            return super(packagesJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        """To Filter data in table using in search
        """
        sSearch = self.request.GET.get("sSearch", None)
        if sSearch:
            qs = qs.filter(
                   Q(number__icontains=sSearch)
                  | Q(name_ar__icontains=sSearch)                
            )
        return qs


################# Start PackageView Data View ##############
class travellersView(CreateView):
    """
    Outgoing Order Type View for create new Outgoing Order Type
    """
    def get(self, request, *args, **kwargs):
        
        context = {
            'form': '',
            'url': '',
            'title_form': _('travellers '),
            'title_list': _('travellers'),
            }
       
        if 'id' in request.GET.keys():
            if request.GET.get('id'):
                try:
                    data=travellers.objects.filter(pk=request.GET.get('id'))
                    

                    result={'status':1,'data':serializers.serialize('json',data)}
                except:
                   pass
            else:
                
                result={'status':0,'data':''}
            return JsonResponse(result)
        else:
            
            context = {
                'form': travellersForm(),
                'url': reverse('travellers'),
                'title_form': _('travellers'),
                'title_list': _('travellers'),
                }
            

            return render(request, 'booking/travellers.html', context)

    def post(self, request, *args, **kwargs):
        form = travellersForm(request.POST)
        if request.POST.get('id'):
            data=get_object_or_404(travellers,pk=int(request.POST.get('id')))
            form=travellersForm(request.POST,instance=data)

        if form.is_valid():
           
            obj = form.save()
            obj.save()
            if request.POST.get('id'):
                if obj.id:
                    msg="تم التعديل بنجاح"
                    result={'status':1,'message':msg}
                else:
                    msg="هناك خطاء"
                    result={'status':2,'message':msg}
            else:
                if obj.id:
                    msg="تم الحفظ بنجاح"
                    result={'status':1,'message':msg}
                else:
                    msg="هناك خطاء"
                    result={'status':2,'message':msg}
        else:
            result={'status':0,'error':form.errors.as_json()}
        return JsonResponse(result)
          
    def delete(self, request,*args, **kwargs):
        pk=int(QueryDict(request.body).get('id'))
        if pk:
            try:
                data=get_object_or_404(travellers,pk=pk)
                data.delete()
                msg=message.delete_successfully()
                result={'status':1,'message':msg}
            except:
                msg=message.delete_error()
                result={'status':0,'message':msg}
        else:
            msg=message.delete_error()
            result={'status':0,'message':msg}
        return JsonResponse(result)


class travellersJson(BaseDatatableView):
    """List Customer Groups
    Returns:
        [json] --
    """
    model = travellers
    columns = [
        'id',  
        "name",
        "confirm",
        "mobile1",
        "status",
        'action',
        
    ]
    order_columns = [
        'id',  
        "name",
        "confirm",
        "mobile1",
        "status",
        'action',
         ]
    
    count = 0
    def get_initial_queryset(self):
        
        return self.model.objects.all()
        
        
    def render_column(self, row, column):
        """Render Column For Datatable
        """
        if column == "id":
            self.count += 1
            return self.count

        if column == "action":
            return '<button type="button" class="btn btn-icon btn-success edit feather icon-check-circle" id="test" data-bs-toggle="modal" data-bs-target="#exampleModal"></button><button type="button" class="btn btn-icon btn-danger delete feather icon-trash-2" id="test" data-bs-toggle="modal" data-bs-target="#confirmModal">'
                    
        else:
            return super(travellersJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        """To Filter data in table using in search
        """
        sSearch = self.request.GET.get("sSearch", None)
        if sSearch:
            qs = qs.filter(
                   Q(number__icontains=sSearch)
                  | Q(name_ar__icontains=sSearch)                
            )
        return qs




################# Start PackageView Data View ##############
class bookingView(CreateView):
    """
    Outgoing Order Type View for create new Outgoing Order Type
    """
    def get(self, request, *args, **kwargs):
        
        context = {
            'form': '',
            'url': '',
            'title_form': _('booking '),
            'title_list': _('booking'),
            }
       
        if 'id' in request.GET.keys():
            if request.GET.get('id'):
                try:
                    data=booking.objects.filter(pk=request.GET.get('id'))
                    

                    result={'status':1,'data':serializers.serialize('json',data)}
                except:
                   pass
            else:
                
                result={'status':0,'data':''}
            return JsonResponse(result)
        else:
            
            context = {
                'form': bookingForm(),
                'url': reverse('booking'),
                'title_form': _('booking'),
                'title_list': _('booking'),
                }
            

            return render(request, 'booking/booking.html', context)

    def post(self, request, *args, **kwargs):
        form = bookingForm(request.POST)
        if request.POST.get('id'):
            data=get_object_or_404(booking,pk=int(request.POST.get('id')))
            form=bookingForm(request.POST,instance=data)

        if form.is_valid():
           
            obj = form.save()
            obj.save()
            if request.POST.get('id'):
                if obj.id:
                    msg="تم التعديل بنجاح"
                    result={'status':1,'message':msg}
                else:
                    msg="هناك خطاء"
                    result={'status':2,'message':msg}
            else:
                if obj.id:
                    msg="تم الحفظ بنجاح"
                    result={'status':1,'message':msg}
                else:
                    msg="هناك خطاء"
                    result={'status':2,'message':msg}
        else:
            result={'status':0,'error':form.errors.as_json()}
        return JsonResponse(result)
          
    def delete(self, request,*args, **kwargs):
        pk=int(QueryDict(request.body).get('id'))
        if pk:
            try:
                data=get_object_or_404(booking,pk=pk)
                data.delete()
                msg=message.delete_successfully()
                result={'status':1,'message':msg}
            except:
                msg=message.delete_error()
                result={'status':0,'message':msg}
        else:
            msg=message.delete_error()
            result={'status':0,'message':msg}
        return JsonResponse(result)


class bookingJson(BaseDatatableView):
    """List Customer Groups
    Returns:
        [json] --
    """
    model = booking
    columns = [
        'id',  
        "passport",
        "traveller",
        "state_note",
        "created_at",
        "state",
        "total",
        'action',
        
    ]
    order_columns = [
        'id',  
        "passport",
        "traveller",
        "state_note",
        "created_at",
        "state",
        "total",
        'action',
         ]
    
    count = 0
    def get_initial_queryset(self):
        
        return self.model.objects.all()
        
        
    def render_column(self, row, column):
        """Render Column For Datatable
        """
        if column == "id":
            self.count += 1
            return self.count
        if column == "passport":
            
            return booking.objects.filter(id=row.id).values("traveller__passport")[0]["traveller__passport"]
        if column == "action":
            return '<button type="button" class="btn btn-icon btn-success edit feather icon-check-circle" id="test" data-bs-toggle="modal" data-bs-target="#exampleModal"></button><button type="button" class="btn btn-icon btn-danger delete feather icon-trash-2" id="test" data-bs-toggle="modal" data-bs-target="#confirmModal">'
                    
        else:
            return super(bookingJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        """To Filter data in table using in search
        """
        sSearch = self.request.GET.get("sSearch", None)
        if sSearch:
            qs = qs.filter(
                   Q(number__icontains=sSearch)
                  | Q(name_ar__icontains=sSearch)                
            )
        return qs

def show_all_books(request):
    return render(request, 'booking/all_booking.html',{"":""})



def show_dashboard(request):
    count_bookings=booking.objects.count()
    state_bookings_start=booking.objects.filter(state=1).count()
    state_bookings_stop=booking.objects.filter(state=2).count()
    state_bookings_end=booking.objects.filter(state=3).count()
    bookings=booking.objects.all().values("traveller__name","state_note","state","created_at")
    print("bookings"*100)
    print(bookings)
    context={
        "bookings":bookings,
        "count_bookings": count_bookings,
        "state_bookings_start":state_bookings_start,
        "state_bookings_stop":state_bookings_stop,
        "state_bookings_end":state_bookings_end,

    }
    return render(request, 'home/index.html',context)

