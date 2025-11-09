from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'date')  # ✅ show date column
    list_filter = ('date',)  # optional – adds a filter by date on the right side
    search_fields = ('name', 'email', 'phone')  # optional – adds search bar
 