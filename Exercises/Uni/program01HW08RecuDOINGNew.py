#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Una proprietaria terriera in California, Lida, eredita un
appezzamento di terreno. La superficie è modellata come un lotto
rettangolare di grandezza variabile. Il lotto di terra è
rappresentato come un'immagine codificata come lista di liste.

Per far fruttare l'appezzamento di terra, Lida decide di affittare la
terra ad altre persone. Per fare ciò, può decidere di dividere la
terra in quattro parti. Nel caso in cui decida di non affittare la sua
proprietà nessuna divisione è effettuata. Al contrario, nel caso in
cui la proprietà venga divisa in quattro sotto parti, delle linee di
demarcazione colorate vengono create, per tutelare i confini, appunto.
Le linee hanno uno spessore di un solo pixel. Non è dato sapere come
e dove le line verranno poste (non vi è una regolarità), e neppure
sappiamo quale è il colore che verrà usato a priori.  Conosciamo
solamente che le linee sono allineate agli assi.

I quattro locatari che ricevono le quattro proprietà potrebbero
prendere la solita decisione che Lida ha preso in precedenza oppure
no: essi potrebbero subaffittare ancora una volta le loro piccole
proprietà ad altre persone, oppure, potrebbero decidere di tenere la
terra tutta per loro. La decisione della suddivisione per ogni
locatario è indipendente alle altre. Per esempio, il locatario #1 può
decidere di subaffittare ancora, mentre il locatario #2 può tenere la
proprietà, mentre i locatari #3, #4 possono suddividere ancora. Quello
che sappiamo è che se subaffittano, dividono sempre in quattro
parti. Infatti, nel caso in cui dividano ancora la proprietà,
seguiranno una strategia simile di impostare i loro confini tracciando
delle linee di demarcazione degli stessi. Sicuramente useranno un
colore che è diverso dai colori usati da Lida (e da altri eventuali in
precedenza) tuttavia i quattro locatari usano il solito colore fra
loro, allo stesso livello di suddivisione.

NOTA: E' importante ricordare che il colore del background (bg) dell'
appezzamento non è dato (cioè non sappiamo a priori se il bg è
nero, bianco oppure blue). Sappiamo però che il colore di background
della terra NON è usato da nessuno dei locatari (ne da Lida) per
marcare i confini.

Il processo di suddivisione può continuare fino a quando tutti i
locatari in tutte gli appezzamenti decidono di smettere col subaffitto.
Questo processo descritto fino ad ora, ci porta all'immagine che è
data in input al vostro programma.

NOTA: Potete assumere che l'ipotetico appezzamento di terreno più
piccolo (rettangolo più piccolo possibile) abbia il lato più corto di
due pixel.

Riflettete bene sul problema e una volta che siete sicuri di una
soluzione, progettate su carta una soluzione (questa soluzione poi
deve essere descritta nella pseudo codice) e poi implementate un
programma ex1(input_file, output_file) che:
   - legge il file indicato dal parametro 'input_file' usando
     il modulo libreria 'images'.
   - pre-processa l'immagine, se necessario, e implementa una funzione
     *ricorsiva* per risolvere i requisiti sottostanti.
   - si deve contare tutte gli appezzamenti di terra che sono nell'
     immagine e restituire questo conteggio. Il programma deve
     restituire il numero di rettangoli con il colore del background
     dell'immagine che vi sono presenti. Riferendosi alla figura
     semplificata sottostante:

        # +++++++++++++++++++
        # +-1-|-2-|---------+
        # ++++a+++|----5----+
        # +-3-|-4-|---------+
        # ++++++++b++++++++++
        # +-------|--7-|-8--+
        # +---6---|++++c+++++
        # +-------|-10-|-9--+
        # +++++++++++++++++++
  
    l'approccio deve restituire un intero che corrisponde a 10 in
    questo caso (numero totale di rettangoli). I numeri posti nella
    figura soprastante sono stati inseriti solo per chiarire il
    concetto. (I dati sono privi di tali numeri inseriti, ovviamente).
    - infine, dato che l'agenzia immobiliare deve registrare
    tutti i confini che sono creati, il programma deve costruire un'
    immagine di output di grandezza 1x(N+1). L'immagine codifica come
    primo pixel il colore del background. Poi, deve codificare la
    gerarchia dei colori di tutti gli N colori usati per suddividere
    la terra in sotto rettangoli. La gerarchia dei colori e' definita
    "visitando" prima in profondita' il lotto in alto a sx, poi in
    alto a dx, poi in basso a sx, e infine in basso a dx. I colori
    devono essere salvati in ordine inverso rispetto alla visita
    effettuata. Con riferimento all'immagine semplificata precedente,
    assumendo che i colori dei confini di demarcazione siano descritti
    dalla lettere al loro centro, allora l'immagine di output deve
    contenere:
             out_colors = bg b c a


    Un altro esempio un pochino piu' complesso:

         +++++++++++++++++++++++++++++++++++++
         +-1-|-2-|---------|--------|--------+
         ++++a+++|----5----|---6----|----7---+
         +-3-|-4-|---------|--------|--------+
         ++++++++b+++++++++|++++++++c+++++++++
         +-------|--9-|-10-|--------|--------+
         +--8----|++++d++++|---13---|---14---+
         +-------|-11-|-12-|--------|--------+
         ++++++++++++++++++e++++++++++++++++++
         +-15|-16|---------|--------|-21|-22-+
         ++++f+++|---19----|---20---|+++g+++++
         +-17|-18|---------|--------|-23|--24+
         ++++++++h+++++++++|++++++++l+++++++++
         +-------|-26-|-27-|--------|-31-|-32+
         +--25---|++++m++++|---30---|+++n+++++
         +-------|-29-|-28-|--------|-33-|-34+
         +++++++++++++++++++++++++++++++++++++

         num. rect: 34
         gerarchia dei colori:
         bg e l n g h m f c b d a


NOTA: è vietato importare/usare altre librerie o aprire file tranne
quello indicato

NOTA: il sistema di test riconosce la presenza di ricorsione SOLO se
    la funzione/metodo ricorsivo è definita a livello esterno.  NON
    definite la funzione ricorsiva all'interno di un'altra
    funzione/metodo altrimenti fallirete tutti i test.
"""

import images

class rectangle():
    
    divLine = []
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    
        
    pass

#Util functions ------------------------------------------------

def checkIfDivisible(firstRow):
    # True if divisible else False
    blackSet = {(0,0,0)}
    
    firstRowSet = set(firstRow)
    if firstRowSet.difference(blackSet):
        return True
    
    return False


#main functions ------------------------------------------------

def findDivColor(matrix, rect_x, rect_y, width, height): #apparently it works
    #return color for divLine and index of that line
    #first find the color
    
    index_y = 0
    index_X = 0
    colorFound = 0
    for rowNum,row in enumerate(matrix[rect_y: rect_y + height]):
        if colorFound != 0:
            break
        for columnNum, color in enumerate(row[rect_x: rect_x + width]):
            if colorFound != 0:
                break
            if len(set(row)) == 1 and matrix[rect_y][rect_x + columnNum] == color:
                index_X = rect_x + columnNum
                index_y = rect_y + rowNum
                colorFound = color
                
    
    return color, index_y, index_X
    pass

def partitionRect():
    pass

# def recursiveCount(matrix):
    
#     count = 1
    
#     if not chechIfDivisible(matrix):
#         return count
    
#     subrect = partitionRect(matrix)
    
#     count += recursiveCount(subrect[0])
#     count += recursiveCount(subrect[1])
#     count += recursiveCount(subrect[2])
#     count += recursiveCount(subrect[3])
    
#     return count
#     #base case
    
#     #if not base case than this
#     pass

def recursiveCount(matrix, left_upper_x, left_upper_y, width, height):
    
    pass
    #base case
    count = 1
    listDiv = []
    
    if not checkIfDivisible(matrix[left_upper_y: left_upper_y + width]):
        return count, listDiv


def ex1(input_file,  output_file):
    
    decField = images.load(input_file)
    
    # for i,j in enumerate(decField):
    #     for k,l in enumerate(j):
    #         decField[i][k] = (0,0,0)
            
    boolTest = checkIfDivisible(decField)
    # res = recursiveCount(decField)
    
    return boolTest,decField
    pass


if __name__ == '__main__':
    
    testSmall01 = ex1('puzzles/small01.in.png', 'provaSmall01.png')
    provaDec = testSmall01[1]
    provaSeria = findDivColor(provaDec, 0, 0, 256, 256)
    
    provaMatrix = [[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)]] 
    provaMatrixDiv = [[(0,0,0),(1,0,0),(0,0,0),(0,0,0)],[(0,0,0),(1,0,0),(0,0,0),(0,0,0)],[(1,0,0),(1,0,0),(1,0,0),(1,0,0)],[(0,0,0),(1,0,0),(0,0,0),(0,0,0)]] 

    test = checkIfDivisible(provaMatrix)
    test2 = checkIfDivisible(provaMatrixDiv)
    
    test1B = findDivColor(provaMatrix, 0, 0, 4, 4)
    test2B = findDivColor(provaMatrixDiv, 0, 0, 4, 4)
    
    test1C = recursiveCount(provaMatrix, 0, 0, 4, 4)
    test2C = recursiveCount(provaMatrixDiv, 0, 0, 4, 4)
    
    # write your tests here
    pass


    