def tri_cocktail(tableau):
    tableau_trie = True
    while tableau_trie:
        tableau_trie = False
        for i in range(0, len(tableau) - 2):
            if tableau[i] > tableau[i + 1]:
                (tableau[i], tableau[i + 1]) = (tableau[i + 1], tableau[i])
                tableau_trie = True
        for i in range(len(tableau) - 2, 0, -1):
            if tableau[i] > tableau[i + 1]:
                (tableau[i], tableau[i + 1]) = (tableau[i + 1], tableau[i])
                tableau_trie = True
    return tableau


def tri_insertion(tableau):
    for i in range(1, len(tableau)):
        j = i
        while j > 0 and tableau[j - 1] > tableau[j]:
            tableau[j], tableau[j - 1] = tableau[j - 1], tableau[j]
            j -= 1
    return tableau


def tri_fusion(tableau):
    if len(tableau) > 1:
        milieu = len(tableau) // 2
        tableau_gauche = tableau[:milieu]
        tableau_droit = tableau[milieu:]

        tri_fusion(tableau_gauche)
        tri_fusion(tableau_droit)

        g = d = t = 0

        while g < len(tableau_gauche) and d < len(tableau_droit):
            if tableau_gauche[g] < tableau_droit[d]:
                tableau[t] = tableau_gauche[g]
                g += 1
            else:
                tableau[t] = tableau_droit[d]
                d += 1
            t += 1

        while g < len(tableau_gauche):
            tableau[t] = tableau_gauche[g]
            g += 1
            t += 1

        while d < len(tableau_droit):
            tableau[t] = tableau_droit[d]
            d += 1
            t += 1
    return tableau