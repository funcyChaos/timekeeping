from django.db import models

# Create your models here.

class TimeEntry(models.Model):
    employee_number = models.CharField(max_length=50, blank=False)
    invoice_number  = models.CharField(max_length=50, blank=False, null=False)
    time_spent      = models.DurationField(blank=False, null=False)
    notes           = models.TextField(blank=True, null=True)
    date            = models.DateField(blank=False)

    def __str__(self):
        return f"Employee {self.employee_number} - {self.date}"
