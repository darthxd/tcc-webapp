from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from django.forms import ModelForm, DateInput
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name','rm','birthdate','email','phone','student_course','student_grade','photo']
        labels = {
            'name':'Nome',
            'rm':'RM',
            'birthdate':'Data de nascimento',
            'email':'E-mail',
            'phone':'Telefone',
            'student_course':'Curso',
            'student_grade':'Série',
            'photo':'Foto'
        }
        widgets = {'birthdate': DateInput(attrs={'type':'date'})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('rm',wrapper_class='col-md-4 col-12 px-1'),
                Field('name',wrapper_class='col-md-8 col-12 px-1'),
                css_class='row w-100'
            ),
            Div(
                Field('phone', wrapper_class='col-md-6 col-12 px-1'),
                Field('birthdate', wrapper_class='col-md-6 col-12 px-1'),
                css_class='row w-100'
            ),
            Div(
                Field('student_course', wrapper_class='col-md-6 col-12 px-1'),
                Field('student_grade', wrapper_class='col-md-6 col-12 px-1'),
                css_class='row w-100'
            ),
            Div(
                Field('email', wrapper_class='col-md-8 col-12 px-1'),
                Field('photo', wrapper_class='col-md-4 col-12 px-1'),
                css_class='row w-100'
            ),
        )
