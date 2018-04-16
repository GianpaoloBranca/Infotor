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

    max_length = get_max_fields_length(Torrente)
    data_with_length = add_max_length_to_items(max_length, data_dict)
    # non voglio che la chiave primaria venga mandata alla pagina
    del data_with_length['IDtrat']

    context_dict = {
        'torrents': torrents,
        'data': data,
        'data_dict': data_with_length,
        'field_max_length': max_length
    }

    return render(request, 'infotor/torrenti.html', context_dict)

def get_max_fields_length(Model):

    max_lengths = []
    fields = Model._meta.get_fields() #tuple

    for field in fields:
        max_lengths.append(field.max_length)

    return max_lengths

def add_max_length_to_items(max_lengths, data_dict):

    output = {}

    for i, (key, value) in enumerate(data_dict.items()):
        output[key] = (value, max_lengths[i])

    return output
