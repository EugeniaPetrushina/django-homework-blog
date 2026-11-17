from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'checked')
    list_filter = ('checked',)
    list_editable = ('checked',)
