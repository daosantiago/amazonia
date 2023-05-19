from django.contrib import admin

from .models import Path


class Paths(admin.ModelAdmin):
    path = Path()
    list_display = ('id', 'path')


admin.site.register(Path, Paths)
