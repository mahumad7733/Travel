# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.booking import views

urlpatterns = [
path('packages/', views.PackageView.as_view(),name="packages"),
path('packagesJson/',views.packagesJson.as_view(),name='packagesJson'),

# ========================================
path('travellers/', views.travellersView.as_view(),name="travellers"),
path('travellersJson/',views.travellersJson.as_view(),name='travellersJson'),
# =========================================

# ========================================
path('booking/', views.bookingView.as_view(),name="booking"),
path('bookingJson/',views.bookingJson.as_view(),name='bookingJson'),
# =========================================
path('showallbooks/',views.show_all_books,name='show_all_books'),
path('dashboard/',views.show_dashboard,name='show_dashboard'),


]
