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
def extractValue():
    pass

def es26(tabella, colonna):
    ''' 
    Si implementi la funzione es26(tabella,colonna) che presi in input
    - una tabella rappresentata tramite lista di dizionari
    - una stringa con il nome di una delle colonne della tabella
    modifica distruttivamente la tabella riordinandone le righe in ordine decrescente rispetto 
    ai valori contenuti nella  colonna indicata. La funzione deve restituire il numero di colonne della tabella.
        Ad esempio con  tabella = [{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432},
                        {'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546}]
    al termine di es26(dati, 'anno')  la  tabella sara' stata modificata in 
    [{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432},{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546}]
    e restituisce il numero di colonne 3.
    '''
    
    # inserisci qui il tuo codice

    tabella.sort(key= lambda x : x[colonna])

    return len(tabella)
    #TODO: to run test !!!!!!

    #tentativo N. 2!!
    # listRes = []
    # listValue = []
    
    # #estraggo tutti i valori, li ordino e poi associo alla lista result
    # for i in range(len(tabella)):
    #     listValue.append(tabella[i][colonna])
        
    # listValue = sorted(listValue)
    # for j in listValue:
    #     ind = tabella.index(j)
    #     listRes += tabella[ind]
    #     tabella.pop(ind)
    
    # return listRes
    
    
    
    
    
    
    
    
    
# PROVA VARIA
#     listAppoggio = []
#     for i in tabella:
#         listAppoggio.append(i[colonna])

#     for j in tabella:
#         print(j[colonna])
        
#     return listAppoggio

provaTab = [{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]

provaFun = es26(provaTab, 'anno')

print(provaFun)
