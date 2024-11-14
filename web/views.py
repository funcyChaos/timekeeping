from django.shortcuts import render
from api.models         import TimeEntry
from api.serializers    import TimeEntrySerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')
