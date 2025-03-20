import os

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect

from .models import StudentModel

from .forms import StudentForm

def student_register(request: HttpRequest):
    s_form = StudentForm()
    if request.method == 'POST':
        s_form = StudentForm(request.POST, request.FILES)
        if s_form.is_valid():
            s_form.save()
            return redirect('/')
    ctx = {
        'form': s_form,
        'title': 'Cadastrar aluno',
        'type':'create'
    }
    return render(request, "students/studentform.html", ctx)
    
def student_edit(request: HttpRequest, id):
    student = get_object_or_404(StudentModel, id=id)
    if request.method == 'POST':
        s_form = StudentForm(request.POST, request.FILES, instance=student)
        if s_form.is_valid():
            s_form.save()
            return redirect('/')
    s_form = StudentForm(instance=student)
    ctx = {
        'form':s_form,
        'title':'Atualizar aluno',
        'type': 'update'
    }
    return render(request, "students/studentform.html", ctx)

def student_remove(request: HttpRequest, id):
    student = get_object_or_404(StudentModel, id=id)
    student.delete()
    return redirect('/')
