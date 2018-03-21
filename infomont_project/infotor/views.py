# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from infotor.models import Torrente

# Create your views here.
def index(request):
    data = serializers.serialize("python", Torrente.objects.all())
    context_dict = {
        'data':data
    }

    return render(request, 'infotor/base.html', context_dict)
