from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class StartTaskView(APIView):
    def get(self, request):
        pass

class ProgressView(APIView):
    def get(self, request, task_id):
        pass