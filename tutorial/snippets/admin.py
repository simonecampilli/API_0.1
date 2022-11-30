from django.contrib import admin
from .models import Prova, Statistiche, Snippet
# Register your models here.
admin.site.register(Prova)
admin.site.register(Statistiche)
admin.site.register(Snippet)
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']