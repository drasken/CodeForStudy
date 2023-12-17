
''' 
    Un modo comune di memorizzare tabelle e' come liste di dizionari. 
    Ogni riga della tabella corrisponde ad un dizionario le cui chiavi sono i nomi delle colonne della tabella.
    Questa collezione di dizionari e' poi memorizzata in una lista.
    Ad esempio la tabella
    
    nome  | anno | tel
  --------|------|---------
   Sofia  | 1973 | 5553546 
   Bruno  | 1981 | 5558432

puo' essere memorizzata come 
[{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]

'''


def es27(tabella, colonna, valore):
    ''' 
    Si implementi la funzione es27(tabella, colonna, valore) che presi in input
    - una tabella rappresentata tramite lista di dizionari
    - una stringa con il nome di una delle colonne della tabella
    - un valore
    modifica distruttivamente la tabella eliminando  la colonna indicata e 
    le righe che in quella colonna avevano valori diversi da valore.
    La funzione deve poi restituire il numero di righe eliminate.
    Ad esempio con  tabella = [{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},
                                {'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]
    al termine di es27(dati, 'anno', 1981)  verra' restituito il numero 1 e la tabella 
    risultera'  modificata  in [{'nome': 'Bruno','tel': 5558432}]

    '''
    # inserisci qui il tuo codice

    res = len(tabella) #var for storing number of deleted raws
    
    #SECOND TRY

    tabella[:] = [dictio for dictio in tabella if dictio.get(colonna) == valore]

    for i in tabella:
        i.pop(colonna)

    res -= len(tabella)     
        
    return res

    #TEST PASSED!!


    
    #FIRST TRY
    # use column to delete raw if val == val in raw
    # each time a raw is deleted add 1 to res
    #after that delet param column for each remaining raw
    #return res

    # newTab = []
    # for i in tabella:
    #     if i[colonna] == valore:
    #        continue
    #     else:
    #         tabella.remove(colonna[valore])
    #         res += 1

    # for j in newTab:
    #     j.pop(colonna)

    # tabella = newTab

    return res

        
    
prova = [{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546}, {'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}, {'nome': 'Carlo', 'anno': 1981 ,'tel': 6661203}, {'nome': 'Mimma', 'anno': 1997 ,'tel': 11164473}]

provaFun = es27(prova, 'anno', 1981)


print(provaFun)

        
