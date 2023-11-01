#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consideriamo la codifica posizionale di un numero in base B.
Date le N cifre:      a_{N-1} .... a_1 a_0
Il valore del numero si ottiene sommando, per ogni indice i
da 0 ad N-1, i valori a_i*B^i .

Esempio: se la base B=6  e il numero è     (52103)_6
Il suo valore sarà    5*6^4 + 2*6^3 + 1*6^2 + 0*6^1 + 3*6^0 = (6951)_10

Generalizziamo questa notazione per usare basi diverse per ciascuna
posizione: avremo quindi una lista "bases" formata da N basi e un
numero formato da N cifre contenute in una lista di nome "digits".
Per l'esempio sopra avremo: bases = [6, 6, 6, 6, 6] digits = [5, 2, 1,
0, 3]. Le cifre sono tali che ciascuna sia minore della base nella
stessa posizione.  Il valore del numero in base 10 si ottiene come
nella conversione iniziale, usando per la potenza i-esima la base
i-esima della lista.

NOTA: per comodità useremo nel codice delle liste di cifre e di basi
in cui l'esponente della potenza corrisponde all'indice nelle liste.
Quindi ciascuna lista conterrà basi e cifre a partire dalle unita'.

NOTA: Il numero di basi N e' maggiore stretto di 1. I valori delle
basi anche esse sono maggiori di 1.

In base a quanto detto, data in ingresso una lista "bases",
un obiettivo dell'HW e' genera la lista di tutte le possibili
combinazioni valide di cifre rappresentabili con quelle basi.

Esempio: se in ingresso bases vale [2, 5], tutte le combinazioni sono:
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]

infatti:
- nella prima cifra ci sono solo valori fra [0, 1] perche' la base e' 2
- nella seconda cifra ci sono solo valori fra [0, 4] perche' la base e' 5.

Ciascuna combinazione rappresenta un intero che va convertito da lista
a intero secondo la base specificata in "bases". Una volta che tutte
le possibili combinazioni sono state convertite in un intero e'
necessario trovare quali interi hanno piu di una rappresentazione
nelle basi date.

Esempio: Se in ingresso bases vale [4, 3, 2] allora gli interi che 
ammetto piu di una rappresentazione sono {3, 4, 5, 6, 7, 8, 9, 10}

Infatti, ad esempio il numero 10 con queste basi ha le due rappresentazioni 
    [3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
    [0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10

Il problema e' gia' stato diviso in sottoproblemi e dovete realizzate
quindi le funzioni che seguono:
 - decode_digits, e' la funzione piu semplice e basilare che riceve
   una lista di basi e una lista di digits e la converte in intero.
 - generate_digits, e' la funzione che fa la maggior parte del lavoro
   che data una lista di basi, calcola tutte le combinazioni.
 - find_doubles, e' l'ultima funzione che date le combinazioni trova i
   corrispettivi interi che hanno piu di una rappresentazione.

Il Timeout applicato è 0.5 secondi.

ATTENZIONE: è vietato importare altre librerie oltre quelle già presenti.
"""

from typing import List, Set
import random #DA CANCELLARE

#COMMENT TO DELETE APPOGGIO PER LA PRIMA FUNZIONE
def powBases(bass : list[int]) -> list[int]:
    
    res : list[int] = []
    # index : int = 0
    
    # for k in bass:
    #     res.append(pow(k,index))
    #     index += 1
    
    for i,j in enumerate(bass):
          #result.append(pow(j, i)) # append meno veloce  
          res += [pow(j,i)]
    
    return res

def mulTuple (element : tuple[int]) -> int:
    #pass #da implementare, frse basta una lambda     
    res : int = 0
    for i in element:
        res += i[0] * i[1]
    return res    
        
# FUNZIONA, TO REFACTOR
def decode_digits(digits: List[int], bases: List[int]) -> int:
    '''
    Riceve una lista di cifre ed una lista di basi della stessa lunghezza.
    Calcola il valore intero che corrisponde come spiegato prima.
    Parameters
    digits : List[int]    lista di cifre da convertire
    bases   : List[int]    lista di basi della stessa lunghezza
    Returns
    int                    il valore intero corrispondente

    Esempio: decode_digits( [1, 1, 2], [2, 3, 4] ) -> 36
        infatti   1*2^0 + 1*3^1 + 2*4^2 = 36
    '''
    
    result : list[int] = []
    
    
    # ITERATIVE STYLE
    #temp = powBases(bases)
    #print(temp)
    temp = list(zip(digits,powBases(bases)))
    
    for i in temp:
        result.append(i[0] * i[1])
    # temp3 = list(map(mulTuple, temp2))
    # print(temp3)
    # print (temp2)
    # index = 0
    # for i in digits:
    #     result.append(i * temp2[index])
    #     index += 1
    
    return sum(result)   #iterative
    
    # MORE FUNCTIONAL
    # for i,j in enumerate(bases):
    #       #result.append(pow(j, i)) # append meno veloce  
    #       result += [pow(j,i)]
    
    # print(result)
    # result = list(zip(digits, result))
    
    # #sumTuple = (lambda x : x[0] * x[1])
    
    # result = sum(map(lambda x : x[0] * x[1], result)) #Da debaggare// Debuggato,ora funziona
    
    
    
    # return result #iterative

#----------------------------------------------------------------------------
# TO DO, WORK IN PROGRESS second function
def generateListUtil(listDigits : list[int]) -> list[int]:
    res : list[int] = []
    for i in listDigits:
        res.append([x for x in range(i)])
    return res
        

        
def combine(elems): #per adesso usa questa
    if len(elems) == 0:
        return [[]]
    result = []    
    subcombinations =  combine(elems[1:])
    for x in elems[0]:
        for y in subcombinations:
            result.append([x, *y])
    return result        

def generateLists(nu : int) -> list[int]: #used to generate a list in range of num
    res = list(map(int, range(nu)))
    return res

#FROM PYTHON DOCS -->>STUDIARE, PER ORA USO NEL CODICE
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield list(prod)


def generate_digits(bases : List[int] ) -> List[List[int]]:
    '''
    Data una lista di basi, genera la lista di tutte le possibili
    combinazioni di cifre compatibili con le basi date.  Ciascuna
    combinazione è una lista di cifre compatibili.  Ovvero per
    ciascuna posizione che corrisponde a una base B contiene una delle
    possibili cifre in [0..B-1]
    
    Esempio:  generate_digits([2, 5]) produce la lista
    [ [0, 0], [1, 0], [0, 1], [1, 1], [0, 2], [1, 2], [0, 3], [1, 3], [0, 4], [1, 4] ]

    Nota: l'ordine nella lista finale non conta e anche 
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]
    è una soluzione valida.
    '''
    pass

    listBases = [[x for x in range(i)] for i in bases]
    print(listBases)
    index = 1
    res = listBases[0]
    while index == len(listBases):
        list(product(res, listBases[index]))
    return res
    #Prova da Python Doc
    # if len(bases) == 0:
    #     return []
    
    # result = list(product(bases[0], bases[1]))
    # result += generateListUtil(bases[1:])
    
    # return result
    # if len(bases) == 1:
    #     return product(bases[0])
    
    # result : list = list(product(bases[0], bases[1]))
    # result.extend(product(bases[],bases[1]))
        
    # return result


    #provo a creare tutte liste di zeri e cambiare con gli indici
    # bases
    # res : list[int] = [0]
    
    
    
    
    #PSEUDO CODICE
    #Prova recursive
    #caso base, se vuota return []
    #se uno return x in range (x)
    #e faccio res += function(list[1:])
    #PROVA
    
    # if len(bases) == 0:
    #     return []
    
    # flatList : list[int] = []
    # flatList += list(map(generateLists, bases))
    
    # for i in range(len(flatList[0])):
    #     flatList[0].extend(flatList[1:])
    

    # result : list[int] = []

    # for x in bases:
    #     result += x in range(x) + generate_digits(bases[1:])

    # return flatList

    
    


    
    # flatList : list[int] = []
    # flatList += list(map(generateLists, bases))
    
    # result : list[int] = combine(flatList)
    
    # return result 
    
    
    # result  : list[int] = []
    # firstEl = [0] * len(bases)
    # result.append(firstEl)
    # for i in bases:
    #     [x for x in range(i)]
    
    # return result
    
    # PRATICAMENTE SI DEVE FARE UN PRODOTTO CARTESIANO
    
    
    
    # listsLimits : list[list] = generateListUtil(bases)
    # result = [[x, y] for x in ]
    
    
    #first try with nested or loops
    # res : list[int] = []
    
    # for i in range(bases[0]):
    #     for j in range(bases[1]):
    #         res.append([i,j])
    
    #return res
    
    
    #pass
    # first : int = bases[0]
    # second = bases[1]
    # res = [[i for i in range(second)] for j in range(first
    #                                                  )]
    # allNumb = lambda x,k : [x in range(k)]
    
    # prova = allNumb(2,3)
    # print(prova)  
    
    # return res



def find_doubles(bases : List[int]) -> Set[int]:
    '''
    Data una lista di basi, genera la lista di tutte le possibili
    combinazioni valide di cifre rappresentabili con quelle basi,
    converte ciascuna combinazione nell'intero corrispondente e cerca
    quali interi appaiono più volte.

    Ritorna l'insieme di valori interi che hanno più di una
    rappresentazione nelle basi date.

    Esempio: find_doubles([4, 3, 2]) -> {3, 4, 5, 6, 7, 8, 9, 10}
    Infatti, ad esempio il numero 10 con queste basi ha le due rappresentazioni 
    [3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
    [0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10
    '''
    # SCRIVI QUI IL TUO CODICE
    pass


###################################################################################
if __name__ == '__main__':
    pass
    #prova con 2 liste randomper le funzioni
    #list1digits = [random.randrange(0,100) for x in range(1000)]
    #list1bases = [random.randrange(0,100) for x in range(1000)]
    
    
    #First function works, need refactoring
    provaCode = decode_digits([1,1,2],[2,3,4])
    #provaCode2= decode_digits(list1bases,list1digits)
    print(provaCode)
    #---------------------------------------------------------------------
    #second function tests
    #prova2nd = generate_digits([2,5])
    #print(prova2nd)
    provaGenerate = generate_digits([2,5])
    provaGenerate2 = generate_digits([2,4,7])
    provaGenerate3 = list(product([0,1],[0,1,2,3,4],['a','b','c']))
    print(provaGenerate2)
    
    
    
    #--------------------------------------------------------------------
    # 3rd function tests
    
    
    
    # inserisci qui i tuoi test
    # se vuoi provare il tuo codice su piccoli dati
    # nota per eseguire questo main devi usare program.py
    # come cliente e non come modulo ossia con python program.py
