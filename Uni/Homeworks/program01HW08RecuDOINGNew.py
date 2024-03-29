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

# class rectangle():
    
#     divLine = []
    
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
    
    
        
#     pass

#Util functions ------------------------------------------------

def checkIfDivisible(rectangle, angle_up_x, angle_up_y, width, bg_color) -> bool:
    # True if divisible else False
    bg_color_set = {bg_color}
    
    #firstElementSet = set()
    firstRowSet = set()
    
    for color in rectangle[angle_up_y][angle_up_x: angle_up_x + width]:
        firstRowSet.add(color)
    
    if firstRowSet.difference(bg_color_set):
        return True
    
    #can't do a deep copy so inspect first column instead of first row
    # for i in rectangle:
    #     firstElementSet.add(i[0])
    
    # if firstElementSet.difference(blackSet):
    #     return True
    
    #inspect first row
    # rectangleSet = set(rectangle[0])
    # if rectangleSet.difference(blackSet):
    #     return True
    
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
        if len(set(row[rect_x: rect_x + width])) != 1:
            continue
        for columnNum, color in enumerate(row[rect_x: rect_x + width]):
            if colorFound != 0:
                break
            if matrix[rect_y][rect_x + columnNum] == color:
                index_X = rect_x + columnNum
                index_y = rect_y + rowNum
                colorFound = color
                
    #colorFound = list(colorFound)
    return colorFound, index_y, index_X
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
    #local field 
    count = 0
    listDiv = []
    bg_color = matrix[left_upper_y][left_upper_x]
    
    #base case
    if not checkIfDivisible(matrix, left_upper_x, left_upper_y, width, bg_color):
        count += 1
        return count, listDiv
    
    # if not checkIfDivisible(matrix[left_upper_y: left_upper_y + height][left_upper_x: left_upper_x + width]):
    #     count += 1
    #     return count, listDiv
    
    #this var save color and coordinates y,x
    divLine = findDivColor(matrix, left_upper_x, left_upper_y, width, height)
    listDiv.append(divLine)
    divLine_x, divLine_y = divLine[2], divLine[1]
    
    #now do a recursive call on each subRect and add the returned values
    subrectUpLeft = recursiveCount(matrix, left_upper_x, left_upper_y, (divLine_x - left_upper_x), (divLine_y - left_upper_y))
    count += subrectUpLeft[0]
    
    subrectUpRight = recursiveCount(matrix, (divLine_x + 1), left_upper_y, (left_upper_x + width - divLine_x - 1), divLine_y - left_upper_y)
    count += subrectUpRight[0]
    
    subrectDownLeft = recursiveCount(matrix, left_upper_x, (divLine_y + 1), (divLine_x - left_upper_x), (left_upper_y + height - 1 - divLine_y))
    count += subrectDownLeft[0]
    
    subrectDownRight = recursiveCount(matrix, (divLine_x + 1), (divLine_y + 1), (left_upper_x + width - 1 - divLine_x) , (left_upper_y + height - 1 - divLine_y))
    count += subrectDownRight[0]
    
    #colors hierarchy
    listDiv.extend(subrectDownRight[1])
    listDiv.extend(subrectDownLeft[1])
    listDiv.extend(subrectUpRight[1])
    listDiv.extend(subrectUpLeft[1])



    
    return count, listDiv

def ex1(input_file,  output_file):
    
    decField = images.load(input_file)
    
   
    
    #find background color
    bg_color = decField[0][0]
    
    heightField = len(decField)
    widthField = len(decField[0])
    
    
    countedField = recursiveCount(decField, 0, 0, widthField, heightField)
    
    numFields = countedField[0]
    
    listColors = [bg_color]
    
    for col in countedField[1]:
        listColors.append(col[0])
        # putInsideList = [col[0]]
        # listColors.append(putInsideList)
    
    outputListColors = [listColors]
        
    
    
    images.save(outputListColors, output_file)
    #print(listColors)
    # for i,j in enumerate(decField):
    #     for k,l in enumerate(j):
    #         decField[i][k] = (0,0,0)
            
    #boolTest = checkIfDivisible(decField, 0, 0, 256)
    # res = recursiveCount(decField)
    
    return numFields#, listColors
    pass


if __name__ == '__main__':
    
    testSmall01 = ex1('puzzles/small01.in.png', 'provaSmall01.png')
    #provaDec = testSmall01[1]
    # ciaoooooo = 0
    # for num, i in enumerate(provaDec):
    #     if i[-1] == (255,0,0):
    #         ciaoooooo = num
        
    # provaSeria = findDivColor(provaDec, 0, 0, 256, 256)
    # provaRec = recursiveCount(provaDec, 0, 0, 256, 256)
    
    provaMatrix = [[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0)]] 
    provaMatrixDiv = [[(0,0,0),(1,0,0),(0,0,0),(0,0,0)],[(0,0,0),(1,0,0),(0,0,0),(0,0,0)],[(1,0,0),(1,0,0),(1,0,0),(1,0,0)],[(0,0,0),(1,0,0),(0,0,0),(0,0,0)]] 

    test = checkIfDivisible(provaMatrix, 0, 0, 4, (0,0,0))
    test2 = checkIfDivisible(provaMatrixDiv, 0, 0, 4, (0,0,0))
    
    test1B = findDivColor(provaMatrix, 0, 0, 4, 4)
    test2B = findDivColor(provaMatrixDiv, 0, 0, 4, 4)
    
    test1C = recursiveCount(provaMatrix, 0, 0, 4, 4)
    test2C = recursiveCount(provaMatrixDiv, 0, 0, 4, 4)
    
    # write your tests here
    pass


    