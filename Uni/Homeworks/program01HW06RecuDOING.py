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

"""

Note to self: nel file da stampare ogni riga per un palazzo in base a parametri
               
               x e y: pixel dell'angolo A-S
               x: # colonna angolo A-S se y1==y2 uso x ordine crescente
               y: angolo A-S # riga, decrescente
               w,h: altezza e larghezza del rettangolo
               r,g,b: i valori RGB del colore del rettangolo

2) Altro file contenente terne delle astronazi con:
               w: larghezza
               h: altezza
               d: distanza minima sui lati da mantere con gli edifici

        Return:
               - Lista di N valori boleani, ogni i-esimo True se astronave c'entra 


"""



from pngmatrix import load_png8

def colourRect(lup_y : int, lup_x: int, width: int, height: int, table: list) -> None:
    #util function: after finding a rect saves coordinates setting values to black
    #params are coordinates of Left up angle and measures
    
    #default check and vaue is black, not using a variable, change if needed
    
    for rawNum, raw in enumerate(table[lup_y: lup_y+height]):
        for columnNum, elem in enumerate(raw[lup_x: lup_x+width]):
            if elem != (0,0,0):
                table[lup_y + rawNum][lup_x + columnNum] = (0,0,0)
    
    
    #TO DEBUG, SECOND RECTANGLE NOT WORKING CORRECTLY
    pass

def calculateRect(x : int, y : int, table: list) -> tuple: #TODO!!!!!
    #function that calculate width and height
    #terurn a tuple of int
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
    
    meas = (height,width)
    return meas
    pass
    #Apparently it's working

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
    for numRaw, raw in enumerate(table): #get each raw
        for numColumn, color in enumerate(raw):
            if color != black: #find a palace
                measures = calculateRect(numRaw, numColumn, table)
                tempRectangle = (numRaw, numColumn, measures[0], measures[1], color)
                listRect.append(tempRectangle) #save the rectangle found in listRect
                colourRect(numColumn, numRaw, measures[1], measures[0], table) #use this to not calculate 2 times same rect
                
                # measures = calculateRect(numRaw, numColumn, table)
                # perimeter = sum(measures) * 2
                # tempRect = (perimeter, numRaw, measures[0], measures[1], color)
                # listRect.append(tempRect)
    
    listRect.sort(reverse=True, key= lambda x : (x[1], - x[0]))
            
    return listRect   

def extractRect(list_in_tuple : tuple) -> str:
    #use this function to translate tuple rect in a string to write in file
    #use tuple unpack
    
    x_num, y_num, wid, hig, color = list_in_tuple
    
    r_col, g_col, b_col = color
    
    str_output = f"{x_num},{y_num},{wid},{hig},{r_col},{g_col},{b_col}\n"
    
    return str_output
    
    pass

def printRect(listRect: list, fileName: str) -> None:
    with open(fileName, mode='a') as myFile:
        for i in listRect:
            str_out = extractRect(i)
            myFile.write(str_out)
        pass
    
    #return nothing wtite in the file



#Ideas algorithm for part2: ----------------------------------------------
    
    """
    basically you use a util function check inside rect to see id all black in a given area, is true 
    ufo can land else can't.
    the approach is the same as in part 1, we use the upper left corner of the rectangle and the measures
    from the file in input one each
    """

#end idea part 2 ----------------------------------------------------------


def extractUfoFromFile(fileName: str) -> list:
    #use this function to extract measures from file to use in script: list,str,tuple,etc what needed
    #the number representing UFOsare width hight padding
    
    result = []
    with open(fileName, mode='r') as file_ufo:
        list_ufo = file_ufo.readlines()
    
    for raw in list_ufo:
        new_raw = raw.split()
        if new_raw:
            result.extend(new_raw)
            
    result = [int(x) for x in result]
    
    result = [(result[i], result[i+1], result[i+2]) for i in range(0, len(result), 3)]    
    
    return result
    #done: return tuples with numbers
    pass

def checkInsideUfo(measuresUfo: tuple, table: list) -> bool:
    #this function check inside UFO shadow isall black or building
    #the returned bool is used for the parent returned list
    #DON'T ITERATE ON ELEMENTS!!! will use for in ex function!!!!
    
    #resultSet = set()
    width, height, padding = measuresUfo
    black = (0,0,0)
    
    #result = set() #use this set to add  colours found
    
    searchResult = {black}
    result = set()
    
    #need to use an eteernal function, the brack is not working
    restProva = []
    for rawNum, raw in enumerate(table): #is not space padding ignore
        if rawNum < padding or (len(table) -rawNum) < (height + padding):
            continue
        for columnNum, item in enumerate(raw): # is not space ignore
            if columnNum < padding or (len(raw) - columnNum) < (width + padding):
                continue
            # if len(raw[columnNum:]) < width:
            #     continue #break
            if item != black:
                continue #no free space, ignore it
            else: #this need improvment, maybe another function !!!!!!!!
                #here check Horizontal rect
                check_set = set()
                for hor_row in table[rawNum: height +1]:
                    for colour in hor_row[columnNum - padding: columnNum + width + padding +1]:
                        check_set.add(colour)
                
                for vert_rows in table[rawNum-padding: rawNum + height + padding +1]:
                    for colourVert in vert_rows[columnNum: columnNum + width + 1]:
                        check_set.add(colourVert)
                        
                check_set.difference_update(searchResult)
                if len(check_set) == 0:
                    return True
            
                pass
            
    return False
            
    #             check_up = True
    #             check_mid = True
    #             check_low = True
                
    #             for checkRaw in table[rawNum-padding:rawNum]:
    #                 if check_up == False:
    #                     break
    #                 for checkItem in checkRaw[columnNum:columnNum + width]:
    #                     if checkItem != black:
    #                         check_up = False
                
    #             for checkRawMid in table[rawNum: rawNum+height]: 
    #                 if check_mid == False or check_up == False:
    #                     break
    #                 for checkItemMid in checkRawMid[columnNum-padding: columnNum + width + padding]:
    #                     if checkItemMid != black:
    #                         check_mid = False
                
    #             for checkRawLow in table[rawNum+height: rawNum+height+padding]:
    #                 if check_low == False or check_mid == False or check_low == False:
    #                     break
    #                 for checkItemLow in checkRawLow[columnNum: columnNum+padding]:
    #                     if checkItemLow != black:
    #                         check_low = False
                
    #             if check_up == True and check_mid  == True and check_low == True:
    #                 return True
                
                
                        
    
    
    # return False
    
    
    
                #check upper square
                # checkVar = True
                # checkVarMid = True
                # checkVarLow = True

                # for checkRaw in table[rawNum-padding:rawNum+1]:
                #     for checkItem in checkRaw[columnNum:columnNum + width + 1]:
                #         result.add(checkItem)
                #     #     if checkItem == black:
                #     #         continue
                #     #     else:
                #     #         checkVar = False
                #     #         break
                #     #         # result = False
                #     #         # break
                #     # if not checkVar:
                #     #     break
                # #check mid rect
                # for checkRawMid in table[rawNum: rawNum+height+1]:
                #     # if table[rawNum: rawNum+height+1] >= height:
                #     #     continue
                #     # else:
                #     #     break
                #     # if not checkVar:
                #     #     break
                #     for checkItemMid in checkRawMid[columnNum-padding: columnNum+width+1]:
                #         # if checkRawMid[columnNum-padding: columnNum+width+1] >= width:
                #         #     continue
                #         # else:
                #         #     break
                #         if checkItemMid == black:
                #             result.add(checkItemMid)
                #         # else:
                #         #     checkVarMid = False
                #         #     break
                #             # result = False
                #             # break
                #     # if not checkVar:
                #     #     break
                # #check low square
                # for checkRawLow in table[rawNum+height: rawNum+height+padding+1]:
                #     # if not result and not checkVarMid:
                #     #     break
                #     for checkItemLow in checkRawLow[columnNum: columnNum+padding+1]:
                #         if checkItemLow == black:
                #             result.add(checkItemLow)
                #     #     else:
                #     #         checkVarLow = False
                #     #         break
                #     # if not checkVarLow:
                #     #     break
                # if result == searchResult:
                #     return True
                
                # result = set()
                
                # if checkVar and checkVarMid and checkVarLow:
                #     return True#if all for passed should be true
            
                # if rawNum == len(table) and columnNum == len(raw):
                #     return result
                # else:
                #     result = True
                
    pass

    #Done, to implement in function ex!!!!!

def ex(file_png, file_txt, file_out):
    """
    Docstring: TODO

    Args:
        file_png (TYPE): DESCRIPTION.
        file_txt (TYPE): DESCRIPTION.
        file_out (TYPE): DESCRIPTION.

    Returns:
        matrix (TYPE): DESCRIPTION.

    """
    """
    Algoritm: idea: convertire matrice triple in 0 e 1 setriple 000 -> 0 else 1
    poi usare indice pee vedere, finche in basso c'è 1 e tenere tracia degli indici
    tenere traccia degi angoli per non rischiare di contare 2 volte stesso rettangolo
    """
    matrix = load_png8(file_png)
    black = (0,0,0)
    white = (255,255,255)
    
    
    #here for omplementing returned list for cycle
    listUfos = extractUfoFromFile(file_txt)
    listBooleanUfo = []
    
    for i in listUfos:
        listBooleanUfo.append(checkInsideUfo(i, matrix))
    
    #new_matrix = [[0 if tup == (0,0,0) else 1 for tup in raw] for raw in matrix]
 
    list_buildings = checkRectangle(matrix)    
    
    # for m in list_buildings:
    #     i = extractRect(m)
    #     print(i)
    
    printRect(list_buildings, file_out)
    
    return listBooleanUfo

    pass

if __name__ == "__main__":
    
    testCheck = ex('images/image0.png', 'rectangles/rectangles0.txt', 'prova0.txt')
    print('ciao')
    print(testCheck)
    print('ciao')

    
    test = ex('images/example.png', 'rectangles/example.txt', 'prova2.txt')
    print(test)
    
    
    testCheck5 = ex('images/image5.png', 'rectangles/rectangles5.txt', 'prova5.txt')
    print('ciao 5555555555555555555')
    print(testCheck5)
    print('ciao')
    
    testCheck6 = ex('images/image6.png', 'rectangles/rectangles6.txt', 'prova6.txt')
    print('ciao 6666666666666666')
    print(testCheck6)
    print('ciao')
    #prova = calculateRect(4, 4, test)
    #prova2 = calculateRect(0, 0, test)
    test_real = ex('images/image0.png', 'rectangles/rectangles0.txt', 'prova0.txt')
    
    provaRead = extractUfoFromFile('rectangles/example.txt')
    provaRead2 = extractUfoFromFile('rectangles/rectangles0.txt')
    
    #use thi to test checkInsideUdo function, no not working
    listTest = load_png8('images/example.png')
    testMes = (3, 3, 0)
    testCheckUfo = checkInsideUfo(testMes, listTest)
    print('test check UFO')
    print(testCheckUfo)
    
    listTest6 = load_png8('images/image6.png')
    testMes6 = (3,3,1)
    testCheckUfo6 = checkInsideUfo(testMes6, listTest6)
    print('test check UFO6')
    print(testCheckUfo6)


    
    

    pass



