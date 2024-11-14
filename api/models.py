from django.db import models

# Create your models here.

class TimeEntry(models.Model):
    employee_number = models.CharField(max_length=50)
    invoice_number  = models.CharField(max_length=50)
    time_spent      = models.DurationField()
    notes           = models.TextField(blank=True, null=True)
    date            = models.DateField()

    def __str__(self):
        return f"Employee {self.employee_number} - {self.date}"
