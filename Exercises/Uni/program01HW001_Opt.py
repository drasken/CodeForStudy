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
    
    newSeq : list[str] = int_seq.split(sep=',')
    newSeq : list[int] = [int(x) for x in newSeq]
    
    
    res : int = 0
    arrLen: int = len(newSeq)
    
    for i in range(arrLen):
        tot : int = 0
        for j in range(i, arrLen):
            tot += newSeq[j]
            if tot == subtotal:
                res += 1
            elif tot > subtotal:
                break
                
        
    return res
        

        
if __name__ == '__main__':
    pass
    # Inserisci qui i tuoi test personali
    # try_int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
    # try_int_seq2='3,0,4,0,9'    
    # pytest05 = "433,159,651,0,0,858,0,0,0,0,626,824,0,24,497,926,837,72,122,572,84,749,642,0,0,0,0,0,299,127,19,849,0,0,0,969,883,0,0,0,0,0,0,0,0,0,0,0,630,168,31,0,993,53,0,0,935,0,0,355,209,0,433,0,0,91,636,671,0,654,0,0,0,0,618,0,362,0,0,207,0,688,82,114,127,0,870,0,86,345,0,0,155,253,0,802,375,255,919,0,244,0,482,0,858,0,0,502,109,34,0,0,0,0,588,0,583,899,127,574,252,0,0,0,0,0,587,0,0,0,0,612,676,0,0,0,735,0,0,712,974,893,441,260,405,153,0,0,902,0,0,360,541,377,306,180,526,495,0,0,0,0,0,431,0,479,0,569,0,0,0,0,0,296,0,0,0,289,15,0,402,0,542,0,543,0,0,0,411,357,537,0,0,0,565,752,48,0,275,0,449,691,0,435,0,0,701,0,18,0,119,0,758,73,773,0,648,677,0,678,0,0,0,741,22,0,0,425,100,0,96,312,0,355,0,0,0,15,0,0,0,0,401,906,362,310,324,0,539,0,619,181,972,0,57,316,0,34,997,11,0,688,149,0,357,0,0,48,0,230,0,0,192,754,349,501,0,456,36,0,0,0,0,0,0,0,117,0,0,918,0,0,180,686,0,819,721,951,0,260,0,135,0,0,17,318,826,0,0,0,0,0,0,781,820,0,114,655,148,0,0,167,772,0,0,0,0,0,201,0,14,262,794,0,0,0,803,0,296,0,0,0,287,0,0,0,867,757,0,0,0,0,0,772,0,0,0,653,0,693,0,422,834,29,0,0,698,969,857,0,232,0,137,0,880,64,0,0,67,0,435,552,677,286,383,271,0,0,0,0,303,0,685,0,0,0,0,0,0,0,0,839,494,89,388,392,0,699,907,0,40,401,465,0,653,0,0,939,751,212,557,432,0,960,0,846,847,0,0,260,0,701,278,0,87,0,0,631,0,274,0,417,0,75,0,0,847,912,0,521,387,960,214,0,873,639,355,310,0,786,634,712,302,0,0,0,0,0,406,591,470,413,0,819,0,0,0,0,0,0,0,118,375,893,135,0,452,0,407,322,240,0,0,0,948,352,915,0,993,0,0,0,877,0,0,595,0,0,0,0,0,515,965,0,161,0,0,0,255,0,0,112,276,0,0,0,210,869,0,0,746,98,969,0,0,0,0,0,203,591,644,0,0,0,0,651,301,0,141,500,0,0,800,327,0,0,0,519,0,327,0,156,526,0,0,0,525,0,331,369,498,215,911,530,0,0,0,0,665,0,274,264,0,0,854,745,0,712,930,722,621,0,876,50,647,0,0,219,313,0"
    # val = ex1(pytest05, 660)
    # provaL = [1,4,5,8,2,3,4,1,2,3,2,7,3,5,4,9,4,6,2]
    # #testLC = [y in x[x for x in provaL if ]
    # testComp = [[x for x in range(4)] for y in range(10)]
    # print(val)
