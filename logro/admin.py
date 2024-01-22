from django.contrib import admin
from .models import Achievements

# Register your models here.
class AchievementsAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Achievements)

