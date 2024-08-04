from django.contrib import admin
from .models import TimeLine

# Register your models here.

@admin.register(TimeLine)
class TimeLineAdmin(admin.ModelAdmin):
    pass