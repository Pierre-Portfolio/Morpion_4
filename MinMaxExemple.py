# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:59:18 2021

@author: tompa
"""

#construit un jeu vide
def nouveauJeu():
    return ('.','.','.','.','.','.','.','.','.')

#permet d'afficher un jeu
def affiche(jeu):
    print(jeu[0],jeu[1],jeu[2])
    print(jeu[3],jeu[4],jeu[5])
    print(jeu[6],jeu[7],jeu[8])


#permet de savoir qui doit jouer
def joueur(jeu):
    J1=0
    J2=0
    for i in jeu:
        if i=='X':
           J1+=1
        if i=='O':
           J2+=1
    if J1==J2:
        return 'X'
    return('O')

#retourne les coups possibles
# a savoir les cases vides avec un '.' dedans
def coupPossible(jeu):
    res=[]
    for i in range(9):
        if jeu[i]=='.':
            res+=[i]
    return res


#permet de jouer un coup sur une case
def jouer(jeu,coup):
    if jeu[coup]!='.':
        print("case occupee")
    else:
        liste=[]
        liste+=jeu
        liste[coup]=joueur(jeu)
        return(tuple(liste))


#permet de savoir si le joueur 1 'X' gagne une partie
def gagner(jeu):
    res='.'
    if (jeu[0]!='.' and jeu[0]==jeu[3]==jeu[6]):
        res=jeu[0]
    if (jeu[1]!='.' and jeu[1]==jeu[4]==jeu[7]):
        res=jeu[1]
    if (jeu[2]!='.' and jeu[2]==jeu[5]==jeu[8]):
        res=jeu[2]
    if (jeu[0]!='.' and jeu[0]==jeu[1]==jeu[2]):
        res=jeu[0]
    if (jeu[4]!='.' and jeu[4]==jeu[5]==jeu[3]):
        res=jeu[3]
    if (jeu[7]!='.' and jeu[7]==jeu[8]==jeu[6]):
        res=jeu[6]
    if (jeu[0]!='.' and jeu[0]==jeu[4]==jeu[8]):
        res=jeu[0]
    if (jeu[2]!='.' and jeu[2]==jeu[4]==jeu[6]):
        res=jeu[2]
    if (res=='O'):
        return(-1)
    else:
        if res=='X':
            return(1)
    return(0)

#test gagner
print("************************")
print("Test fonction gagner")
print("************************")
jeu=nouveauJeu()
print('jeu vide',gagner(jeu));
jeu=jouer(jeu,0)
affiche(jeu)
print('jeu faux',gagner(jeu));
jeu=jouer(jeu,1)
affiche(jeu)
print('jeu faux',gagner(jeu));
jeu=jouer(jeu,3)
affiche(jeu)
print('jeu faux',gagner(jeu));
jeu=jouer(jeu,4)
affiche(jeu)
print('jeu faux',gagner(jeu));
jeu=jouer(jeu,6)
affiche(jeu)
print('jeu vrai',gagner(jeu));
print("************************")



#**************************************************************
# Approche Minmax
#**************************************************************



# fonction recursive appelÃ©e par le joueur X
# X maximise la valeur de son coup sur valmin (coup de l'adversaire)
def valMax(jeu,dic):
    coups=coupPossible(jeu)
     
    # si c'est un Ã©tat terminal
	# on retourne la valeur
	
	# l'Ã©tat est terminal si un joueur a gagnÃ© ou s'il n'y a plus de coups Ã  jouer
    if gagner(jeu)!=0 or len(coups)==0:
        dic[jeu]=gagner(jeu)
        return ([gagner(jeu),['f']])

    # sinon, c'est qu'il y a des coups Ã  jouer
	# on fait un max sur les situations resultantes
	# car X cherche Ã  maximiser son gain
    max=[-2,['.']]
    valeurMax='.'

    # pour chaque coup
    for coup in coups:
		#calcule le nouveau jeu
        njeu=jouer(jeu,coup)
        # appel recursif
        val=valMin(njeu,dic)
        # si le coup est meilleur, je le stocke
        if val[0]>max[0] :
            max=val
            print(f'Valeur de max :{max}')
            valeurMax=coup

	#on stocke la valeur dans le dictionnaire
    dic[jeu]=max[0]
	
    # on retourne la valeur et le coup correspondant
    max[1].append(valeurMax)
    return [max[0],max[1]]
    

# fonction recursive appelÃ©e par le joueur O
# O minimise la valeur de son coup sur valmax (coup de l'adversaire)
# puisque la valeur est maximale quand X est gagnant
def valMin(jeu,dic):
    coups=coupPossible(jeu)
     
    # si c'est un Ã©tat terminal
    if gagner(jeu)!=0 or len(coups)==0:
        dic[jeu]=gagner(jeu)
        return ([gagner(jeu),['f']])

    #on fait un minimum sur la valeur 
	#car O cherche Ã  minimiser le gain de X
    min=[2,['.']]
    valeurMin='.'

    # pour chaque coup
    for coup in coups:
        njeu=jouer(jeu,coup)
        # appel recursif
        val=valMax(njeu,dic)
        # si le coup est meilleur
        if val[0]<min[0] :
            min=val
            valeurMin=coup

    dic[jeu]=min[0]
	
    # on retourne le val et le coup
    min[1].append(valeurMin)
    return [min[0],min[1]]


# permet de lancer minmax
# appelle soit valmin soit valmax en fonction du joueur dont c'est le tour
def MinMax(jeu,dic):
    coups=coupPossible(jeu)

    # si c'est un Ã©tat terminal
    if gagner(jeu)!=0 or len(coups)==0:
        dic[jeu]=gagner(jeu)
        return ([gagner(jeu),['f']])

    #cherche le joueur
    if joueur(jeu)=='X':
		#le joueur 1 maximise
        return valMax(jeu,dic)
    else:
		#le joueur 2 minimise
        return valMin(jeu,dic)
    
    

#**************************************************************
# Approche Minmax avec facteur gamma
#**************************************************************

	
# comme valMAx sauf qu'on ajoute un facteur de decompte
# cela se traduit par le facteur 0.9 du return et l'appel Ã  valMinGamma
def valMaxGamma(jeu,dic):
    coups=coupPossible(jeu)
     
    # si c'est un Ã©tat terminal
    if gagner(jeu)!=0 or len(coups)==0:
        dic[jeu]=gagner(jeu)
        return ([gagner(jeu),['f']])

    #on fait un max sur valeur*mult
    max=[-2,['.']]
    valeurMax='.'

    # pour chaque coup
    for coup in coups:
        njeu=jouer(jeu,coup)
        # appel recursif
        val=valMinGamma(njeu,dic)
        # si le coup est meilleur
        if val[0]>max[0] :
            max=val
            valeurMax=coup

    dic[jeu]=max[0]
    # on retourne le val et le coup
    max[1].append(valeurMax)
    return [max[0]*0.9,max[1]]
    

#comme valMin sauf qu'on ajoute un facteur de decompte
# cela se traduit par le facteur 0.9 du return et l'appel Ã  valMaxGamma
def valMinGamma(jeu,dic):
    coups=coupPossible(jeu)
     
    # si c'est un Ã©tat terminal
    if gagner(jeu)!=0 or len(coups)==0:
        dic[jeu]=gagner(jeu)
        return ([gagner(jeu),['f']])

    #on fait un max sur valeur*mult
    min=[2,['.']]
    valeurMin='.'

    # pour chaque coup
    for coup in coups:
        njeu=jouer(jeu,coup)
        # appel recursif
        val=valMaxGamma(njeu,dic)
        # si le coup est meilleur
        if val[0]<min[0] :
            min=val
            valeurMin=coup

    dic[jeu]=min[0]
    # on retourne le val et le coup
    min[1].append(valeurMin)
    return [min[0]*0.9,min[1]]


#comme MinMax sauf qu'on ajoute un facteur de decompte
# cela se traduit par appel de valMaxGamma et valMinGamma
def MinMaxGamma(jeu,dic):
    coups=coupPossible(jeu)

    # si c'est un Ã©tat terminal
    if gagner(jeu)!=0 or len(coups)==0:
        dic[jeu]=gagner(jeu)
        return ([gagner(jeu),['f']])

    #cherche le joueur
    if joueur(jeu)=='X':
        return valMaxGamma(jeu,dic)
    else:
        return valMinGamma(jeu,dic)
	

#**************************************************************
# Fonctions pour lancer le jeu
#**************************************************************


#permet de prÃ©senter la matrice des coups
def afficheMatrice():
    print ("touches")
    print ("------")
    print ("0 1 2")
    print ("3 4 5")
    print ("6 7 8")
    print ("------")
    
    

#permet de jouerPartie
# depart : situation de depart
# table : le dictionnaire avec les valeurs
# humain : quel joueur est jouÃ© par l'humain (X ou O)
def jouerPartie(depart,table,humain):
    jeu=depart
    print("******* bonne partie *****")
    affiche(jeu)
    #tant que le jeu n'est pas fini
    while (gagner(jeu)==0) and len(coupPossible(jeu))!=0:
        #si c'est au joueur
        if joueur(jeu)==humain :
            print("----- a vous -----") 
            coup=-1
            #demander coup valide
            coups=coupPossible(jeu)
            afficheMatrice()
            #demander tant que le coup n'est pas valide
            while(coup not in coups):
                coup=int(input("quel coup jouer ? "))
            #jouer coup
            jeu=jouer(jeu,coup)
            affiche(jeu)
            
        # si c'est au programme
        else:
            print("----- a moi -----")
            #deux cas se posent
            # si la situation n'est pas connue, on la calcule
            #cela arrive si on sort du chemin optimal
            if (jeu not in table):
                table=calcul(jeu)
            #joue le meilleur coup
            coup=coupMeilleur(jeu,table)
            jeu=jouer(jeu,coup)
            affiche(jeu)

import random

# recherche du meilleur coup  Ã  jouer
# a partir de la situation jeu et du dictionnaire table
# on peut faire mieux plutot que recommencer
def coupMeilleur(jeu,table):
    #cherche le coup Ã©gal Ã  la valeur
    coups=coupPossible(jeu)
    valeur=table[jeu]

    #pour faire au hasard
    #on choisit le coup au hasard parmi les meilleurs
    fini=False
    while (not fini):
        #choisit un coup au hasard
        coup=coups[random.randint(0,len(coups)-1)]
        #si la valeur est celle attendue, on return
        njeu=jouer(jeu,coup)
        #si la cle existe
        if (njeu in table):
            if (table[njeu]==valeur):
                return coup
                    

#**************************************************************
# Utilisation de minmax gammma pour lancer une partie
#**************************************************************


#creation du dictionnaire Ã  partir d'un jeu initial
dico={}
jeu=nouveauJeu()
#affiche la suite de coups optimaux et calcule dico
print("**********************************")
print("*Calcul Minmax en cours")
print("**********************************")

res=(MinMaxGamma(jeu,dico))
print("*Meilleure trajectoire")
print(res)


print("\n\n\n")

#lancement d'une partie contre l'IA
# en utilisant le dictionnaire construit
print("**********************************")
print("*Lancement de la partie")
print("**********************************")
jouerPartie(jeu,dico,'X')





