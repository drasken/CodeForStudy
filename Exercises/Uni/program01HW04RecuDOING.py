#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uno dei meccanismi utilizzati per conservare e gestire grandi
quantità di dati è costituito dai database. Esistono tantissimi
tipi di database, ma quello che ha rivoluzionato il settore è
costituito dai database organizzati secondo il modello relazionale
teorizzato da Codd ormai mezzo secolo fa. Secondo questo modello
i dati sono organizzati in tabelle e relazioni fra di esse, in
modo da ottimizzare le richieste di memoria, favorire la coerenza
dei dati e minimizzare gli errori.

Dobbiamo progettare un insieme di funzioni che implementi una
semplice forma di database relazionale di una scuola di formazione
in cui ci sono quattro tabelle, ovvero students, teachers, courses
ed exams. I database sono di tre diverse dimensioni, ovvero small,
medium e large. Le tabelle del database di dimensione dbsize sono
salvate in quattro file json <dbsize>_<nometabella>.json (ad esempio,
il db small è composto dai file small_students.json, small_teachers.json,
small_courses.json e small_exams.json). Le tabelle sono organizzate in
liste di dizionari (si veda ad esempio small_students.json) e hanno le
seguenti strutture:
    - students: chiavi stud_code, stud_name, stud_surname, stud_email
    - teachers: chiavi teach_code, teach_name, teach_surname, teach_email
    - courses: chiavi course_code, course_name, teach_code
    - exams: chiavi exam_code, course_code, stud_code, date, grade.
La relazione fra le tabelle implica che ogni riga in ognuna delle
tabelle ha un riferimento ad un'altra tabella: ad esempio, un esame
(exam_code) corrisponde ad un voto (grade) dato da un docente
(teach_code) ad uno studente (stud_code) per aver sostanuto
l'esame di un certo corso (course_code) in una certa data (date). Ogni
studente può aver sostenuto diversi esami. Ogno docente può tenere
diversi corsi. Ogni corso è tenuto da un solo docente.

Il campo stud_code è una chiave primaria per la tabella students poiché
identifica univocamente uno studente, ovvero non esistono due studenti
con lo stesso stud_code. Similmente, teach_code, course_code ed exam_code
sono le chiavi primarie rispettivamente delle tabelle teachers, courses ed
exams. Per questo motivo, tali campi vengono utilizzati per realizzare
la relazione fra le tabelle.

Inoltre, i campi in tutte le tabelle non sono mai vuoti.

Dobbiamo realizzare alcune funzioni per poter interrogare i database delle
diverse dimensioni. Quindi, le funzioni prevedono di usare sempre il
parametro dbsize di tipo stringa, che può assumere i valori 'small',
'medium' e 'large'. Le funzioni sono:
    - media_studente(stud_code, dbsize), che riceve una stud_code di
      uno studente e ritorna la media dei voti degli esami sostenuti,
      dallo studente.
    - media_corso(course_code, dbsize), che riceve un identificatore per un
      corso e ritorna la media dei voti degli esami per quel corso,
      sostenuti da tutti gli studenti.
    - media_docente(teach_code, dbsize), che riceve un identificatore
      di un docente e ritorna la media dei voti per gli esami
      sostenuti in tutti i corsi del docente.
    - studenti_brillanti(dbsize), che ritorna la lista delle matricole
      (stud_code) con una media di esami sostenuti superiore o uguale a 28,
      ordinate in modo decrescente per media e, in caso di parità, in
      ordine lessicografico per il cognome e il nome dello studente. In
      caso di ulteriore parità, si usi il valore numerico dello stud_code
      in ordine crescente.
    - stampa_esami_sostenuti(stud_code, dbsize, fileout), che riceve un
      numero di stud_code e salva nel file fileout la lista degli esami
      sostenuti dallo studente identificato dal valore stud_code.
      Le righe nel file devono essere ordinate in modo crescente
      per data di esame sostenuto e, in caso di stessa data, in ordine
      alfabetico. Il file ha una riga iniziale con il testo
       "Esami sostenuti dallo studente  <stud_surname> <stud_name>, matricola <stud_code>",
      mentre le righe seguenti hanno la seguente struttura
        "<course_name>\t<date>\t<grade>", in cui i campi sono allineati
      rispetto al nome del corso più lungo (ovvero tutte le date e
      i voti sono allineati verticalmente). La funzione ritorna
      il numero di esami sostenuti dallo studente.
    - stampa_studenti_brillanti(dbsize, fileout), che salva nel file
      fileout una riga per ogni studente con una media di esami
      sostenuti superiore o uguale a 28. Le righe nel file
      devono essere ordinate in modo decrescente per media e,
      in caso di parità, in ordine lessicografico per il
      cognome e il nome dello studente.
      Le righe nel file hanno la seguente struttura:
          "<stud_surname> <stud_name>\t<media>", in cui il valore media
      è allineato verticalmente per tutte le righe. La funzione
      ritorna il numero di righe salvate nel file.
    - stampa_verbale(exam_code, dbsize, fileout), che riceve un identificatore
      di esame e salva nel fileout le informazioni relative
      all'esame indicato, usando la seguente formula
        "Lo studente <stud_surname> <stud_name>, matricola <stud_code>, ha sostenuto in data <date> l'esame di <course_name> con il docente <teach_surname> <teach_name> con votazione <grade>."
      La funzione ritorna il voto dell'esame associato
      all'identificatore ricevuto in input.

Tutte le medie devono essere arrotondate alla seconda cifra decimale,
anche prima di ogni funzione di ordinamento.
Tutti i file devono avere encoding "utf8".
Per stampare agevolmente righe allineate considerare la funzione format con
i modificatori per l'allineamento (https://pyformat.info/#string_pad_align)
e con i parametri dinamici (https://pyformat.info/#param_align).
"""
import json

def media_studente(stud_code, dbsize):
    # return average for specific student 
    #basically, open the json file corresponding to the param size
    #for each dictionary if the corresponding student code is found append grade value ti res list
    #round each float to he second digit
    #return the average value of the student grades
    
    # print(f'check for code: {stud_code}')
    # print(f'check for size: {dbsize}')
    fileName = f'{dbsize}_exams.json' #the file to open
    resList = [] #the list in wich append each grade
    with open(fileName, 'r') as f:

        content = json.load(f)
        #print(content)
        for i in range(len(content)):
            #print(content[i])
            if content[i]['stud_code'] == stud_code:
                #resList.append(i)
                resList.append(content[i]['grade'])
    average = round(sum(resList)/ len(resList), 2)
    return average
        
    pass

def media_corso(course_code, dbsize):
    #cycle for loop exams dictionary
    #for each elements of the dict check the course_id key
    #if course_code == param append grade to list result
    #return 
    filename = f'{dbsize}_exams.json'
    resultList = []
    with open(filename, 'r') as f:
        content = json.load(f)
        for i in range(len(content)):
            if content[i]['course_code'] == course_code:
                resultList.append(content[i]['grade'])
    average = round(sum(resultList) / len(resultList), 2)
    return average
    pass

def media_docente(teach_code, dbsize):
    #extract the course code for each teacher's course
    #save in a list, each teac maybe multiple courses
    #than use the same logic search for each exam if code in listCourse append to result
    #use func mediacorso?
    fileName = f'{dbsize}_courses.json'
    coursesLegit = []
    averagesForTotalGrades = []
    with open(fileName, 'r') as file:
        content = json.load(file)
        for i in range(len(content)):
            if content[i]['teach_code'] == teach_code:
                coursesLegit.append(content[i]['course_code'])
        #print(coursesLegit)
        # for j in coursesLegit:
        #     averagesForTotalGrades.append(media_corso(j, dbsize))
        #using the function return not expected value, changing approach
    
    examsName = f'{dbsize}_exams.json'
    with open(examsName, 'r') as f2:
        cont = json.load(f2)
        for j in range(len(cont)):
            if cont[j]['course_code'] in coursesLegit:
                averagesForTotalGrades.append(cont[j]['grade'])
        
    #print(averagesForTotalGrades)
    totalAverages = round(sum(averagesForTotalGrades) / len(averagesForTotalGrades), 2)
    return totalAverages
    pass

def studenti_brillanti(dbsize): #works, just timeout error, need refactoring
    #fare check della media per ogni studente
    #se media >= 28 tieni studente
    #nella lista memorizza ogni informazione studente
    #ordina in baseordinate in modo decrescente per media --> FIRST
    #in caso di parità, in ordine lessicografico per il cognome e il nome dello studente.
    #In caso di ulteriore parità, si usi il valore numerico dello stud_code in ordine crescente.
    #una volta ordinato tutto, ritorna solo gli stud_code
    
    allStudentCode = [] #save here all extracted stud_code
    topStudents = [] #save here top stundent stud_code only
    topAverage = []
    topStudentsDict = [] #save only top students profile
    topStudentsRanked = []
    
    fileName = f'{dbsize}_students.json'
    
    with open(fileName, 'r') as file:
        content = json.load(file)
        for i in range(len(content)):
            allStudentCode.append(content[i]['stud_code']) #added all stud_code
        
        for j in allStudentCode:
            if media_studente(j, dbsize) >= 28:
                topStudents.append(j)
                topAverage.append(media_studente(j, dbsize))
        
        for k in range(len(content)):
            if content[k]['stud_code'] in topStudents:
                topStudentsDict.append(content[k])
        studentsAndAverage = list(zip(topStudentsDict, topAverage)) #tuple (studProfile, average)
        studentsAndAverage.sort(key=lambda x: (-x[1], x[0]['stud_surname'], x[0]['stud_name'], int(x[0]['stud_code'])))
        for z in range(len(studentsAndAverage)):
            topStudentsRanked.append(studentsAndAverage[z][0]['stud_code'])
        
        #IN PROGRES FROM HERE
        #Use the zipped list for sort the list, than sort by [0] element of the 2
        # topStudents = sorted(topStudents, key=lambda x: (x['grade'], x['']))    
    return topStudentsRanked
    pass

def stampa_verbale(exam_code, dbsize, fileout):
    pass

def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    pass 

def stampa_studenti_brillanti(dbsize, fileout):
    pass



#test per prima funzione
prova = media_studente('1803891', 'small')
print(prova) #expected average of 22,26,23,24

#test seconda funzione
prova2 = media_corso('TIPAPFC0xa0bb4a', 'small')
# data: 22+21+31+27+31+24+19+27+19
print(prova2)
prova2B = media_corso('CELE0xc62458', 'medium')
print(prova2B)
prova2C = media_corso('MASP0x6f69a0', 'large')
print(prova2C)

#test per la terza funzione
prova3A = media_docente('003', 'small')
print('test 3')
print(prova3A)
# print(type(prova3A))
#expected courses: EDIELFAC0x5203a7, SOM0x835db8, SNL0xadd7c7
prova3 = media_docente('001', 'small')
print(prova3)
#expected courses: MP0x3702b5,TIPAPFC0xa0bb4a
#test passed with print not test lib

#test per la funzione 4
prova4 = studenti_brillanti('small')
print('test 4')
print(prova4)
