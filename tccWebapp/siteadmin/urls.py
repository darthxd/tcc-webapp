from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.student_show, name="home"),
    path('cadastrar-aluno/',views.student_register, name='studentregister'),
    path('remover-aluno/id=<int:id>',views.student_remove, name='studentremove'),
    path('editar-aluno/id=<int:id>',views.student_edit, name='studentedit')
]
