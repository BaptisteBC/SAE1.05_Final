import pickle

with open("tirage_loto.bin", "rb") as fichier:
    donnees = pickle.load(fichier)

print(donnees)