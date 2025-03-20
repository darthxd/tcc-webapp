from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-aluno', views.student_form, name='studentform'),
    path('cadastro',views.student_register, name='studentregister'),
    path('remover-aluno/<int:id>',views.student_remove, name='studentremove'),
    path('editar-aluno/<int:id>',views.student_edit, name='studentedit')
]
