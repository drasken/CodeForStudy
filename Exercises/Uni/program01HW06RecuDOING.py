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

def colourRect(raw : int, column: int) -> None:
    #util function: after finding a rect saves coordinates setting values to black
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
                colourRect(measures[0], measures[1]) #use this to not calculate 2 times same rect
                
                # measures = calculateRect(numRaw, numColumn)
                # perimeter = sum(measures) * 2
                # tempRect = (perimeter, numRaw, measures[0], measures[1], color)
                # listRect.append(tempRect)
                
    return listRect   

def extractRect(listRect : tuple) -> str:
    #use this function to translate tuple rect in a string to write in file
    pass

def printRect(listRect: list, fileName: str) -> None:
    with open(fileName, mode='a') as myFile:
        pass
    
    #return nothing wtite in the file
    

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
    
    new_matrix = [[0 if tup == (0,0,0) else 1 for tup in raw] for raw in matrix]
 
    return matrix

    pass

if __name__ == "__main__":
    test = ex('images/image0.png', 'rectangles/rectangles0.txt', 'prova2.txt')
    test = ex('images/example.png', 'rectangles/example.txt', 'prova2.txt')
    print(test)
    prova = calculateRect(4, 4, test)
    prova2 = calculateRect(0, 0, test)
    pass
