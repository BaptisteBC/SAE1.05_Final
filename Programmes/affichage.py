import pickle
import matplotlib.pyplot as plt

with open("tirage_loto.bin", "rb") as fichier:
    donnees = pickle.load(fichier)

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
