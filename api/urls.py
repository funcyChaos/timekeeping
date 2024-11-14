from django.urls    import path
from .views         import TimeEntryView

urlpatterns = [
        path('time-entry/', TimeEntryView.as_view(), name='time-entry'),
]
