# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('about', views.aboutUS, name='aboutUS'),
    path('tours', views.tours, name='tours'),
    path('place', views.place, name='place'),
    path('callus', views.callus, name='callus'),
    path('search_p', views.search_p, name='search_p'),
    
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
