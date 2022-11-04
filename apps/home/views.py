# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from apps.booking.models import booking, travellers 
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/website/index.html')
    return HttpResponse(html_template.render(context, request))

def aboutUS(request):
    context = {'segment': 'معلومات عنا'}

    html_template = loader.get_template('home/website/about_as.html')
    return HttpResponse(html_template.render(context, request))

def tours(request):
    context = {'segment': 'استعلامات'}

    html_template = loader.get_template('home/website/tours.html')
    return HttpResponse(html_template.render(context, request))

def place(request):
    context = {'segment': 'الإماكن'}

    html_template = loader.get_template('home/website/place.html')
    return HttpResponse(html_template.render(context, request))
def callus(request):
    context = {'segment': 'للتواصل معنا'}

    html_template = loader.get_template('home/website/callus.html')
    return HttpResponse(html_template.render(context, request))


def search_p(request):
    if request.POST.get('text_search'):
        travell=travellers.objects.filter(passport=request.POST.get('text_search')).values(
        "id",
        "name",
        "email",
        "confirm",
        "state_name",
        "mobile1",
        "passport",
        "address",
        "photo",
        "status")[0]

        bookings=booking.objects.filter(traveller__id=travell['id']).values(
            "traveller__name",
            "traveller__name",
            "state_note",
        )[0]
        
    context = {'state_note': bookings["state_note"],"status":1}
    return JsonResponse(context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
