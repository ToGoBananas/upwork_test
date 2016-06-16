from django.contrib import admin
from .models import SampleA, SampleB


@admin.register(SampleA)
class Sample1Admin(admin.ModelAdmin):
    list_display = ('created', )


@admin.register(SampleB)
class Sample2Admin(admin.ModelAdmin):
    list_display = ('created', )