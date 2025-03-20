from django.http import HttpRequest
from django.shortcuts import render

from students.models import StudentModel

# Create your views here.
def home(request: HttpRequest):
    ctx = {
        'students': StudentModel.objects.all()
    }
    return render(request,"main/home.html", ctx)