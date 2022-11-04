# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import (
    state,
    packages,
    travellers,
    booking)
# Register your models here.
admin.site.register(state)
admin.site.register(packages)
admin.site.register(travellers)
admin.site.register(booking)