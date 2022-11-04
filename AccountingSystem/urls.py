# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path,re_path, include  # add this
from apps.home import views
urlpatterns = [
    path('admindea/', admin.site.urls),          # Django admin route
    path("cpanalcontrol/", include("apps.authentication.urls")), # Auth routes - login / register
    path("cpanalcontrol/", include("apps.booking.urls")),

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
    
    # re_path(r'^.*\.*', views.pages, name='pages'),
]
