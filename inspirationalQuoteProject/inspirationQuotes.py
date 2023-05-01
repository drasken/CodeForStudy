#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:40:45 2023

@author: drasken
"""

#Così riesco a estrarre una citazione dal sito

import requests

def citazioneWeb (url):
    quoteOTD = requests.get(url)
    quote = quoteOTD.json()['quote']
    author = quoteOTD.json()['author']
    citazione = quote + ' - ' + author
    return citazione
    
#voglio implementare un metodo per confrontare le stringhe e se c'è già la citazine
#non si aggiunge la citazione al testo
#eventualmente se decido come mandare la citazione a me stesso implementare
#un'altra funzione che mi mandi comunque la cit ma segnandola come ripetuta
def aggiungiCitazioneTesto (cit, fileTxt):
    citazioni = []
    with open(file= fileTxt) as file:
        citazioni = file.readlines()        
    citApp = cit+'\n'
    if citApp  not in citazioni:
        with open (file= fileTxt, mode='a+') as file:
            file.writelines(citazione)            
            
#questa variabile è una stringa con la citazione e l'autore    
citazione = citazioneWeb("https://api.goprogram.ai/inspiration")

#questa variabile è il file  txt a cui fare append
fileCitazioni = "inspirationalQuotes.txt"

#provo a implementarlo come funzione

aggiungiCitazioneTesto (citazione, fileCitazioni)
#funziona, se la frase è già presente non l'aggiunge

#ora sarebbe da implementare in qualche modo tipo
#su telegram o mandarla tramite email o whatsapp...ma WA è una rottura mi sa
#Ora devo implementare iln qualche moto la citazine,
# devo trovare un modo per mandarmela o mandarla tutti i giorni 
#Possibilità, Telegram-facile, whatsapp- medio, email-facile, notificca push-???

#intanto credo che salverò le citazioni in un file txt ///FATTO





