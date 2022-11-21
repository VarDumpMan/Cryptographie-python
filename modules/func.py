# coding:utf8
    
# Fonction permet d'ajouter dans un tableau des lettres suivant des valeurs du code ascii envoyés.

def push(liste={}, debut=65, fin=90):
    i = len(liste)
        
    while debut <= fin:
        liste[i] = chr(debut)
        debut+= 1
        i+=1
        
        pass
    
    return liste

# Fonction qui génère des lettres de l'alphabet suivant une plage de valeur ASCII

def alphabet(debut=65, fin=90):
    lettres = {}
    if (debut==65 and fin==90):
        push(lettres, debut, fin)
    elif (debut > 65):
        lettres = push(lettres, debut, fin)
        push(lettres, 65, debut-1)
    return lettres

# Fonction permettant de crypter un mot suivant une clé 

def crypt_text(texte, cle) : 
    l = 0
    texte_crypte = ""

    while(l < len(texte)) :
        sous_texte = texte[l:l+len(cle)]
        i = 0
        
        for lettre in sous_texte:

            texte_crypte = texte_crypte + alphabet(ord(cle[i]), 90)[ord(lettre) - 65]        
            i+=1

        l+= len(cle)
        

    return texte_crypte.lower()

# Fonction permettant de crypter une phrase suivant une clé

def crypt_sentence(sentence, key):
    
    
    
    pass





