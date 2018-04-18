# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Torrente(models.Model):

    class Meta:
        verbose_name_plural = 'Torrenti'

    def __str__(self):
        return self.Trtname

    IDtrat = models.IntegerField(primary_key=True)

    # nome della forra com'è conosciuta dai torrentisti
    Trtname = models.CharField('Nome tratta', max_length=16)

    Regione = models.CharField('Regione', max_length=2)
    Provincia = models.CharField('Provincia', max_length=2)
    Comune = models.CharField('Comune', max_length=6)
    Grumon = models.CharField('Gruppo montuoso', max_length=11)
    Sezion = models.CharField('Sezione', max_length=7) # sezione

    NUOVO_CHOICES = (('SI', 'Sì'), ('NO', 'No'))
    Nuovo = models.CharField('Nuovo tracciato?', max_length=2, choices=NUOVO_CHOICES)

    Tipologia = models.CharField('Tipologia', max_length=2) # codice tipologia
    Caratter = models.CharField('Caratteristica', max_length=2) # codice caratteristica

    PerLun = models.IntegerField('Lunghezza piana') # in metri
    PerLunF = models.IntegerField('Lunghezza inclinata') # in metri
    Perquo1 = models.IntegerField('Quota inizio') # in metri slm
    Perquo2 = models.IntegerField('Quota fine') # in metri slm
    Pendenza = models.IntegerField('Pendenza') # > 0 salita, < 0 discesa
    PerTem1 = models.IntegerField('Tempo di percorrenza andata')
    PerTem2 = models.IntegerField('Tempo di percorrenza ritorno')
    PerDif = models.CharField('Gradi di difficoltà', max_length=3)

    Dataril = models.DateField('Data aggiornamento')
    Rilevatore = models.CharField('Nome rilevatore', max_length=50)
    TipoRIL = models.CharField('Classe di accuratezza', max_length=3)


class Percorso(models.Model):

    class Meta:
        verbose_name_plural = 'Percorsi'

    def __str__(self):
        return self.Nume

    IDperc = models.IntegerField(primary_key=True)

    Nume = models.CharField('Numero percorso', max_length=6) # numero / sigla percorso
    Trek1 = models.CharField('Nome/sigla/logo trekking', max_length=80) # codice del trekking
    Percorr = models.CharField('Percorribilità', max_length=2) # codice di percorribilità
    Denomi = models.CharField('Descrizione', max_length=80) # denominazione del percorso

    PerLun = models.IntegerField('Lunghezza piana') # in metri
    PerLunF = models.IntegerField('Lunghezza inclinata') # in metri
    Perquo1 = models.IntegerField('Quota inizio') # in metri slm
    Perquo2 = models.IntegerField('Quota fine') # in metri slm
    Pendenza = models.IntegerField('Pendenza') # > 0 salita, < 0 discesa
    PerTem1 = models.IntegerField('Tempo di percorrenza andata')
    PerTem2 = models.IntegerField('Tempo di percorrenza ritorno')
    PerDif = models.CharField('Grado di difficoltà', max_length=3)

    Segni = models.CharField('Segnaletica orizzontale', max_length=3)
    Dataril = models.DateField('Data aggiornamento')

    ReteReg = models.CharField('Rete regionale', max_length=4) # se inserito in reti regionali
    CodReg = models.CharField('Codice catasto regionale', max_length=12)
    Operatore = models.CharField('Ente manutentore', max_length=80)
    Storico = models.CharField('Interesse storico', max_length=2)
    Arcitett = models.CharField('Interesse architettonico', max_length=2) # codice interesse architettonico
    Paesagg = models.CharField('Interesse paesaggistico', max_length=2) # codice interesse paesaggistico
    Natural = models.CharField('Interesse naturalistico', max_length=2) # codice interesse naturalistico
    Link = models.CharField('Link CMS', max_length=16) # link alla possibile scheda CMS
    UTENTE = models.CharField('Utente aggiornatore', max_length=16) # codice utente aggiornatore
