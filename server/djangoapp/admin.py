from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarModelAmin(admin.ModelAdmin):
    list_display = ['name', 'dealer_id', 'type', 'year']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description', 'state']

# Register models here
admin.site.register(CarModel, CarModelAmin)
admin.site.register(CarMake, CarMakeAdmin)
