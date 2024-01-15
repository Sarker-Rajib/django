from django.contrib import admin
from . import models

# Register your models here.
class DesignationAmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ['name']
admin.site.register(models.Designation, DesignationAmin)

class SpecializationAmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ['name']
admin.site.register(models.Specialization, SpecializationAmin)

admin.site.register(models.AvailableTime)
admin.site.register(models.Doctor)
admin.site.register(models.Review)