# -*- coding: utf-8 -*-
from django import forms
from .models import Pregunta,ApuestasRealizadas



class PreguntaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Pregunta
        fields = ('text', 'due_date')
        exclude = ('create_date', 'create_user', 'update_date', 'update_user')
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Ingrese la pregunta.',
                'class' : 'form-control'
            }),
            'due_date': forms.TextInput( attrs={
            'class' : 'form-control'
            }),
        }

    def save(self, commit=True):
        return super(PreguntaForm, self).save(commit=commit)

class ApuestasRealizadasForm(forms.ModelForm):
    pregunta = None
    user = None

    def __init__(self, pregunta, user, *args, **kwargs):
        super(ApuestasRealizadas, self).__init__(*args, **kwargs)
        self.pregunta = pregunta
        self.user = user
        self.fields['respuestas_validas'].label = self.pregunta.text
        self.fields['respuestas_validas'].queryset = self.pregunta.respuestas_validas

    class Meta:
        model = ApuestasRealizadas
        fields = ('respuestas', 'user')
        exclude =('pregunta','date')
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Ingrese la pregunta.',
                'class' : 'form-control'
            }),
            'due_date': forms.TextInput( attrs={
            'class' : 'form-control'
            }),
        }

    def save(self, commit=True):
        if commit:
            try:
                return super(PreguntaForm, self).save(commit=commit)
            except:
                raise forms.ValidationError(_('Ya respondiste chango'))
