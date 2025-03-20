from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect

from .models import StudentModel

from .forms import StudentForm


# Create your views here.
def student_form(request: HttpRequest):
    s_form = StudentForm()
    ctx = {
        'form':s_form,
        'submit':'Cadastrar'
    }
    return render(request, "students/studentform.html",ctx)

def student_register(request: HttpRequest):
    s_form = StudentForm()
    if request.method == 'POST':
        s_form = StudentForm(request.POST, request.FILES)
        if s_form.is_valid():
            s_form.save()
            return redirect('/')
        else:
            return render(request, "students/studentform.html", {'form':s_form})
    ctx = {
        'form':s_form
    }
    return render(request, "students/studentform.html", ctx)
    
def student_edit(request: HttpRequest, id):
    student = get_object_or_404(StudentModel, id=id)
    s_form = StudentForm(instance=student)
    if request.method == 'POST':
        s_form = StudentForm(request.POST, request.FILES)
        if s_form.is_valid():
            s_form.save()
            return redirect('/')
        else:
            return render(request, "students/studentform.html", {'form':s_form})
    ctx = {
        'form':s_form,
        'submit':'Salvar'
    }
    return render(request, "students/studentform.html", ctx)

def student_remove(request: HttpRequest, id):
    student = get_object_or_404(StudentModel, id=id)
    student.delete()
    return redirect('/')
