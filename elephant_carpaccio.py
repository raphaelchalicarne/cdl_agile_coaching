# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
taxes ={"UT":1.0685,"NV":1.08,"TX":1.0625,"AL":1.04,"CA":1.0825}

def whatIsThePrice():
    price = input('Quel est le prix de l\'objet ?\n')
    try:
        price = float(price)
    except:
        print("Mauvaise entrée")
        return
    print('L\'objet coûte ' + str(price) + ' $')
    
def howManyItems():
    nbItems = input('Combien d\'objets?\n')
    priceItem = input('Combien coûte un objet?\n')
    try:
        nbItems = int(nbItems)
        priceItem = float(priceItem)
    except:
        print("Mauvaise entrée")
        return
    somme = nbItems * priceItem
    print('\nPrix total avant taxes : ' + str(somme) + ' $')
    return somme
    

def addTaxes():
    somme = howManyItems()
    state = input("Dans quel état vendez-vous le produit?\n")
    #state = 'TX'
    tax = 1
    if state in taxes:
        tax = taxes[state]
    #if state == 'TX':
    #    tax = 1.0625
    sommeTax = round(somme*tax,2)
    print('\nTaux de taxe dans l\'état de ' + state + ' : ' + str((tax - 1)*100) + '%')
    print('\nPrix après taxes dans l\'état du ' + state + ' : ' + str(sommeTax) + ' $')
    return sommeTax

def whatAreTaxRates():
    print('\nTax rates :\nUT : 6.85%\nNV : 8.00%\nTX : 6.25%\nAL : 4.00%\nCA : 8.25%')
    
    
def addDiscount():
    somme = howManyItems()
    isThereADiscount = False
    discount = 0
    if somme > 1000:
        discount = 0.03
        isThereADiscount = True
    somme = (1-discount)*somme
    somme = round(somme,2)
    if isThereADiscount:
        print('\nIl y a eu une réduction appliquée')
        print('\nPrix après réduction : '+ str(somme) + ' $')
    else:
        print('\nIl n\'y a pas eu de réduction appliquée')
        print('\nPrix : '+ str(somme) + ' $')
    return somme
    
#whatIsThePrice()
#howManyItems()
addTaxes()

#whatAreTaxRates()
addDiscount()

