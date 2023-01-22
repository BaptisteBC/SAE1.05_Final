# Recherche Dichotomique itérative

def dichotomique_iteratif(val, tableau_trie):
    global milieu
    debut = 0
    fin = len(tableau_trie) - 1
    trouve = False

    while not trouve and debut <= fin:
        milieu = (debut + fin) // 2
        if tableau_trie[milieu] == val:
            trouve = True
        elif val > tableau_trie[milieu]:
            debut = milieu + 1
        else:
            fin = milieu - 1
    if trouve:
        return milieu
    else:
        return -1


# dichotomique_iteratif(val, tableau_trie)

# Dichotomique récursive

def dichotomique_recursive(val, tableau_trie):
    milieu = len(tableau_trie) // 2
    if len(tableau_trie) == 1:
        return -1
    if tableau_trie[milieu] == val:
        return milieu
    if tableau_trie[milieu] > val:
        return dichotomique_recursive(val, tableau_trie[:milieu])
    else:
        return milieu + dichotomique_recursive(val, tableau_trie[milieu:])

# dichotomique_recursive(val, tableau_trie)