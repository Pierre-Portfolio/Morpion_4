# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:31:49 2021

@author: tompa
"""
import numpy as np
import time
import random
import copy

Prof= 4
count = 0
class Morpion():
    def __init__(self, numJoueur = 1,plateau=None, etat = None,N = 12, lcj=None):
        self.N = N
        if lcj == None:
            self.listeCoupJoue=[]
        else:
            self.listeCoupJoue = lcj
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
        col = '   '
        for k in range(self.N):
            col += ' '+str(k+1)
        print(col)
        for i in range(self.N):
            s = '  '+str(i+1) if i+1 < 10 else ' '+str(i+1)
            for j in range(self.N):
                s += ' '+self.plateau[i][j]
            print(s)
    
    def finDePartie(self):
        for k in range(self.N):
            for l in range(self.N):
                if self.plateau[k][l]=='.':
                    return False
        return True
    
    def TestBottom(self,i,j,chara,nbrIt=0):
        if i>=self.N:
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
        if j < self.N and nbrIt < 4 and self.plateau[i][j] == chara:
            return self.TestRight(i,j+1,chara,nbrIt+1)
        return nbrIt
    
    def TestLeft(self,i,j,chara,nbrIt=0):
        if j >= 0 and nbrIt < 4 and self.plateau[i][j]==chara:
            return self.TestLeft(i,j-1,chara,nbrIt+1)
        return nbrIt
    
    def TestBottomRight(self,i,j,chara,nbrIt=0):
        if (i>=self.N) or (j>=self.N):
            return nbrIt
        if nbrIt==4:
            return nbrIt
        if self.plateau[i][j]==chara:
            return self.TestBottomRight(i+1,j+1,chara,nbrIt+1)
        return nbrIt
    
    def TestBottomLeft(self,i,j,chara,nbrIt=0):
        if (i>=self.N) or (j<0):
            return nbrIt
        if nbrIt==4:
            return nbrIt
        if self.plateau[i][j]==chara:
            return self.TestBottomLeft(i+1,j-1,chara,nbrIt+1)
        return nbrIt
    
    def TestUpperRight(self,i,j,chara,nbrIt=0):
        if (i<0) or (j>=self.N):
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
        for i in range(self.N):
            if i%4 == 0:  
                for j in range(self.N):
                    if (self.plateau[i][j] != '.') and ( (self.TestBottom(i+1,j, self.plateau[i][j])+ self.TestUpper(i-1,j,self.plateau[i][j])== 3 ) or (self.TestLeft(i,j-1, self.plateau[i][j])+ self.TestRight(i,j+1,self.plateau[i][j]) == 3) or (self.TestBottomRight(i+1,j+1, self.plateau[i][j])+ self.TestUpperLeft(i-1,j-1,self.plateau[i][j]) == 3) or (self.TestUpperRight(i-1,j+1, self.plateau[i][j])+ self.TestBottomLeft(i+1,j-1,self.plateau[i][j]) == 3) ):                   
                        res = self.plateau[i][j]                       
            else:
                for j in range(0,self.N,4):
                    if (self.plateau[i][j] != '.') and ( (self.TestBottom(i+1,j, self.plateau[i][j])+ self.TestUpper(i-1,j,self.plateau[i][j])== 3 ) or (self.TestLeft(i,j-1, self.plateau[i][j])+ self.TestRight(i,j+1,self.plateau[i][j]) == 3) or (self.TestBottomRight(i+1,j+1, self.plateau[i][j])+ self.TestUpperLeft(i-1,j-1,self.plateau[i][j]) == 3) or (self.TestUpperRight(i-1,j+1, self.plateau[i][j])+ self.TestBottomLeft(i+1,j-1,self.plateau[i][j]) == 3) ):                   
                        res = self.plateau[i][j]                   
            if res != '.':
                break;  
        if ( res == 'O'):
            return (2)
        elif res == 'X':
            return (1)
        elif (self.finDePartie()): #MatchNull
            return -1
        else:
            return (0)
        
    def Actions(self):
        coups = [];
        for i in range(self.N):
            for j in range(self.N):
                if(self.plateau[i][j] == '.'):
                   coups.append((i,j))
        return coups
    
    def Result(self,a):
        self.listeCoupJoue.append(a)
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
        self.listeCoupJoue.remove(a)
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
        for i in range(self.N):
            for j in range(self.N):
                if((val ==  1 and self.plateau[i][j]=='X') or (val ==  2 and self.plateau[i][j]=='O')):
                    res += 1
        return res
    
    def Evaluate(self,a):
        # J1 : Bloquer un Trio > Poser un Trio > Poser un duo > bloquer un duo > Poser Solo
        # J2 : Bloquer un Trio > Poser un Trio > Bloquer un duo > poser un duo > Poser Solo
        x = a[0]
        y = a[1]
        bloqueT, nbT = self.bloqueTrio(x, y)
        bloqueD, nbD = self.bloqueDuo(x, y)
        score = nbD + nbT
        if bloqueT:
            score += 60 - self.ComptPions(self.numJoueur)
        if self.isTrio(x, y):
            score += 40 - self.ComptPions(self.numJoueur)
            if bloqueT: #Si isTrio + bloque score * 10
                score= score * 10
            elif bloqueD:
                score= score * 5
        if bloqueD:
            score += 20 if self.numJoueur == 2 else 10
            score -= self.ComptPions(self.numJoueur)
        if self.isDuo(x, y):
            score += 20 if self.numJoueur == 1 else 10
            score -= self.ComptPions(self.numJoueur)    
        if self.VoisinProche(x,y):
            score += 1                 
        #print(f'score:{score} pour la pose : {x},{y}')
        return score
    
    def Utility(self, a):
        score = 0
        if(self.Terminal_Test()):
            win = self.win()
            if(win == self.numJoueur):
                score += 10000 - self.ComptPions(self.numJoueur)
            elif(win == -1):
                return 10
            else:
                score+= -10000 + self.ComptPions(1 if self.numJoueur == 2 else 2)
        chara = 'X' if self.numJoueur == 1 else 'O'
        for point in self.listeCoupJoue:
            if self.plateau[point[0]][point[1]] == chara:
                score += self.Evaluate(point)
        return score
        """
        # J1 : Bloquer un Trio > Poser un Trio > Poser un duo > bloquer un duo > Poser Solo
        # J2 : Bloquer un Trio > Poser un Trio > Bloquer un duo > poser un duo > Poser Solo
        x = a[0]
        y = a[1]
        bloqueT, nbT = self.bloqueTrio(x, y)
        bloqueD, nbD = self.bloqueDuo(x, y)
        score = nbD + nbT
        if bloqueT:
            score += 60 - self.ComptPions(self.numJoueur)
        if self.isTrio(x, y):
            score += 40 - self.ComptPions(self.numJoueur)
            if bloqueT: #Si isTrio + bloque score * 10
                score= score * 10
            elif bloqueD:
                score= score * 5
        if bloqueD:
            score += 20 if self.numJoueur == 2 else 10
            score -= self.ComptPions(self.numJoueur)
        if self.isDuo(x, y):
            score += 20 if self.numJoueur == 1 else 10
            score -= self.ComptPions(self.numJoueur)    
        if self.VoisinProche(x,y):
            score += 1                 
        #print(f'score:{score} pour la pose : {x},{y}')
        return score
        """
        
#%% Autre fonctions
    def VoisinProche(self,x,y):
        xmin = 0 if x <= 0 else x-1
        ymin = 0 if y <= 0 else y-1
        xmax = self.N-1 if x >= self.N-1 else x+1
        ymax = self.N-1 if y >= self.N-1 else y+1
        chara = 'X' if self.numJoueur == 2 else 'O'
        for i in range(xmin,xmax+1):
            for j in range(ymin,ymax+1):
                if self.plateau[i][j] == chara:
                    return True
        return False
        
    def isSolo(self,x,y):
        if (self.plateau[x][y] != '.') and ( (self.TestBottom(x+1,y, self.plateau[x][y])+ self.TestUpper(x-1,y,self.plateau[x][y])== 0 ) or (self.TestLeft(x,y-1, self.plateau[x][y])+ self.TestRight(x,y+1,self.plateau[x][y]) == 0) or (self.TestBottomRight(x+1,y+1, self.plateau[x][y])+ self.TestUpperLeft(x-1,y-1,self.plateau[x][y]) == 0) or (self.TestUpperRight(x-1,y+1, self.plateau[x][y])+ self.TestBottomLeft(x+1,y-1,self.plateau[x][y]) == 0)):
            return True
        return False
    
    def isDuo(self,x,y):
        if (self.plateau[x][y] != '.') and ( (self.TestBottom(x+1,y, self.plateau[x][y])+ self.TestUpper(x-1,y,self.plateau[x][y])== 1 ) or (self.TestLeft(x,y-1, self.plateau[x][y])+ self.TestRight(x,y+1,self.plateau[x][y]) == 1) or (self.TestBottomRight(x+1,y+1, self.plateau[x][y])+ self.TestUpperLeft(x-1,y-1,self.plateau[x][y]) == 1) or (self.TestUpperRight(x-1,y+1, self.plateau[x][y])+ self.TestBottomLeft(x+1,y-1,self.plateau[x][y]) == 1)):
            return True
        return False
    
    def isTrio(self,x,y):
        if (self.plateau[x][y] != '.') and ( (self.TestBottom(x+1,y, self.plateau[x][y])+ self.TestUpper(x-1,y,self.plateau[x][y])== 2 ) or (self.TestLeft(x,y-1, self.plateau[x][y])+ self.TestRight(x,y+1,self.plateau[x][y]) == 2) or (self.TestBottomRight(x+1,y+1, self.plateau[x][y])+ self.TestUpperLeft(x-1,y-1,self.plateau[x][y]) == 2) or (self.TestUpperRight(x-1,y+1, self.plateau[x][y])+ self.TestBottomLeft(x+1,y-1,self.plateau[x][y]) == 2)):
            return True
        return False
    
    def bloqueDuo(self,x,y):
        res = 0
        b = False
        xmin = 0 if x <= 0 else x-1
        ymin = 0 if y <= 0 else y-1
        xmax = self.N-1 if x >= self.N-1 else x+1
        ymax = self.N-1 if y >= self.N-1 else y+1
        chara = 'X' if self.numJoueur == 2 else 'O'
        for i in range(xmin,xmax+1):
            for j in range(ymin,ymax+1):
                if i!=x or j!=y:
                    if i == x-1 and j == y-1:
                        if self.TestUpperLeft(i, j, chara,2)  == 4:
                            b = True
                            res += 1
                    elif i == x-1 and j == y:
                        if self.TestUpper(i, j, chara,2) == 4:
                            b = True
                            res += 1
                    elif i == x-1 and j == y+1:
                        if self.TestUpperRight(i, j, chara,2) == 4:
                            b = True
                            res += 1
                    elif i == x and j == y-1:
                        if self.TestLeft(i, j, chara,2) == 4:
                            b = True
                            res += 1
                    elif i == x and j == y+1:
                        if self.TestRight(i, j, chara,2) == 4:
                            b = True
                            res += 1
                    elif i == x+1 and j == y-1:
                        if self.TestBottomLeft(i, j, chara,2) == 4:
                            b = True
                            res += 1
                    elif i == x+1 and j == y:
                        if self.TestBottom(i, j, chara,2) == 4:
                            b = True
                            res += 1
                    elif i == x+1 and j == y+1:
                        if self.TestBottomRight(i, j, chara,2) == 4:
                            b = True
                            res += 1
        return res,b
    
    def bloqueTrio(self,x,y):
        res = 0
        b = False
        xmin = 0 if x <= 0 else x-1
        ymin = 0 if y <= 0 else y-1
        xmax = self.N-1 if x >= self.N-1 else x+1
        ymax = self.N-1 if y >= self.N-1 else y+1
        chara = 'X' if self.numJoueur == 2 else 'O'
        for i in range(xmin,xmax+1):
            for j in range(ymin,ymax+1):
                if i!=x or j!=y:
                    if i == x-1 and j == y-1:
                        if self.TestUpperLeft(i, j, chara,1) == 4:
                            b = True
                            res += 1
                    elif i == x-1 and j == y:
                        if self.TestUpper(i, j, chara,1) == 4:
                            b = True
                            res += 1
                    elif i == x-1 and j == y+1:
                        if self.TestUpperRight(i, j, chara,1) == 4:
                            b = True
                            res += 1
                    elif i == x and j == y-1:
                        if self.TestLeft(i, j, chara,1) == 4:
                            b = True
                            res += 1
                    elif i == x and j == y+1:
                        if self.TestRight(i, j, chara,1) == 4:
                            b = True
                            res += 1
                    elif i == x+1 and j == y-1:
                        if self.TestBottomLeft(i, j, chara,1) == 4:
                            b = True
                            res += 1
                    elif i == x+1 and j == y:
                        if self.TestBottom(i, j, chara,1) == 4:
                            b = True
                            res += 1
                    elif i == x+1 and j == y+1:
                        if self.TestBottomRight(i, j, chara,1) == 4:
                            b = True
                            res += 1
        return res,b
#%% Algo Minmax
def decoTimer(fonction):
    def inner(*param, **param2):
        tic = time.perf_counter()
        print(f'Début de la recherche : {tic}')
        val = fonction(*param, **param2)
        tac = time.perf_counter()
        print(f"Temps d'execution de {tac - tic:0.6f} sec")
        return val
    return inner

def getSubTab(morpion):
    imin=11
    imax=0
    jmin=11
    jmax=0
    for point in morpion.listeCoupJoue:
        #print("test getSubTAb")
        if imin>=point[0]-2:
            imin=max(0,point[0]-2)
        if imax<=point[0]+2:
            imax=min(11,point[0]+2)
        if jmin>=point[1]-2:
            jmin=max(0,point[1]-2)
        if jmax<=point[1]+2:
            jmax=min(11,point[1]+2)
        iminsave = imin
        imaxsave = imax
        jminsave = jmin
        jmaxsave = jmax
        Nmax = max(imax-imin,jmax-jmin)
        while jmax-jmin>imax-imin:
            if imin>0:
                imin-=1
            if jmax-jmin>imax-imin:
                if imax<11:
                    imax+=1
                else:
                    imin-=1
        while imax-imin>jmax-jmin:
            if jmin>0:
                jmin-=1
            if imax-imin>jmax-jmin:
                if jmax<11:
                    jmax+=1
                else:
                    jmin-=1
    return [imin,jmin],[imax,jmax], abs(jmax-jmin)

@decoTimer
def MinMax_Decision(morpion):
    global count
    count = 0
    copy_morp = copy.deepcopy(morpion)
    copy_morp.Afficher()
    indexMin, indexMax, newN = getSubTab(copy_morp)
    #Création du sous tableau
    print(indexMin)
    print(indexMax)
    nplateau = [['.' for i in range(indexMin[0],indexMax[0]+1)] for j in range(indexMin[1],indexMax[1]+1)]
    for i in range(newN):
        for j in range(newN):
            #print(f'i:{i},j:{j}')
            nplateau[i][j] = copy_morp.plateau[i+indexMin[0]][j+indexMin[1]]
    morp = Morpion(copy_morp.numJoueur,nplateau,copy_morp.etat,newN)
    la= []
    etatBase = morp.etat
    for a in morp.Actions():
        la.append((a,Max_Value(morp.Result(a),a,Prof)))
        morp.Afficher()
        morp.UnResult(a, etatBase)
    la = sorted(la, key = lambda val:val[1], reverse = True)
    print(la)
    res = (la[0][0][0]+indexMin[0],la[0][0][1]+indexMin[1])
    print(f'{indexMin[0]},{indexMin[1]}')
    return res

def Min_Value(morpion,a, profondeur = 0, alpha = -1000000, beta=1000000):
    global count
    count += 1
    if(morpion.Terminal_Test() or profondeur == 0):
        etatBase = morpion.etat
        morpion.Result(a)
        val = morpion.Utility(a)
        morpion.UnResult(a, etatBase)
        return val
    score_min = 100000
    etatBase = morpion.etat
    profondeur -= 1
    for a in morpion.Actions():
        score_min = min(score_min,Max_Value(morpion.Result(a),a,profondeur,alpha,beta))
        morpion.UnResult(a, etatBase)
        beta = min(score_min,beta)
        if beta <= alpha:
            break
    return score_min

def Max_Value(morpion, a, profondeur = 0, alpha = -1000000, beta = 1000000):
    global count
    count += 1
    if(morpion.Terminal_Test() or profondeur == 0):
        etatBase = morpion.etat
        morpion.Result(a)
        val = morpion.Utility(a)
        morpion.UnResult(a, etatBase)
        return val
    score_max = -100000
    etatBase = morpion.etat
    profondeur -= 1
    for a in morpion.Actions():
        score_max = max(score_max,Min_Value(morpion.Result(a),a,profondeur,alpha,beta))
        morpion.UnResult(a, etatBase)
        alpha = max(alpha,score_max)
        if beta <= alpha:
            break
    return score_max

#%% Game
def RepresentsInt(s):
    try: 
        s = int(s)
        if(s<=0 or s > 12):
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
                val = MinMax_Decision(m)
                print(f'nb calcul :{count}')
                print(f"Valeur a jouer : {val[0]+1},{val[1]+1}")
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
            m = m.Result((i-1,j-1))
        nbCoups += 1
    valWin = m.win()
    winner = "Null" if valWin == 0 else "J1" if valWin == 1 else "J2"
    print(f"Fin de partie ! Gagnant : {winner}")
    m.Afficher()
                
    

#%% Zone Main
if __name__ == "__main__":
    Partie()