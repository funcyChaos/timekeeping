from django.shortcuts import render

from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import status
from .models                    import TimeEntry
from .serializers               import TimeEntrySerializer

# Create your views here.


#@csrf_exempt
class TimeEntryView(APIView):
    def post(self, request, *args, **kwargs):
        serializer  = TimeEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):
        data = {"message": "Hello, World!"}
        return Response(data, status=status.HTTP_200_OK)
