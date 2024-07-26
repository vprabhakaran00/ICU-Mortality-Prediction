#  This file registers models with the Django admin interface.
#  We can use the Django admin to manage the models data

from django.contrib import admin    # admin contains admin interface
from .models import PatientData     # we get the model - PatientData

# Register your models here.
admin.site.register(PatientData)    # register the model with the Django admin interface