# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.forms.models import model_to_dict
from infotor.models import Torrente

def index(request):
    torrents = Torrente.objects.values_list('IDtrat', 'Trtname').order_by('Trtname')

    context_dict = {
        'torrents': torrents
    }
    # la pagina index non è altro che quella per i torrenti ma senza dati visualizzati
    return render(request, 'infotor/torrenti.html', context_dict)

def show_torrent(request, torrent_id):
    torrents = Torrente.objects.values_list('IDtrat', 'Trtname').order_by('Trtname')
    data = Torrente.objects.get(IDtrat=torrent_id)
    data_dict = model_to_dict(data)

    # non voglio che la chiave primaria venga mandata alla pagina
    del data_dict['IDtrat']

    context_dict = {
        'torrents': torrents,
        'torrente': data,
        'data_dict': data_dict,
    }

    return render(request, 'infotor/torrenti.html', context_dict)
