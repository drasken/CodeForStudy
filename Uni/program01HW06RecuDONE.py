# -*- coding: utf-8 -*-
'''
I Caponians, una specie aliena proviente da un non ben specificato
pianeta della galassia, stanno pianificando da un bel po' l'invasione
del pianeta Terra. Per farlo, hanno creato e installato in vari punti
del pianeta varie *mind bending machine*, macchine che riducono
l'intelligenza degli umani attraverso la rete telefonica [1].

Terminata la fase di riduzione dell'intelligenza umana, il prossimo
passo verso la conquista della Terra sara' lo sbarco sul nostro
pianeta, che avverra' non appena i Caponians avranno trovato dei punti
sufficientemente spaziosi per far atterrare le loro astronavi.

Un'astronave vista dall'alto puo' essere rappresentata come un
rettangolo di dimensioni W (larghezza) e H (altezza). Nel considerare
lo spazio necessario ad un'astronave per atterrare vanno pero' aggiunti
sui 4 lati del rettangolo 4 aree in piu'. Le aree in piu' sono una una
per lato.
Le aree sporgono tutte di una stessa quantita' D, per permettere di
aprire su ogni lato un portellone di sbarco. Ogni portellone e' quindi
largo quanto il lato dell'astronave su cui si trova e lungo D, su
qualunque lato si trovi.

I Caponians vorrebbero sbarcare con le loro astronavi in alcune nostre
citta', di cui hanno scaricato le rispettive mappe. Una citta' puo'
essere rappresentata come un'immagine rettangolare nera, in cui ogni
palazzo e' rappresentato come un rettangolo colorato (ogni palazzo ha
un colore che lo identifica univocamente).

Per definire gli ultimi dettagli del piano di sbarco, i Caponians
hanno bisogno di un algoritmo che, data la mappa di una citta' e un
elenco di astronavi definite come sopra, confermi oppure no se
ciascuna astronave ha abbastanza spazio per atterrare in quella citta',
aprire i suoi 4 portelloni e sbarcare il suo contenuto. Le astronavi
non atterrano contemporaneamente nella citta', quindi vanno valutate
separatamente le une rispetto alle altre.

(1) Quindi, data un'immagine nera (citta') con dei rettangoli colorati
pieni (palazzi) disegnati sopra, con ogni rettangolo di un colore
diverso da tutti gli altri, bisognera':

- determinare posizione, dimensioni e colore di ogni rettangolo
- salvare in un file di testo un rettangolo per riga
- nel file, ogni rettangolo e' rappresentato con una sequenza di 7 valori:
     x, y, w, h, r, g, b
  separati da virgole, in ordine di coordinata y (numero di riga)
  decrescente e, a parimerito, di x (pixel della riga) crescente.

(2) Successivamente, e' dato un file di testo contente N terne di
interi.  Ogni terna separata internamente e dalle altre terne da un
qualunque numero di spazi, tabulazioni o ritorni a capo. Ogni terna
rappresenta larghezza W, altezza H e distanza minima D (vedere sotto)
di un rettangolo (astronave) che si vorrebbe aggiungere all'immagine
al punto (1):

- restituire una lista di N valori booleani, l'i-esimo valore nella
lista e' True se nell'immagine c'e' abbastanza spazio per inserire
l'i-esimo rettangolo

- un rettangolo puo' essere inserito nell'immagine se esiste almeno una
posizione nell'immagine in cui c'e' abbastanza spazio (cioe' un'area
costituita interamente da pixel neri) per contenere il rettangolo
stesso, piu' le 4 "estensioni" del rettangolo, ossia i 4 portelloni
dell'astronave.

Ad esempio, se un'astronave da inserire ha 2 pixel di
larghezza e 3 di altezza e D = 2, bisognera' cercare uno spazio
nell'immagine adatto a contenere la seguente figura:

                              **
                              **
                            **++**
                            **++**
                            **++**
                              **
                              **

in cui i simboli + sono i pixel del rettangolo/astronave 2x3 e i *
sono i pixel delle 4 estensioni/portelloni

Esempio:
Data la seguente immagine rappresentata con un carattere per ogni
pixel, dove "." e' un pixel nero mentre caratteri diversi da "." sono
pixel colorati (*=rosso, +=verde):

**....
**....
......
......
....++
....++

Il file con i rettangoli trovati da voi salvato deve contenere le
righe:
4,4,2,2,0,255,0
0,0,2,2,255,0,0

e dati le seguenti astronavi:

(3, 3, 0)
(2, 2, 4)
(1, 1, 3)
(4, 2, 1)
(2, 4, 1)

verra' restituita la lista: [True, False, False, False, False]
infatti solo la prima astronave puo' atterrare ad esempio nella
zona marcata da 'X' (non ha sportelloni, infatti D = 0)

**.XXX
**.XXX
...XXX
......
....++
....++

mentre le altre non entrano nella mappa perche', pur avendo un punto
in cui possono atterrare, non possono aprire tutti i portelloni


[1] https://en.wikipedia.org/wiki/Zak_McKracken_and_the_Alien_Mindbenders)
'''
# import copy
from pngmatrix import load_png8

#Part 1 -----------------------------------------------

def colourRect(lup_x : int, lup_y: int, width: int, height: int, table: list) -> None:
    #util function: after finding a rect saves coordinates setting values to black
    #params are coordinates of Left up angle and measures
    
    #default check and vaue is black, not using a variable, change if needed
    
    for rowNum, row in enumerate(table[lup_y: lup_y + height]):
        for columnNum, color in enumerate(row[lup_x: lup_x+ width]):
            if color != (0,0,0):
                table[lup_y + rowNum][lup_x + columnNum] = (0,0,0)
    
    # for rowNum, row in enumerate(table[lup_y: lup_y+height]):
    #     for columnNum, elem in enumerate(row[lup_x: lup_x+width]):
    #         if elem != (0,0,0):
    #             table[lup_y + rowNum][lup_x + columnNum] = (0,0,0)
    
    
    #TO DEBUG, SECOND RECTANGLE NOT WORKING CORRECTLY
    pass

def calculateRect(y : int, x : int, table: list) -> tuple: #TODO!!!!!
    #function that calculate width and height of rectheight
    value = table[y][x]
    # pivot = 0
    height = 0
    width = 0
   
    #calculate width
    for j in table[y][x:]:
        if j == value:
            width += 1
        else:
            break
    #calculate height
    for i in table[y:]:
        if i[x] == value:
            height += 1
        else:
            break
    
    measures = (width,height)
    return measures
    pass

#implement a function for checking colour rectangle
def checkRectangle(table: list[list]) -> list:
    """


    Args:
        table (list[list]): the list descibing each pixel in a png

    Returns:
        list: the list of the rectangles found in the images.

    """
    black  = (0,0,0)
    #to do: function to calcuate rectangule mesures
    listRect = [] #here save each rect when found
    for numRow, row in enumerate(table): #get each raw
        for numColumn, color in enumerate(row):
            if color != black: #find a palace
                measures = calculateRect(numRow, numColumn, table)
                tempRectangle = (numColumn, numRow, measures[0], measures[1], color)
                listRect.append(tempRectangle) #save the rectangle found in listRect
                colourRect(numColumn, numRow, measures[0], measures[1], table) #use this to not calculate 2 times same rect
                
                # measures = calculateRect(numRaw, numColumn, table)
                # perimeter = sum(measures) * 2
                # tempRect = (perimeter, numRaw, measures[0], measures[1], color)
                # listRect.append(tempRect)
    
    listRect.sort(reverse=True, key= lambda x : (x[1], - x[0]))
            
    return listRect   

def formatPalacesStr(singleTuplePalace: tuple) -> str:
    
    x_num,y_num,width,height,color= singleTuplePalace
    r_num, g_num, b_num = color
    
    output = f'{x_num},{y_num},{width},{height},{r_num},{g_num},{b_num}\n'
    
    return output
    
    #format transform each palace from tuple to desired str output
    pass

def outputPalaces(listPalaces: list, fileName:str):
    #write on file the str representing the palaces
    
    with open(fileName, mode='w') as palaces:
        for i in listPalaces:
            str_out = formatPalacesStr(i)
            palaces.write(str_out)
            
    pass

#Part 2 --------------------------------------------------

def extractUfoFromFile(fileName: str) -> list: #function checked, it works
    #use this function to extract measures from file to use in script: list,str,tuple,etc what needed
    #the number representing UFOsare width hight padding
    
    result = []
    with open(fileName, mode='r') as file_ufo:
        list_ufo = file_ufo.readlines()
    
    for row in list_ufo:
        new_row = row.split() #split the rows, get the numbers and ignore black space
        if new_row: #is not black 
            result.extend(new_row)#add the numbers to the list
            
    result = [int(x) for x in result]
    
    result = [(result[i], result[i+1], result[i+2]) for i in range(0, len(result), 3)]    
    
    return result
    #done: return tuples with numbers: width, height, padding
    pass

def checkUfoLanding(singleUfo: tuple, matrix:list) -> bool:
    
    width,height,padding = singleUfo
    black = (0,0,0)
    setBlack = {black}
    
    for rowNum, row in enumerate(matrix):
        if rowNum < padding or rowNum > (len(matrix) - height - padding + 1):
            continue
        for columnNum, color in enumerate(row):
            if columnNum < padding or columnNum > (len(row) - width - padding + 1):
                continue
            if color != black:
                continue
            setElements = set()
            
            #check for vertical rect
            for i in matrix[rowNum - padding : rowNum + height + padding]:
                for j in i[columnNum: columnNum + width]:
                    setElements.add(j)
            
            #check horizontal rect
            for k in matrix[rowNum: rowNum + height]:
                for l in k[columnNum - padding: columnNum + width + padding]:
                    setElements.add(l)
            
            checkSet = setElements.difference(setBlack)
            if not checkSet:
                return True
            
    return False
    
    pass


def ex(file_png, file_txt, file_out):
    
    black = (0,0,0)
    white = (255,255,255)
    matrix = load_png8(file_png)
    # matrix2 = copy.deepcopy(matrix) #to delete
    
    listUfos = extractUfoFromFile(file_txt)
    resultBooleanList = []
    for ufo in listUfos:
        checkUfo = checkUfoLanding(ufo, matrix)
        resultBooleanList.append(checkUfo)
    
    listFromMatrix = checkRectangle(matrix) 
    outputPalaces(listFromMatrix, file_out)

    
    
    return resultBooleanList#,matrix2,listFromMatrix
    # return listFromMatrix,matrix,listUfos,resultBooleanList

    pass

if __name__ == "__main__":
    
    provaExample = ex('images/example.png', 'rectangles/example.txt', 'example.txt')
    
    provaTest0 = ex('images/image0.png', 'rectangles/rectangles0.txt', 'prova0.txt')
    
    provaTest1 = ex('images/image1.png', 'rectangles/rectangles1.txt', 'prova1.txt')


    provaTest3 = ex('images/image3.png', 'rectangles/rectangles3.txt', 'prova3.txt')

    
    # provaTest5 = ex('images/image5.png', 'rectangles/rectangles5.txt', 'prova5.txt')
    # provaTest6 = ex('images/image6.png', 'rectangles/rectangles6.txt', 'prova6.txt')
    
    provaTest9 = ex('images/image9.png', 'rectangles/rectangles9.txt', 'prova9.txt')

    pass
