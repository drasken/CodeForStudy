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

def stampa_verbale(exam_code, dbsize, fileout): #IT WORKS
    """
    stampa_verbale(exam_code, dbsize, fileout), che riceve un identificatore
      di esame e salva nel fileout le informazioni relative
      all'esame indicato, usando la seguente formula
        "Lo studente <stud_surname> <stud_name>, matricola <stud_code>, ha sostenuto in data <date> l'esame di <course_name> con il docente <teach_surname> <teach_name> con votazione <grade>."
      La funzione ritorna il voto dell'esame associato
      all'identificatore ricevuto in input.

    """
    #return Int is correct, error returned prob by formatting
    
    filename = f'{dbsize}_exams.json'
    
    with open(filename, mode='r') as f:
        content = json.load(f)
        esame = [x for x in content if x['exam_code'] == exam_code]
        #need to get course name from course code
        
    #need to get student name and surname from stud code
    student = esame[0]['stud_code']
    
    with open(f'{dbsize}_students.json', mode='r') as stud:
        studentContent = json.load(stud)
        studentContent = [x for x in studentContent if x['stud_code'] == student]
        name = studentContent[0]['stud_name']
        surname = studentContent[0]['stud_surname']
    
    date = esame[0]['date']
    grade = esame[0]['grade']
    
    #TODO: to get the course name
    courseId = esame[0]['course_code']
    with open(f'{dbsize}_courses.json', mode='r') as course:
        cour = json.load(course)
        cour = [x for x in cour if x['course_code'] == courseId]
        courseName = cour[0]['course_name']
        teachId = cour[0]['teach_code']
    
    #TODO: to get the teach info
    
    with open(f'{dbsize}_teachers.json', mode='r') as teach:
        teac = json.load(teach)
        teac = [x for x in teac if x['teach_code'] == teachId]
        teachName = teac[0]['teach_name']
        teachSurname = teac[0]['teach_surname']
        
    output = f"Lo studente {name} {surname}, matricola {student}, ha sostenuto in data {date} l'esame di {courseName} con il docente {teachName} {teachSurname} con votazione {grade}."
        
    with open(fileout, mode='w', encoding='utf8') as out:
        out.writelines(output)
        
    return grade
        
    
    pass

def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    """
    stampa_esami_sostenuti(stud_code, dbsize, fileout), che riceve un
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

    """
    
    fileName = f'{dbsize}_exams.json'
    
    with open(fileName, mode='r') as f:
        content = json.load(f)
    
    results = [x for x in content if x['stud_code'] == stud_code] #all exam for a specific student
    results.sort(key= lambda x : (int(x['date'][:4]), int(x['date'][5:7]), int(x['date'][-2:]), x['course_code']))
    
    with open(f'{dbsize}_students.json', mode='r') as st: #get the student informations
        studCredentials = json.load(st)
        studCredentials = [x for x in studCredentials if x['stud_code'] == stud_code]
        #use this for extract param for output in first string 
    
    surname, name= studCredentials[0]['stud_surname'], studCredentials[0]['stud_name']  
    
    #now need to get the course information
    
    desired_courses = []
    for ex in results:
        desired_courses.append(ex['course_code'])
        
    with open( f'{dbsize}_courses.json') as co:
        courses = json.load(co)
        courses = [x for x in courses if x['course_code'] in desired_courses]
    
    to_print_course = {x['course_code']:x['course_name'] for x in courses}
    
    max_length_course = len(max(to_print_course.values(), key=len)) 
        
    
    #use the studCredential variable for this params
    output = f"Esami sostenuti dallo studente {surname} {name}, matricola {stud_code}\n"
    with open(fileout, mode='w', encoding='utf8') as out:
        #need to write output file
        out.writelines(output)
        for ex in results:
            co_name = ex['course_code']
            co_name = to_print_course[co_name]
            extratLine = lambda x : (x['date'], x['grade'])
            toAddString = extratLine(ex)
            diff_name = max_length_course - len(co_name)
            riempitivo = ' ' * diff_name
            lineToAdd = co_name + riempitivo + '\t' + toAddString[0] + '\t' + str(toAddString[1]) + '\n'
            out.writelines(lineToAdd)
            
    #apparently it's done!
    #need to adjust each column        
    
    return len(results) #this return the number of exams taken
    
    pass 

def stampa_studenti_brillanti(dbsize, fileout):
    """
    stampa_studenti_brillanti(dbsize, fileout), che salva nel file
      fileout una riga per ogni studente con una media di esami
      sostenuti superiore o uguale a 28. Le righe nel file
      devono essere ordinate in modo decrescente per media e,
      in caso di parità, in ordine lessicografico per il
      cognome e il nome dello studente.
      Le righe nel file hanno la seguente struttura:
          "<stud_surname> <stud_name>\t<media>", in cui il valore media
      è allineato verticalmente per tutte le righe. La funzione
      ritorna il numero di righe salvate nel file.

    Args:
        dbsize (TYPE): DESCRIPTION.
        fileout (TYPE): DESCRIPTION.

    Returns:
        None.

    """
    
    listStudentiBrillanti = studenti_brillanti(dbsize)
    
    studentsList = []
    with open(f'{dbsize}_students.json', mode='r') as f:
        students = json.load(f)
        for brill in listStudentiBrillanti:
            for stud in students:
                if brill == stud["stud_code"]:
                    media = media_studente(brill, dbsize)
                    studentData = (stud["stud_surname"], stud["stud_name"], media)
                    studentsList.append(studentData)
                    break
    
    maxLengthName = 0
    
    for persona in studentsList:
        lunghezza = len(persona[0]) + 1 + len(persona[1])
        if lunghezza > maxLengthName:
            maxLengthName = lunghezza
        
    with open(fileout, mode='w') as out:
        for data in studentsList:
            surname = str(data[0])
            name = str(data[1])
            average = str(data[2])
            spazioNome = maxLengthName - (len(name) + 1 + len(surname))
            riempitivo = ' ' * spazioNome
            linea = f'{surname} {name}' + riempitivo + '\t' + f'{average}\n'#.format(stud_surname= surname, stud_name= name, media= average )
            out.write(linea)

    
    return len(listStudentiBrillanti)
    
    # riga = "<stud_surname> <stud_name>\t<media>"
    # #TODO ALLINEA MEDIA VOTO UNA CON L'ALTRA
    
    # allStudentCode = []
    # topStudents = []
    # topAverage = []
    # studentsNames = []
    # studentSurnames = []
    
    # fileToOpen = f'{dbsize}_students.json'
    
    # with open(fileToOpen, 'r') as file:
    #     content = json.load(file)
    #     for i in range(len(content)):
    #         allStudentCode.append(content[i]['stud_code']) #added all stud_code
        
    #     for j in allStudentCode:
    #         if media_studente(j, dbsize) >= 28:
    #             topStudents.append(j)
    #             topAverage.append(media_studente(j, dbsize))
    #             #TODO!!!!! GET NAME AND SURNAME FROM HERE(?)
    
    # for y in range(len(content)):
    #     if content[y]['stud_code'] in topStudents:
    #         studentsNames.append(content[y]['stud_name'])
    #         studentSurnames.append(content[y]['stud_surname'])
    
    # studentAndGrade = list(zip(studentSurnames,studentsNames,topAverage)) 
    # studentAndGrade.sort(key=lambda x : (-int(x[2]), x[0], x[1]) )
    
    # with open(fileout, mode='a') as f:
    #     for i in studentAndGrade:
    #         name = i[1]
    #         surname = i[0]
    #         grade= i[2]
    #         tempRiga = f"{surname} {name}\t{grade}"
    #         spazioLunghezza = ' ' * (60 -len(tempRiga))
    #         tempRiga = f"{surname} {name}" + spazioLunghezza + f"\t{grade}\n" 
    #         f.writelines(tempRiga)
    
    # with open(fileout, mode='r') as fOut:
    #     result = fOut.readlines()
        
    # return len(result)
    # pass



#test per stampa studenti brillanti 

provaStampaStudendiBrillantiSmall = stampa_studenti_brillanti('small', 'provaBrillantiSmall.txt')
provaStampaVerbale = stampa_verbale(447, 'small', 'provaStampaVerbale.txt')


if __name__ == '__main':
    
    pass

#OLD TEST
# #test per prima funzione
# prova = media_studente('1803891', 'small')
# print(prova) #expected average of 22,26,23,24

# #test seconda funzione
# prova2 = media_corso('TIPAPFC0xa0bb4a', 'small')
# # data: 22+21+31+27+31+24+19+27+19
# print(prova2)
# prova2B = media_corso('CELE0xc62458', 'medium')
# print(prova2B)
# prova2C = media_corso('MASP0x6f69a0', 'large')
# print(prova2C)

# #test per la terza funzione
# prova3A = media_docente('003', 'small')
# print('test 3')
# print(prova3A)
# # print(type(prova3A))
# #expected courses: EDIELFAC0x5203a7, SOM0x835db8, SNL0xadd7c7
# prova3 = media_docente('001', 'small')
# print(prova3)
# #expected courses: MP0x3702b5,TIPAPFC0xa0bb4a
# #test passed with print not test lib

# #test per la funzione 4
# prova4 = studenti_brillanti('small')
# print('test 4')
# print(prova4)

# #test per la funzione 5
# print('test for function 5')
# print()
# prova5 = stampa_esami_sostenuti('1803891', 'small', 'fileout')
# print(prova5)

# #test per la funzione 6
# print('test for function 6')
# print()
# prova6 = stampa_verbale(447, 'small', 'fileout')
# print(prova6)

#test per la funzione 7
print()
print('test per la funzione 7')
prova7 = stampa_studenti_brillanti('small', 'fileout.txt')
print(prova7)
