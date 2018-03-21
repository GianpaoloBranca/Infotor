# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Torrente(models.Model):
    IDtrat = models.IntegerField(primary_key=True)

    # nome della forra com'è conosciuta dai torrentisti
    Trtname = models.CharField(max_length=16)

    Regione = models.CharField(max_length=2)
    Provincia = models.CharField(max_length=2)
    Comune = models.CharField(max_length=6)
    Grumon = models.CharField(max_length=11) # gruppo montuoso
    Sezion = models.CharField(max_length=7) # sezione
    Nuovo = models.CharField(max_length=2) # nuovo tracciato SI/NO

    Tipologia = models.CharField(max_length=2) # codice tipologia
    Caratter = models.CharField(max_length=2) # codice caratteristica

    PerLun = models.IntegerField() # lunghezza piana in metri
    PerLunF = models.IntegerField() # lunghezza inclinata in metri
    Perquo1 = models.IntegerField() # quota inizio tratta in metri slm
    Perquo2 = models.IntegerField() # quota fine tratta in metri slm
    Pendenza = models.IntegerField() # > 0 salita, < 0 discesa
    PerTem1 = models.IntegerField() # tempo di percorrenza andata
    PerTem2 = models.IntegerField() # tempo di percorrenza ritorno
    PerDif = models.CharField(max_length=3) # difficoltà escursionistica

    Dataril = models.DateField() # data aggiornamento
    Rilevatore = models.CharField(max_length=50) # nome rilevatore
    TipoRIL = models.CharField(max_length=3) # classe di accuratezza del rilievo


class Percorso(models.Model):
    IDperc = models.IntegerField(primary_key=True)

    Nume = models.CharField(max_length=6) # numero / sigla percorso
    Trek1 = models.CharField(max_length=80) # codice del trekking
    Percorr = models.CharField(max_length=2) # codice di percorribilità
    Denomi = models.CharField(max_length=80) # denominazione del percorso

    PerLun = models.IntegerField() # lunghezza piana in metri
    PerLunF = models.IntegerField() # lunghezza inclinata in metri
    Perquo1 = models.IntegerField() # quota inizio tratta in metri slm
    Perquo2 = models.IntegerField() # quota fine tratta in metri slm
    Pendenza = models.IntegerField() # > 0 salita, < 0 discesa
    PerTem1 = models.IntegerField() # tempo di percorrenza andata
    PerTem2 = models.IntegerField() # tempo di percorrenza ritorno
    PerDif = models.CharField(max_length=3) # difficoltà escursionistica

    Segni = models.CharField(max_length=3) # segnaletica orizzontale
    Dataril = models.DateField() # data aggiornamento

    ReteReg = models.CharField(max_length=4) # se inserito in reti regionali
    CodReg = models.CharField(max_length=12) # codice catasto regionale
    Operatiore = models.CharField(max_length=80) # ente manutentore
    Storico = models.CharField(max_length=2) # codice interesse storico
    Arcitett = models.CharField(max_length=2) # codice interesse architettonico
    Paesagg = models.CharField(max_length=2) # codice interesse paesaggistico
    Natural = models.CharField(max_length=2) # codice interesse naturalistico
    Link = models.CharField(max_length=16) # link alla possibile scheda CMS
    UTENTE = models.CharField(max_length=16) # codice utente aggiornatore
