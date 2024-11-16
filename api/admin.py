from django.contrib import admin
from .models        import TimeEntry

# Register your models here.

@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    list_display    = ('invoice_number', 'employee_number', 'time_spent', 'notes', 'date', 'id')
    list_filter     = ('date', 'employee_number')
    search_fields   = ('employee_number', 'invoice_number')
