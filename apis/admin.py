from django.contrib import admin
from .models import *


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name_dish","descriptions","time_category","price","prf_time","created_at",]
    list_filter = ["name_dish","price"]

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["type","max_person","status",]

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ["table","castumername","total_sum","is_paid","created_at",]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["dish","bill","count","total",]
    list_filter = ["dish","bill","count",]