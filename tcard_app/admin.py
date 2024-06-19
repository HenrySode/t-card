from django.contrib import admin

from django.contrib import admin
from .models import TCard,Event, Scan

admin.site.register(Event)
admin.site.register(TCard)
admin.site.register(Scan)