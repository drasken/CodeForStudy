"""
Simple utility script to decide if bnb is a viable alternative or not

NOTE: Only money is considered, the individual work to manage a BnB
is too subjective to include it in some calculation and the same is true
about the effort and if it's worth certain earnings or not.
"""

"""
Global var constants and import statement
"""

import numpy as np
import matplotlib as 

# Home value at the starting point. Change accordingly
INIT_HOME_VALUE = 100_000
# Estimated a 3% yearly on average, found on-line, change on what you think is more appropriate
ANNUAL_HOME_DEPRECIATION = 0.03


"""
 Here is the section about using the apartment for BnB
"""

annual_expected_income = pass
annual_taxes = pass
intermediary_fees = pass
annual_expected_expense = pass
risk_free_rate = 1.73 # Change accordingly, this is the rate for 12 months government bond today


"""
Here is the section about using the money after selling the apartment
"""

# ------------------------------
# Delete after line, this line included!


"calcolo ipotizzando di affittare con affitti brevi(Booking, Airbnb, etc.)"

affitto_giornaliero = 120 #euro al giorno pagati dagli ospiti

FEE_PIATTAFORMA = 15 #percentuale da pagare

TASSA = 20
#percentuale con cedolare secca, avevo contato 21 perchè per piattaforme online google mi dava 21 o 25 per cento

guadagno_netto_giornaliero = (affitto_giornaliero - (affitto_giornaliero / 100 * FEE_PIATTAFORMA)) - ((affitto_giornaliero - (affitto_giornaliero / 100 * FEE_PIATTAFORMA)) / 100 * TASSA)
#guadagno calcolato da affitto meno fee piattaforma, al quale si toglie le tasse

costo_IMU = 730

print(f"Il guadagno giornaliero sarebbe di {guadagno_netto_giornaliero}€")

giorni_affittati = 120 #quanti giorni si prevede di affittare in un anno

guadagno_netto_annuale = (guadagno_netto_giornaliero * giorni_affittati) - costo_IMU

print(f"Il guadagno annuale sarebbe di {guadagno_netto_annuale}€")




netto_vendita = 140000

interesse_CD = 0.03 #percentuale di resa, qui ho considerato un conto deposito al 3% netto

anni_da_calcolare = 20

rendimento_vendita = round(netto_vendita * ((1 + interesse_CD) ** anni_da_calcolare), 2)

Andrea = False #se Andrea, aggiungi anche tasse risparmiate

if Andrea:
  rendimento_vendita += 6500

print(f"Mettendo a rendita il ricavato in {anni_da_calcolare} anni si otterrebbero {rendimento_vendita}€")




guadagno_temporaneo = guadagno_netto_annuale
anni = 0

while guadagno_temporaneo <= netto_vendita:
  #print(f"Per ora il guadagno all'anno {anni} è {guadagno_temporaneo}€ ")
  guadagno_temporaneo += guadagno_netto_annuale
  guadagno_temporaneo = round(guadagno_temporaneo, 2)
  anni += 1

print(f"Per pareggiare i {netto_vendita}€ della vendita ci sono voluti {anni} anni")
print(f"In {anni} anni si arriverebbe a {guadagno_temporaneo}€")


import matplotlib.pyplot as plt






import matplotlib.pyplot as plt

def int_comp (input, anno, interesse): # per calcolare interesse composto
  return input * ((1 + interesse) ** anno)

def compound_with_deposit(init_sum: float, interest: float, years: int, deposit: float) -> float:

    if years <= 1:
        return round((init_sum + deposit) * (1 + interest), 2)
    else:
        new_sum = round((init_sum + deposit) * (1 + interest), 2)
        return compound_with_deposit(new_sum, interest, years - 1, deposit)


interesse_CD = 0.03 #percentuale di resa, qui ho considerato un conto deposito al 3% netto
anni_da_calcolare = 30
prezzo_vendita = 140000
depretiation_rate = 0.0363 #stima trovata online du media di deprezzamento annuale diun immobile
inflation = 0.02 # considerato un 2& standard

anni_list = [x for x in range(anni_da_calcolare)]
guadagno_affitto = [(x * guadagno_netto_annuale) for x in range(1,(anni_da_calcolare + 1))]
guadagno_vendita = [round(int_comp(prezzo_vendita, x , interesse_CD), 2) for x in range(anni_da_calcolare)]

#modifiche del 2025-02-07
# raffiniamo ulteriormente il calcolo dei dati
"""
Promemoria //TODO
Modifica 1:
per l'affitto consideriamo anche reinvestimenti dei guadagni in equivalente del CD
consideriamo anche vendita della casa però con ammortamento del valore di vendita dovuto ad usura
andrebbe anche considerato un tasso di apprezzamento dell'affitto, aumento almeno pare ad inflazione
Storicamente 2%(?)

Modifica 2:
Allo stesso modo anche l'interesse composto sul CD in caso di vendita andrebbe considerato con aumento.
Guardare media storica di aumento tassi di interesse, %?
"""
#calcolo guadagno affitto inflation adjusted più ROI degli affitti reinvestiti
guadagno_affitto_new = [round((int_comp(guadagno_netto_annuale, x, inflation) + compound_with_deposit(0, interesse_CD, x, guadagno_netto_annuale)) , 2)for x in range(1,(anni_da_calcolare + 1))]
#add adjusted home value all'ultimo anno ipotizzando una vendita
guadagno_affitto_new[-1] += round(prezzo_vendita * ((1 - depretiation_rate) ** anni_da_calcolare), 2)

# Plotting the data
plt.plot(anni_list, guadagno_affitto, label='Guadagno Affitto Semplice')
plt.plot([0, anni], [netto_vendita, netto_vendita], 'r--', label='Netto Vendita')
plt.plot(anni_list, guadagno_vendita, label='Guadagno Vendita')
plt.plot(anni_list, guadagno_affitto_new, label="Guadagno Affitto Reinvestiti")
plt.xlabel('Anni')
plt.ylabel('Guadagno')
plt.title('Andamento del guadagno nel tempo')
plt.legend()
plt.grid(True)
plt.show()

