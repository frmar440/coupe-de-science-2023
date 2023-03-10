


































































































# onde radio challenge

INDICE_RADIO = "SUIVEZ LE CHEMIN DE L'ANCIENNE ÉPAVE, OÙ REPOSENT LES OSSEMENTS DES MARINS"

def decode_onde(ans):
    if ans == "5":
        print("Fréquence valide! Vous décodez l'onde radio et trouvez l'indice suivant:")
        print(INDICE_RADIO)
    else:
        print("Fréquence invalide! Veuillez exécuter la cellule (ctrl-enter) pour tenter à nouveau.")

# decoupage challenge

chaine = "2be6d5c4-23b3"
code = chaine[:5] + chaine[-2:]

INDICE_DECOUPAGE = "NAGEZ DANS LE LABYRINTHE DE CORAIL, MAIS MÉFIEZ-VOUS DES CRÉATURES DANGEREUSES QUI S'Y CACHENT"

def decode_decoupage(ans):
    if ans == code:
        print("Code valide! Vous trouvez l'indice suivant:")
        print(INDICE_DECOUPAGE)
    else:
        print("Code invalide! Veuillez exécuter la cellule (ctrl-enter) pour tenter à nouveau.")

# tableau challenge

INDICE_STELE = 'TROUVEZ LA CARTE PERDUE DU ROI DES PIRATES, CACHÉE DANS UNE GROTTE AQUATIQUE'

def decode_stele(ans):
    if ans == "aY9bN":
        print("Code valide! Vous trouvez l'indice suivant:")
        print(INDICE_STELE)
    else:
        print("Code invalide! Veuillez exécuter la cellule (ctrl-enter) pour tenter à nouveau.")

# iteration challenge

def gen_objet():
    for i in 'UTILISEZ LA CARTE POUR LOCALISER LE NAVIRE COULÉ':
        yield i

# pascal challenge

def pascal_triangle(n):
    if n == 0: # cas de base
        return [[1]]
    else: # cas résursif
        triangle = pascal_triangle(n-1) # appel récursif
        ligne_courante = [1]
        ligne_precedente = triangle[-1]
        a = ligne_precedente[0]
        for b in ligne_precedente[1:]:
            ligne_courante.append(a+b)
            a = b
        ligne_courante += [1]
        triangle.append(ligne_courante)
        return triangle

INDICE_PASCAL = 'BRAVEZ LES ALGUES QUI SE TORDENT, ET VOUS TROUVEREZ LE COFFRE REMPLI DE RICHESSES'

def decode_pascal(ans):
    if ans == "120":
        print("Code valide! Vous trouvez l'indice suivant:")
        print(INDICE_PASCAL)
    else:
        print("Code invalide! Veuillez exécuter la cellule (ctrl-enter) pour tenter à nouveau.")
