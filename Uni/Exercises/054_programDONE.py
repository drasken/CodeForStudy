

import copy

def es54(lista):
    ''' 
    la funzione es54(lista) che presa in input una lista contenente interi e stringhe, modifica 
    la lista distruttivamente e restituisce un dizionario.
    Al termine della funzione dalla lista devono risultare  cancellate tutte le stringhe e il dizionario 
    restituito deve contenere come chiavi le stringhe cancellate ciascuna con attributo il numero di volte 
    in cui occorrevano nella lista.
    Ad esempio per lista=[1,'a',2,'b','a',8,'d',8] la funzione al termine restituisce il dizionario 
    {'a':2,'b':1,'d':1} e la lista diviene [1,2,8,8]
    '''
    # inserisci qui il tuo codice
    
    listaCopy = copy.deepcopy(lista)
    dictRes = {}
    
    for num, chiave in enumerate(listaCopy):
        if type(listaCopy[num]) != str:
            continue
        else:
            if listaCopy[num] not in dictRes.keys():
                dictRes[chiave] = 1
            else:
                dictRes[chiave] += 1
            
            lista.remove(chiave)
        
    return dictRes    


if __name__ == '__main__':
    provaList = [1, 'a', 2, 'b', 'a', 8, 'd', 8]
    
    test1 = es54(provaList)

