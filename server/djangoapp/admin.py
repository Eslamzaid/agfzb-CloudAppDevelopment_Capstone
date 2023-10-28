from django.contrib import admin
# from .models import related models
from .models import *

# Register your models here.

# CarModelInline class
# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

class CarModelInline(admin.TabularInline):
    model = CarModel


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [
        CarModelInline,
    ]

admin.site.register(CarMake, CarMakeAdmin)


# admin.site.register(CarMake)
# admin.site.register(CarModel)