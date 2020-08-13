from django.contrib import admin
from food.models import Restaurant, Image
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'business_id', 'address', 'latitude', 'longitude']

class ImageAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'category']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Image, ImageAdmin)