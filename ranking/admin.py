from django.contrib import admin

from .models import Ranking


@admin.register(Ranking)
class Ranking(admin.ModelAdmin):
    pass