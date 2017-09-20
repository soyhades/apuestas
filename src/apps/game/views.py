# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import urllib2

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import PreguntaForm
from .models import Pregunta
from .models import ApuestasRealizadas


def apuestas_api():
    method = "GET"
    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)
    #data = urllib.urlencode([{respuesta_id: '2'}])
    #request = urllib2.Request(url, data=data)
    request = urllib2.Request(settings.HOST_API)
    request.add_header("Content-Type",'application/json')
    request.add_header('Authorization', 'token %s' % settings.API_AUTH_TOKEN)
    request.get_method = lambda: method

    try:
        connection = opener.open(request)
    except urllib2.HTTPError,e:
        connection = e

    if connection.code == 200:
        data = connection.read()
        return json.loads(data)

    else:
        pass

@login_required
def apuestas_list(request):
    form = PreguntaForm()
    if request.method == 'POST':
        form = PreguntaForm(data=request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.create_user = request.user
            pregunta.update_user = request.user
            pregunta.save()
    template = loader.get_template('apuestas_list.html')
    pregunta_list = Pregunta.objects.all()
    context = {
        'username': request.user.username,
        'form': form,
        'pregunta_list': pregunta_list
    }
    return HttpResponse(template.render(context, request))

class PreguntaView(LoginRequiredMixin,View):
    form = PreguntaForm()
    template_name = "pregunta_form.html"
    def get(self, request, *args, **kwargs):
        id_pregunta = self.kwargs['id_pregunta']
        prg = Pregunta.objects.get(pk=id_pregunta)
        form = PreguntaForm(instance=prg)
        context={
            'form': form
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        id_pregunta = self.kwargs['id_pregunta']
        prg = Pregunta.objects.get(pk=id_pregunta)
        form = PreguntaForm(data=request.POST, instance=prg)
        if form.is_valid():
            prg=form.save(commit=False)
            prg.update_user = request.user
            prg.save()
            context = {
                'form':form
            }

        return render(request, self.template_name, context)


@login_required
def apuesta(request, id_pregunta):
    template = loader.get_template('apuestasrealizadas.html')
    pregunta = Pregunta.objects.get(pk=id_pregunta)
    form = ApuestasRealizadasForm(pregunta, request.user)
    if request.method == 'POST':
        form = ApuestasRealizadasForm(pregunta, request.user, data=request.POST)
        if form.is_valid():
            respuesta_apuesta = form.save(commit=False)
            respuesta_apuesta.user = request.user
            respuesta_apuesta.save()
    context = {
        'pregunta': pregunta,
        'form': form
    }
    return HttpResponse(template.render(context, request))
