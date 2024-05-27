#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:46:09 2024

@author: drasken


Un sistema di e-cash consente agli utenti registrati di effettuare
    transazioni in valuta elettronica. Indicheremo la moneta elettronica in
    questione con il simbolo Ħ.
    Per il trasferimento di Ħ, gli utenti ricorrono ad agenti intermediari
    che gestiscono le transazioni al prezzo di una commissione. Le
    commissioni di transazione si basano su percentuali variabili, decise
    dagli intermediari.

Lo scopo di questo programma è quello di elaborare un registro delle transazioni
    tra gli utenti del sistema di e-cash che riporti:
    1) una lista con il saldo finale di ogni conto dei giocatori coinvolti;
    2) una lista con l'importo finale guadagnato da ogni intermediario;
    3) una lista in cui, per ogni intermediario, una lista annidata riporta i
       debiti residui dei conti del giocatore (0 se non è stato accumulato
       alcun debito, altrimenti un numero intero negativo).
    I risultati (1), (2) e (3) devono essere elementi di una tupla.

In particolare, deve essere progettata la seguente funzione:
     ex1 (acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log)
     dove
     - acn1, acn2 e acn3 sono i numeri di conto del giocatore 1, 2 e 3,
       rispettivamente;
     - imd_acn1 e imd_acn2 sono i numeri di conto degli intermediari 1 e 2,
       rispettivamente;
     - init_amount è l'importo iniziale nei conti dei tre giocatori
       (assumiamo che tutti i giocatori inizino con lo stesso importo iniziale);
     - i conti degli intermediari iniziano con un saldo di 0Ħ;
     - transact_log è un elenco di transazioni; ogni transazione è una tupla
       che consta dei seguenti elementi:
       · una coppia di numeri interi indicanti il numero del conto del
         mittente e il numero del conto del destinatario;
       · l'importo trasferito;
       · il numero del conto dell'intermediario;
       · la percentuale della commissione di transazione (da calcolare in
         base all'importo trasferito).

Ad esempio, la seguente tupla:
       ((0x44AE, 0x5B23), 800, 0x1612, 4)
     indica una transazione che trasferisce 800Ħ dal numero di conto 0x44AE al
     conto numero 0x5B23, con il servizio dell'intermediario che riceverà il
     4% di 800Ħ (quindi, 32Ħ) sul proprio conto a 0x1612.
     Di conseguenza,
     - il saldo del mittente (0x44AE) diminuirà di
         800 + 32 = 832Ħ,
     - il saldo del destinatario (0x5B23) aumenterà di
         800Ħ,
     - l'intermediario guadagnerà e depositerà sul proprio conto (0x1612)
         32Ħ.

Si noti che se i fondi nel conto del mittente sono insufficienti,
    la transazione viene dichiarata non valida dall'intermediario.
    L'intermediario riceverà comunque la commissione dal mittente, se ci sono
    abbastanza Ħ nel conto del mittente. Se il mittente non può pagare la
    commissione di transazione, l'intermediario riceverà tutti i fondi
    rimanenti e prenderà la sua parte dalle successive transazioni inviate al
    debitore fino al pagamento del debito. Considerando l'esempio precedente,
    se ci sono solo 700Ħ nel conto 0x44AE, l'intermediario guadagna 32Ħ e
    l'importo in 0x44AE diminuisce a 668Ħ. Se ci sono solo 10Ħ nel conto
    0x44AE, l'intermediario guadagna 10Ħ e l'importo in 0x44AE diminuisce a
    0Ħ; inoltre, l'intermediario mantiene un credito di 22Ħ con il mittente. Il
    mittente sarà obbligato a rimborsare i 22Ħ ottenendo l'importo dovuto
    dalle transazioni ricevute successivamente fino all'estinzione del debito.

    Se si accumula un debito nei confronti di due intermediari, i fondi vanno
    per primo all'intermediario che ha il credito più elevato e il resto va
    all'altro intermediario. Ad esempio, se il giocatore 1 deve 300Ħ
    all'intermediario 1 e 200Ħ all'intermediario 2, quando il giocatore 1
    riceve 400Ħ, 300Ħ vengono pagati all'intermediario 1 e 100Ħ vengono
    pagati all'intermediario 2. Se lo stesso importo è dovuto a entrambi gli
    intermediari, il rimborso è equamente diviso. Ad esempio, il giocatore 2
    deve 100Ħ all'intermediario 1 e 100Ħ all'intermediario 2; quando il
    giocatore 2 riceve 100Ħ, 50Ħ vanno a ciascun intermediario.

Ad esempio,
    ex1(0x5B23, 0xC78D, 0x44AE, 0x1612, 0x90FF, 1000,
        [ ((0x44AE, 0x5B23),  800, 0x1612,  4),
          ((0x44AE, 0xC78D),  800, 0x90FF, 10),
          ((0xC78D, 0x5B23),  400, 0x1612,  8),
          ((0x44AE, 0xC78D), 1800, 0x90FF, 12),
          ((0x5B23, 0x44AE),  100, 0x1612,  2)
        ]
    ritorna
    ( [2098, 568, 0], [66, 268], [ [0, 0, 0], [0, 0, -28] ] )
    perché tutti gli utenti iniziano con 1000Ħ nei loro conti ed, al termine,
    – il saldo dell’utente 1 ammonta a 2098Ħ,
    – il saldo dell’utente 2 ammonta a 568Ħ,
    – il saldo dell’utente 3 ammonta a 0Ħ,
    – l'intermediario 1 ha guadagnato 66Ħ,
    – l'intermediario 2 ha guadagnato 268Ħ,
    – l’utente 3 rimane in debito di 28Ħ con l'intermediario 2.

Il TIMEOUT per ciascun test è di 0.5 secondi

ATTENZIONE: è proibito:
    - importare altre librerie
    - usare variabili globali
    - aprire file
"""



# def checkPayDebt(money, receiver, inter, dictInterme):
#     #use this function for repaying debts after a transaction
#     for innerList in dictInterme:
#         for innerKey in innerList:
#             if innerKey == inter: #here we find the debt if exists
#                 if innerKey[receiver] < 0:
#                     return innerKey[receiver]
#     return 0


# def payDebts(user, dictUser, dictDebts, keyImd, dictImd): #last one that I miss!!!
#     #dictDebts is negative
#     currentMoney = dictUser[user] #used to pay the int
#     currentDebt = abs(dictDebts[user])
#     if currentMoney >= currentDebt:
#         transaction = currentMoney - currentDebt
#         dictUser[user] = transaction
#         dictImd[keyImd] += currentDebt
#         dictDebts[user] = 0
#     else:
#         transaction = currentDebt - currentMoney
#         dictDebts[user] = - transaction
#         dictImd[keyImd] += currentMoney
#         dictUser[user] = 0
    
           
def payBetweenUsers(money:int, sender:int, dictionaryUsers:dict) -> int:
    #used to check if a transaction in doable
    res :int = 0
    if dictionaryUsers[sender] >= money:
        res = money #this will be updatedto receiver account else 0
        dictionaryUsers[sender] -= money
    return res

# def payIntermediary(fee, sender, dictUsers, interm, dictIntermediary, dictDebtors):
#     if dictUsers[sender] >= fee:
#         dictIntermediary[interm] += fee
#         dictUsers[sender] -= fee
#     else:
#         difference = fee - dictUsers[sender] #money can'r be paid
#         dictIntermediary[interm] += dictUsers[sender] #user pay what can be paid
#         dictUsers[sender] = 0 #set user account to 0
#         for i in dictDebtors:
#             for j in i:
#                 if j == interm:
#                     i[j][sender] -= difference

def payIntermediaryTransaction(fee:int, payer:int, usersDict:dict, interm:int, dictIntermAccount:dict, dictDebtors:dict) -> None:
    
    if usersDict[payer] >= fee:
        usersDict[payer] -= fee
        dictIntermAccount[interm] += fee
    else:
        missing_money = fee - usersDict[payer]
        dictIntermAccount[interm] += usersDict[payer]
        usersDict[payer] = 0
        dictDebtors[payer] -= missing_money
    
    return
    pass

def payIntermediaryDebts(receiver:int, dictUsers:dict, debts_firts:dict, debts_second:dict):
    
    while dictUsers[receiver] > 0 and (debts_firts[receiver] < 0 and debts_second[receiver] < 0):
        if debts_firts[receiver] < debts_second[receiver]:
            payment = min(dictUsers[receiver], abs(debts_firts[receiver]))
            dictUsers[receiver] -= payment
            debts_firts[receiver] += payment
            if dictUsers[receiver] > 0:
                payment_2 = min(dictUsers[receiver], abs(debts_second[receiver])) 
                dictUsers[receiver] -= payment_2
                debts_second[receiver] += payment_2
        else:
            payment = min(dictUsers[receiver], abs(debts_second[receiver])) 
            dictUsers[receiver] -= payment
            debts_second[receiver] += payment
            if dictUsers[receiver] > 0:
                payment_2 = min(dictUsers[receiver], abs(debts_firts[receiver])) 
                dictUsers[receiver] -= payment_2
                debts_firts[receiver] += payment_2
                
    return

def ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log):
    #INITIALIZE ALL VAR WITH INPUT PARAMS EXEPT TRANSACT_LOG
    
    #initialize the dictionary for users and intermediays 
    dictUsers:dict = {acn1: init_amount, acn2: init_amount, acn3: init_amount}
    dictIntermediary:dict = {imd_acn1: 0, imd_acn2: 0}
    
    #dictionary used to track debts
    dictDebts:dict = [{imd_acn1: {acn1: 0, acn2: 0, acn3: 0}}, {imd_acn2: {acn1: 0, acn2: 0, acn3: 0}}] 
    #created whit pointer so referring to the same objects
    debtInt1:dict = dictDebts[0][imd_acn1]
    debtInt2:dict = dictDebts[1][imd_acn2]
    
    #TO USE AND INPLEMENT FUNC FOR LOG OPERATION
    #initialize helpful variable??
    for transact in transact_log:
        #initialize util variables
        sender:int = transact[0][0]
        receiver:int = transact[0][1]
        moneySent:int = transact[1]
        intermediaryTemp:int = transact[2] 
        intermediaryFee:int = moneySent * transact[3] / 100
        debt_register_temp = dict()
        
        if intermediaryTemp in debtInt1:
            debt_register_temp = debtInt1
        else:
            debt_register_temp = debtInt2
        
        #first check if transaction in doable for now i assume if check == money precedence to receiver
        dictUsers[receiver] += payBetweenUsers(moneySent, sender, dictUsers) 
        #now pay the int
            #if not enought pay intermediary what users can and than add to debt
        #payIntermediary(intermediaryFee, sender, dictUsers, intermediaryTemp, dictIntermediary, dictDebts)
        payIntermediaryTransaction(intermediaryFee, sender, dictUsers, intermediaryTemp, dictIntermediary, debt_register_temp)
        #with money received the receiver pay debts if there are
        # if debtInt1[receiver] <= debtInt2[receiver]:
        #     payDebts(receiver, dictUsers, debtInt1, imd_acn1, dictIntermediary)
        #     payDebts(receiver, dictUsers, debtInt2, imd_acn2, dictIntermediary)
        # else:
        #     payDebts(receiver, dictUsers, debtInt2, imd_acn2, dictIntermediary)
        #     payDebts(receiver, dictUsers, debtInt1, imd_acn1, dictIntermediary)
        #     pass #to end thi implementatsion
        # STILL NOW WORKING 100 DIFFERENCE DEBTS NOT PAID, TEST
        
        payIntermediaryDebts(receiver, dictUsers, debtInt1, debtInt2)
        
        #try with a for using the max debt and usig he payInterm function and than pay the second int, just 2
        # while dictUsers[receiver] > 0 or dictDebts[imd_acn1][receiver] == 0 and dictDebts[imd_acn2][receiver] == 0:
        #     paydebts(receiver, dictUsers, dictDebts,)
        pass #implement a function that take a tuple in input ad operate on the dictionary
    
    
    #OUTPUTS
    listUserAccount = list(dictUsers.values()) #this is the first list, user accounts
    listIntermediaryMoney = list(dictIntermediary.values()) #this is list intermediary accounts
    #halfway done, all dictionary storage, to extract list of values
    listDebts = [list(dictDebts[0].values()), list(dictDebts[1].values())]
    listRes = [] #finale list to return, list of lists
    for innerList in listDebts: 
        for innerDict in innerList:
            listRes.append(list(innerDict.values()))
    
    return listUserAccount, listIntermediaryMoney, listRes
    pass


if __name__ == '__main__':
    provaTest = ex1(0x5B23, 0xC78D, 0x44AE, 0x1612, 0x90FF, 1000,
        [ ((0x44AE, 0x5B23),  800, 0x1612,  4),
          ((0x44AE, 0xC78D),  800, 0x90FF, 10),
          ((0xC78D, 0x5B23),  400, 0x1612,  8),
          ((0x44AE, 0xC78D), 1800, 0x90FF, 12),
          ((0x5B23, 0x44AE),  100, 0x1612,  2)
        ])
    
    assert (provaTest == ( [2098, 568, 0], [66, 268], [ [0, 0, 0], [0, 0, -28] ] ))
    print("test passed")
    

