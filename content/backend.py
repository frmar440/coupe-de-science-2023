from IPython.display import clear_output
import pandas as pd
import numpy as np

# decoupage challenge
chaine = "2be6d5c4-23b3"
code = chaine[:5] + chaine[-2:]

INDICE_DECOUPAGE = "NOURRITURE DANS GROTTE SOUS CHUTE"

def decode_decoupage():
    clear_output(wait=True)
    code_input = input("Entrez le code du bunker: ")
    if code_input == code:
        print("Code valide! Vous entrez dans le bunker et trouvez l'indice suivant:")
        print(INDICE_DECOUPAGE)
    else:
        print("Code invalide! Veuillez exécuter la cellule (ctrl-enter) pour tenter à nouveau.")

# onde radio challenge
INDICE_RADIO = "BAIES ROUGES DE L'ILE SONT COMESTIBLES"

def decode_onde():
    clear_output(wait=True)
    freq_input = input("Entrez la fréquence de l'onde: ")
    if freq_input == "5":
        print("Fréquence valide! Vous décodez l'onde radio et trouvez l'indice suivant:")
        print(INDICE_RADIO)
    else:
        print("Fréquence invalide! Veuillez exécuter la cellule (ctrl-enter) pour tenter à nouveau.")

# iteration challenge

def gen_objet():
    for i in "INSECTES NUTRITIFS SE CACHENT SOUS LES ROCHES":
        yield i

# tableau challenge
df = pd.DataFrame(np.array([[i for i in "57u2A6mXeK"],
                            [i for i in "MCKDFn76NZ"],
                            [i for i in "3aY9bN4h4P"],
                            [i for i in "2JKD3mQ872"],
                            [i for i in "u5p7VGGpY2"],
                            [i for i in "MgvW7w6Sq8"]]))

INDICE_STELE = "SILEX ENTERRÉ À 1m SOUS LA STÈLE"

def decode_stele():
    clear_output(wait=True)
    code_input = input("Entrez le code secret de la stèle: ")
    if code_input == "aY9bN":
        print("Code valide! Une pierre de la stèle se déplace et vous trouvez l'indice suivant:")
        print(INDICE_STELE)
    else:
        print("Code invalide! Veuillez exécuter la cellule (ctrl-enter) pour tenter à nouveau.")

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

INDICE_PASCAL = "BANANIERS SE CACHENT AU SUD DE L'ILE"

def decode_pascal():
    clear_output(wait=True)
    code_input = input("Entrez le code secret de la roche pyramidale: ")
    if code_input == "120":
        print("Code valide! La roche pyramidale se fragmente et vous trouvez l'indice suivant:")
        print(INDICE_PASCAL)
    else:
        print("Code invalide! Veuillez exécuter la cellule (ctrl-enter) pour tenter à nouveau.")

if __name__ == '__main__':
    pass