from django.contrib import admin
from .models import Trend
# Register your models here.


class TrendAdmin(admin.ModelAdmin):
    list_display = ['phrase', 'hits']


admin.site.register(Trend, TrendAdmin)