# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.defaultfilters import slugify
from infotor.models import Torrente

def index(request):
    torrents_names = Torrente.objects.values_list('Trtname', flat=True).order_by('Trtname')
    torrents_slugs = slugify_all(torrents_names)

    torrents = zip(torrents_names, torrents_slugs)

    context_dict = {
        'torrents': torrents
    }
    # la pagina index non è altro che quella per i torrenti ma senza dati visualizzati
    return render(request, 'infotor/torrenti.html', context_dict)

def show_torrent(request, torrent_name):
    # TODO tipo tutto ancora
    data = Torrente.objects.get(Trtname=torrent_name)

    context_dict = {
        'data': data
    }

    return render(request, 'infotor/torrenti.html', context_dict)

# helper function
def slugify_all(names):

    slugs = []
    for name in names:
        slugs.append(slugify(name))

    return slugs
