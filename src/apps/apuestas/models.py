# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Pregunta(models.Model):
    text = models.CharField(max_length=200)
    due_date = models.DateTimeField('Fecha Limite')
    create_date = models.DateTimeField('Fecha Publicacion', auto_now_add=True)
    create_user = models.ForeignKey(User, related_name="pregunta_create_user")
    update_date = models.DateTimeField('Fecha Actualizada', auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="pregunta_update_user")

    def __unicode__(self):
        return "%s" % (self.text)

    @property
    def respuestas_validas(self):
        return RespuestaValidas.objects.filter(pregunta=self)
    def get_result(self):
        respuestas_validas = self.respuestas_validas
        dic = []
        for x in respuestas_validas:
            dic.append((x.text, apuestas.objects.filter(respuestas_validas=x).count()))
        return dic


class RespuestaValidas(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    create_date = models.DateTimeField('Fecha Publicacion', auto_now_add=True)
    create_user = models.ForeignKey(User, related_name="respusta_valida_create_user")
    update_date = models.DateTimeField('Fecha Actualizada', auto_now_add=True)
    update_user = models.ForeignKey(User, related_name="respusta_valida_update_user")

    class Meta:
        unique_together = ('pregunta', 'text')

    def __unicode__(self):
        return "%s" % (self.text)



class ApuestasRealizadas(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    respuestas = models.ForeignKey(RespuestaValidas)
    #fecha = models.ForeignKey(update_date)
    user = models.ForeignKey(User)
    text = models.CharField(max_length=200)


    class Meta:
        unique_together = ('pregunta', 'user')


    def save(self, *args, **kwargs):
        super(ApuestasRealizadas, self), save (*args, **kwargs      )

        return super (ApuestasRealizadas,self).save(*args,**kwargs)
