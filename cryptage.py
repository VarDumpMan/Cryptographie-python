# coding:utf8

from modules.func import crypt_text  

texte = input("Entrer un texte : ").upper()
cle = input("Entrer la clé : ").upper()

print("La forme cryptée donne : " + crypt_text(texte, cle)) 
