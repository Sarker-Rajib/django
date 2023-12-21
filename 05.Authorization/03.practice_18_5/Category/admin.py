from django.contrib import admin
from .models import Add_Category

# Register your models here.
# admin.site.register(Add_Category)

class CategorySlug(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']

admin.site.register(Add_Category, CategorySlug)