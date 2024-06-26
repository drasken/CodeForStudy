# -*- coding: utf-8 -*-
'''
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
'''

def paymoney(dict_users_balance, sender, receiver, money_to_pay):
    #function to send money between users
    pass
    dict_users_balance[sender] -= money_to_pay
    dict_users_balance[receiver] += money_to_pay

def pay_receiver_debt(dict_users_balance, receiver, debtInt1, debtInt2):
    #use this function to pay debt after receiving money
    pass
    #check if can pay all debt and who to pay first
    
    if debtInt1[receiver] < debtInt2[receiver]:
        if dict_users_balance[receiver] >= abs(debtInt1[receiver]): #can pay it all
            dict_users_balance[receiver] += debtInt1[receiver]
            debtInt1[receiver] = 0
        else: #don't have all the money
            debtInt1[receiver] += dict_users_balance[receiver]
            dict_users_balance[receiver] = 0
         #check if I can pay second debt if there is one   
        if dict_users_balance > 0 and dict_users_balance[receiver] >= abs(debtInt2[receiver]):
            dict_users_balance[receiver] += debtInt2[receiver]
            debtInt2[receiver] = 0
        elif dict_users_balance[receiver] > 0 and dict_users_balance[receiver] < abs(debtInt2[receiver]):
            debtInt2[receiver] += dict_users_balance[receiver]
            dict_users_balance[receiver] = 0
    else: #case second debt bigger than fist
        if dict_users_balance[receiver] >= abs(debtInt2[receiver]):
            dict_users_balance[receiver] += debtInt2[receiver]
            debtInt2[receiver] = 0
        else:
            debtInt2[receiver] += dict_users_balance[receiver]
            dict_users_balance[receiver] = 0
        if dict_users_balance[receiver] > 0 and dict_users_balance[receiver] >= abs(debtInt1[receiver]):
            dict_users_balance[receiver] += debtInt1[receiver]
            debtInt1[receiver] = 0
        elif dict_users_balance[receiver] > 0 and dict_users_balance[receiver] < abs(debtInt1[receiver]):
            debtInt1[receiver] += dict_users_balance[receiver]
            dict_users_balance[receiver] = 0


def pay_intermediary_fee():
    #use this function to pay fee cost to intermediary as sender of transaction
    pass

def process_transaction(transaction:tuple, dictUsers:dict, dictIntermediary:dict, debtInt1:dict, debtInt2:dict):
    
    pass
    sender, receiver = transaction[0][0], transaction[0][1]
    money_sent = transaction[1]
    intermediary = transaction[2]
    fee_cost = (money_sent * 100) / transaction[3]
    
    if dictUsers[sender] >= fee_cost:
        paymoney(dictUsers, sender, receiver, fee_cost)
        pay_receiver_debt() # TO IMPLEMENT
    
    pay_intermediary_fee() #TO IMPLEMENT
    
    

def ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log):
    
    pass
    #initialize the dictionaries 
    dictUsers = {acn1: init_amount, acn2: init_amount, acn3: init_amount}
    dictIntermediary = {imd_acn1: 0, imd_acn2: 0}
    
    dictDebts = [{imd_acn1: {acn1: 0, acn2: 0, acn3: 0}}, {imd_acn2: {acn1: 0, acn2: 0, acn3: 0}}] 

    debtInt1 = dictDebts[0][imd_acn1]
    debtInt2 = dictDebts[1][imd_acn2]
    
    for trans in transact_log:
        pass
    
    return dictUsers, dictIntermediary, dictDebts


if __name__ == '__main__':
    
    test =     ex1(0x5B23, 0xC78D, 0x44AE, 0x1612, 0x90FF, 1000,
            [ ((0x44AE, 0x5B23),  800, 0x1612,  4),
              ((0x44AE, 0xC78D),  800, 0x90FF, 10),
              ((0xC78D, 0x5B23),  400, 0x1612,  8),
              ((0x44AE, 0xC78D), 1800, 0x90FF, 12),
              ((0x5B23, 0x44AE),  100, 0x1612,  2)
            ])
    
