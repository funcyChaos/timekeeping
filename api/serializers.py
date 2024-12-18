from rest_framework     import serializers
from .models            import TimeEntry

class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model   = TimeEntry
        fields  = ['employee_number', 'invoice_number', 'time_spent', 'notes', 'date']
