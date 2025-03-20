from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import StudentForm


# Create your views here.
def student_form(request: HttpRequest):
    s_form = StudentForm()
    ctx = {
        'form':s_form
    }
    return render(request, "students/studentform.html",ctx)

def student_register(request: HttpRequest):
    s_form = StudentForm()
    if request.method == 'POST':
        s_form = StudentForm(request.POST)
        if s_form.is_valid():
            s_form.save()
            return redirect('/')
        else:
            return render(request, "students/studentform.html", {'form':s_form})
    return render(request, "students/studentform.html", {'form':s_form})
