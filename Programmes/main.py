import numpy
import tri
import pickle
import matplotlib.pyplot as plt


def histogramme(data):
    histo = {}
    for sublist in data:
        for val in sublist:
            if val in histo:
                histo[val] += 1
            else:
                histo[val] = 1

    plt.bar(histo.keys(), histo.values())
    plt.xlabel("Numéro")
    plt.ylabel("Occurences")
    plt.title("Histogramme Tirage Loto")
    plt.show()


def seed():
    ask = input("Voulez-vous entrer une graine ? (oui/non) : ")
    if ask == "oui":
        graine = int(input("Veuillez entrer une graine (valeur entière positive) : "))
    else:
        graine = numpy.random.randint(1000)
    return graine


numpy.random.seed(seed())


def tri_choice():
    ask = input("Voudrez-vous effectuer un tri des tirages ? (oui/non) : ")
    if ask == "oui":
        ask = input("Quel tri préférez-vous utiliser ? (cocktail, insertion, fusion) : ")
        if ask == "cocktail":
            return 1
        if ask == "insertion":
            return 2
        if ask == "fusion":
            return 3
        else:
            return 1
    else:
        return 0


def tirage_loto(n, choix):
    tirage_mult = []
    if choix == 0:
        for i in range(n):
            tirage = numpy.random.choice(range(1, 46), 5, replace=False)
            tirage_mult.append(tirage.tolist())
        return tirage_mult
    if choix == 1:
        for i in range(n):
            tirage = numpy.random.choice(range(1, 46), 5, replace=False)
            tri.tri_cocktail(tirage)
            tirage_mult.append(tirage.tolist())
        return tirage_mult
    if choix == 2:
        for i in range(n):
            tirage = numpy.random.choice(range(1, 46), 5, replace=False)
            tri.tri_insertion(tirage)
            tirage_mult.append(tirage.tolist())
        return tirage_mult
    if choix == 3:
        for i in range(n):
            tirage = numpy.random.choice(range(1, 46), 5, replace=False)
            tri.tri_fusion(tirage)
            tirage_mult.append(tirage.tolist())
        return tirage_mult


n = int(input("Veuillez enter le nombre de tirage que vous souhaitez réaliser (valeur entière positive) : "))
choix = tri_choice()

with open("tirage_loto.bin", "wb") as fichier:
    pickle.dump(tirage_loto(n, choix), fichier, pickle.HIGHEST_PROTOCOL)

ask = input("Voulez-vous créer un histogramme de vos tirages ? (oui/non)")
if ask == "oui":
    histogramme(tirage_loto(n, choix))
else:
    print(tirage_loto(n, choix))
