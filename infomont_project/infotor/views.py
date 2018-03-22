# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from infotor.models import Torrente
from django.core import serializers

def index(request):
    # tira fuori un dizionario con tutti i campi per il torrente
    field_names = Torrente._meta.get_fields()
    torrent = Torrente.objects.get(Trtname='Torrente esempio')

    context_dict = {
        'fields': field_names,
        'torrent': torrent
    }

    return render(request, 'infotor/home.html', context_dict)
