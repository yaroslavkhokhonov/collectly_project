from django.contrib import admin

from hospital.models import Patient, Payment

admin.site.register(Patient)
admin.site.register(Payment)
