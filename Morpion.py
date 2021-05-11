# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:31:49 2021

@author: tompa
"""
import numpy as np
import time
import random

N = 12
Prof= 2
class Morpion():
    def __init__(self, numJoueur = 1,plateau=None, etat = None):
        if( plateau != None):
            self.plateau = plateau
        else:
            self.plateau = [['.' for i in range(N)] for j in range(N)]
        if(etat != None):
            self.etat = etat
        else:
            self.etat = 1
        self.numJoueur = numJoueur
    def Afficher(self):
        for i in range(N):
            s = ''
            for j in range(N):
                s += ' '+self.plateau[i][j]
            print(s)
    
    def finDePartie(self):
        for k in range(N):
            for l in range(N):
                if self.plateau[k][l]=='.':
                    return False
        return True
    
    def TestBottom(self,i,j,chara,nbrIt=0):
        if i>=N:
            return nbrIt
        if nbrIt==4:
            return nbrIt
        if self.plateau[i][j]==chara:
            return self.TestBottom(i+1,j,chara,nbrIt+1)
        return nbrIt
    
    def TestUpper(self,i,j,chara,nbrIt=0):
        if i<=0:
            return nbrIt
        if nbrIt==4:
            return nbrIt
        if self.plateau[i][j]==chara:
            return self.TestUpper(i-1,j,chara,nbrIt+1)
        return nbrIt
        
    def TestRight(self,i,j,chara,nbrIt=0):
        if j < N and nbrIt < 4 and self.plateau[i][j] == chara:
            return self.TestRight(i,j+1,chara,nbrIt+1)
        return nbrIt
    
    def TestLeft(self,i,j,chara,nbrIt=0):
        if j >= 0 and nbrIt < 4 and self.plateau[i][j]==chara:
            return self.TestLeft(i,j-1,chara,nbrIt+1)
        return nbrIt
    
    def TestBottomRight(self,i,j,chara,nbrIt=0):
        if (i>=N) or (j>=N):
            return nbrIt
        if nbrIt==4:
            return nbrIt
        if self.plateau[i][j]==chara:
            return self.TestBottomRight(i+1,j+1,chara,nbrIt+1)
        return nbrIt
    
    def TestBottomLeft(self,i,j,chara,nbrIt=0):
        if (i>=N) or (j<0):
            return nbrIt
        if nbrIt==4:
            return nbrIt
        if self.plateau[i][j]==chara:
            return self.TestBottomLeft(i+1,j-1,chara,nbrIt+1)
        return nbrIt
    
    def TestUpperRight(self,i,j,chara,nbrIt=0):
        if (i<0) or (j>=N):
            return nbrIt
        if nbrIt==4:
            return nbrIt
        if self.plateau[i][j]==chara:
            return self.TestUpperRight(i-1,j+1,chara,nbrIt+1)
        return nbrIt
    
    def TestUpperLeft(self,i,j,chara,nbrIt=0):
        if (i<0) or (j<0):
            return nbrIt
        if nbrIt==4:
            return nbrIt
        if self.plateau[i][j]==chara:
            return self.TestUpperLeft(i-1,j-1,chara,nbrIt+1)
        return nbrIt

    def win(self):                    
        res ='.'
        for i in range(N):
            if i%4 == 0:  
                for j in range(N):
                    if (self.plateau[i][j] != '.') and ( (self.TestBottom(i+1,j, self.plateau[i][j])+ self.TestUpper(i-1,j,self.plateau[i][j])== 3 ) or (self.TestLeft(i,j-1, self.plateau[i][j])+ self.TestRight(i,j+1,self.plateau[i][j]) == 3) or (self.TestBottomRight(i+1,j+1, self.plateau[i][j])+ self.TestUpperLeft(i-1,j-1,self.plateau[i][j]) == 3) or (self.TestUpperRight(i-1,j+1, self.plateau[i][j])+ self.TestBottomLeft(i+1,j-1,self.plateau[i][j]) == 3) ):                   
                        res = self.plateau[i][j]                       
            else:
                for j in range(0,N,4):
                    if (self.plateau[i][j] != '.') and ( (self.TestBottom(i+1,j, self.plateau[i][j])+ self.TestUpper(i-1,j,self.plateau[i][j])== 3 ) or (self.TestLeft(i,j-1, self.plateau[i][j])+ self.TestRight(i,j+1,self.plateau[i][j]) == 3) or (self.TestBottomRight(i+1,j+1, self.plateau[i][j])+ self.TestUpperLeft(i-1,j-1,self.plateau[i][j]) == 3) or (self.TestUpperRight(i-1,j+1, self.plateau[i][j])+ self.TestBottomLeft(i+1,j-1,self.plateau[i][j]) == 3) ):                   
                        res = self.plateau[i][j]                   
            if res != '.':
                break;  
        if ( res == 'O'):
            return ( 2)
        else :
            if res == 'X':
                return (1)
            elif (self.finDePartie()): #MatchNull
                return -1
            return (0)
        
    def Actions(self):
        coups = [];
        for i in range(N):
            for j in range(N):
                if(self.plateau[i][j] == '.'):
                   coups.append((i,j))
        return coups
    
    def Result(self,a):
        i = a[0]
        j = a[1]
        if(self.plateau[i][j] == '.'):
            if(self.etat  == 1):
                self.plateau[i][j] = 'X'
            else:
                self.plateau[i][j] = 'O'
            self.etat = (1 if self.etat == 2  else 2)
        return self
    
    def UnResult(self,a,etatBase):
        i = a[0]
        j = a[1]
        self.plateau[i][j] = '.'
        self.etat = etatBase
        return self
    
    def Terminal_Test(self):
        if(self.win() != 0) :
            return True
        return False
    
    def ComptPions(self,val):
        res = 0
        for i in range(N):
            for j in range(N):
                if((val ==  1 and self.plateau[i][j]=='X') or (val ==  2 and self.plateau[i][j]=='O')):
                    res += 1
        return res
    
    def Utility(self,a):
        if(self.Terminal_Test()):
            win = self.win()
            if(win == self.numJoueur):
                return 1000 - self.ComptPions(self.numJoueur)
            elif(win == -1):
                return 0
            else:
                return -1000 + self.ComptPions(1 if self.numJoueur == 2 else 2)
        else:
            #Faire isTrio : donne un score * (1/self.numJoueur) puis ifbloqueDuo or bloqueTrioSimple: donne un score (l'idée c'est gagne > bloqueTrioSimple (pas de possiblité de win des deux cotés) > trio > BloqueDuo (si numJoueur == 2) > duo > BloqueDuo (si numJoueur == 1))
            #Si isTrio + bloque score * 10
            return 0
    
#%% Algo Minmax
            
def MinMax_Decision(morpion):
    nplateau = [['.' for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            nplateau[i][j] = morpion.plateau[i][j]
    morp = Morpion(morpion.numJoueur,nplateau,morpion.etat)
    la= []
    etatBase = morp.etat
    for a in morp.Actions():
        la.append((a,Max_Value(morp.Result(a),a,Prof)))
        morp.UnResult(a, etatBase)
    la = sorted(la, key = lambda val:val[1], reverse = True)
    return la[0][0]

def Min_Value(morpion,a, profondeur = 0):
    if(morpion.Terminal_Test() or profondeur == 0):
        return morpion.Utility(a)
    score_min = 100000
    etatBase = morpion.etat
    profondeur -= 1
    for a in morpion.Actions():
        score_min = min(score_min,Max_Value(morpion.Result(a),a,profondeur))
        morpion.UnResult(a, etatBase)
    return score_min

def Max_Value(morpion, a, profondeur = 0):
    if(morpion.Terminal_Test() or profondeur == 0):
        return morpion.Utility(a)
    score_max = -100000
    etatBase = morpion.etat
    profondeur -= 1
    for a in morpion.Actions():
        score_max = max(score_max,Min_Value(morpion.Result(a),a,profondeur))
        morpion.UnResult(a, etatBase)
    return score_max


def RepresentsInt(s):
    try: 
        s = int(s)
        if(s<0 or s >= 12):
            return False
        return True
    except ValueError:
        return False

def Partie():
    nbCoups = 0
    numjoueur = input("Numero de joueurs ?\n") #correspond a notre ia
    m = Morpion(int(numjoueur))
    while(m.win() == 0):
        m.Afficher()
        if(m.etat == m.numJoueur):
            if(nbCoups == 0):
                print("On joue au centre (6,6)");
                m.Result((5,5))
            else:
                print("************************\n*    Au tour de l'ia   *\n************************")
                print("Début du MinMax")
                val = MinMax_Decision(m)
                print(f"Valeur a jouer : {val[0]+1}{val[1]+1}")
                m.Result(val)
                print(f"{m.win()}")
        else:
            i = input("Valeur du i adverse: \n")
            j = input("Valeur du j adverse: \n")
            while(not(RepresentsInt(i)) or not(RepresentsInt(j))):
                print("Erreur dans la saisie, veuillez recommencer\n")
                i = input("Valeur du i adverse: \n")
                j = input("Valeur du j adverse: \n")
            i = int(i)
            j = int(j)
            m = m.Result((i,j))
        nbCoups += 1
    valWin = m.win()
    winner = "Null" if valWin == 0 else "J1" if valWin == 1 else "J2"
    print(f"Fin de partie ! Gagnant : {winner}")
                
    

#%% Zone Main
if __name__ == "__main__":
    Partie()