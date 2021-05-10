# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:31:49 2021

@author: tompa
"""
import numpy as np
import time
import random

N = 12

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
    
    def Terminal_Test(self):
        if(self.win() != 0) :
            return True
        return False
    
    def Utility(self):
        if(self.Terminal_Test()):
            win = self.win()
            if(win == self.numJoueur):
                return 1000
            elif(win == -1):
                return -1
            else:
                return -1000
        else:  
            return 0
    
    '''
    
    def action(self): #Liste les coups possible (Donc à réduire au morpion dans le morpion)
        actionsPossibles=[]
        for k in range(N):
            for l in range(N):
                if self.plateau[k][l]==".":
                    actionsPossibles.append([k,l])
        return actionsPossibles
    
    def Result(self,i,j):
        if(self.plateau[i][j] == '.'):
            if(self.etat  == 1):
                self.plateau[i][j] = 'X'
            else:
                self.plateau[i][j] = 'O'
            self.etat = (1 if self.etat == -1  else -1)
        return self
            
    def Utility(self):
        list_eval = []
        for a in self.action():
            list_eval.append([a,self.Evaluate(a)]) #Add la coord et sa note
        list_eval = sorted(list_eval, key = lambda val:val[1])
        shuf = [i for i in list_eval if i[1] == list_eval[0][1]]
        return shuf[random.randint(0,len(shuf)-1)][0]

    def Evaluate(self,a): # Donne la note de la coord
        nplateau = [[self.plateau[i][j] for j in range(N)] for i in range(N)]
        morp2 = Morpion(nplateau,self.etat)
        morp2.plateau[a[0]][a[1]] = 'X' if self.etat == 1 else 'O'
        j2 = -1 if morp2.etat == 1 else 1
        if(morp2.win() == self.etat):
            return 0
        else:
            morp2.plateau[a[0]][a[1]] = 'X' if j2 == 1 else 'O'
            if(morp2.win() == j2):
                return 1
        return 2
    '''
    
#%% Algo Minmax
            
def MinMax_Decision(morpion):
    nplateau = [['.' for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            nplateau[i][j] = morpion.plateau[i][j]
    morp = Morpion(morpion.numJoueur,nplateau,morpion.etat)
    la= []
    for a in morp.Actions():
        la.append((a,Min_Value(morp.Result(a))))
    la = sorted(la, key = lambda val:val[1])
    return la[0][0]

def Min_Value(morpion):
    if(morpion.Terminal_Test()):
        return morpion.Utility()
    score_min = 100000
    for a in morpion.Actions():
        score_min = min(score_min,Max_Value(morpion.Result(a)))
    return score_min

def Max_Value(morpion):
    if(morpion.Terminal_Test()):
        return morpion.Utility()
    score_max = -100000
    for a in morpion.Actions():
        score_max = max(score_max,Min_Value(morpion.Result(a)))
    return score_max

def RepresentsInt(s):
    try: 
        s = int(s)
        if(s<0):
            return False
        return True
    except ValueError:
        return False

def Partie():
    numjoueur = input("Numero de joueurs ?\n") #correspond a notre ia
    m = Morpion(int(numjoueur))
    while(m.win() == 0):
        m.Afficher()
        if(m.etat == m.numJoueur):
            print("************************\n*    Au tour de l'ia   *\n************************")
            print("Début du MinMax")
            val = MinMax_Decision(m)
            print(f"Valeur a jouer : {val}")
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
        valWin = m.win()
        winner = "Null" if valWin == 0 else "J1" if valWin == 1 else "J2"
        print(f"Fin de partie ! Gagnant : {winner}")
                
    

#%% Zone Main
if __name__ == "__main__":
    Partie()
    """
    morp = Morpion()
    while(morp.win() == 0):
        a = morp.Utility()
        morp.Result(a[0],a[1])                
        morp.Afficher()
        print('\n')
        time.sleep(1)
    print('j1' if morp.win() == 1 else 'j2' if morp.win() == -1 else 'No win')
    """
