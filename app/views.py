from django.shortcuts import render
from django. views import View
# Importing all models from app/models.py
from .models import *
# Index View
class IndexView(View):
    
    def get (self, request):
        return render(request,'index.html',)
    def post(self, request):
        pass
from django.shortcuts import render

