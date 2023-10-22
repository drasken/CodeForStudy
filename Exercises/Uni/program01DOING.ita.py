# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

"""
Idea per risolvere il programa
lanciare un ciclo while che finchè fa somma < 10:
                                     if somma == 9 -> res += 1

Provare anche in maniera ricorsiva, chiamare la fnzione finchè sum < 10 e return res = 0 se non sum == 9
                                                                     
"""



def ex1(int_seq:str, subtotal:int) -> int:
    newSeq : list[int] = [int(x) for x in int_seq if x.isdigit()]
    
    
    res : int = 0
    index_sx : int = 0
    arrLen: int = len(newSeq)
    
    for i in range(arrLen):
        tot : int = 0
        index_dx : int = index_sx + 1
        while tot <= subtotal and index_dx <= arrLen:
            tot = sum(newSeq[index_sx:index_dx])
            index_dx += 1
            if tot == subtotal:
                res += 1
        index_sx += 1
        
    return res
        

        
if __name__ == '__main__':
    # Inserisci qui i tuoi test personali
    try_int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
    val = ex1(try_int_seq, 9)
    provaL = [1,4,5,8,2,3,4,1,2,3,2,7,3,5,4,9,4,6,2]
    #testLC = [y in x[x for x in provaL if ]
    testComp = [[x for x in range(4)] for y in range(10)]
    print(val)
