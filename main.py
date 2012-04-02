import random,pygame
from pygame.locals import *
from classes import *

COL=10
ROWS=20

def affichage(jeu):
    for i in jeu:
        print(i)

def affichage2(fenetre,jeu):
    for i in range(len(jeu)):
        for j in range(len(jeu[0])):
            fenetre.fill(jeu[i][j],(j*25,i*25,j*25+25,i*25+25))
    return fenetre

def ajouter(jeu,p):
    p_aux = p.liste
    for i in p_aux:
        jeu[i[0]][i[1]]=p.couleur
    return jeu

#gestion des collisions de chute
def stop(jeu,p):
    for i in range(len(p.liste)):
        #si on est descendu tout en bas
        if(p.liste[i][0]+1==len(jeu)):
            return True
        #si il y a deja une piece en dessous 
        if(jeu[p.liste[i][0]+1][p.liste[i][1]]!=(0,0,0)):
            appartient=False
            for j in range(len(p.liste)):
                if(p.liste[j][0]==p.liste[i][0]+1 and p.liste[j][1]==p.liste[i][1]):
                    appartient=True
                    break
            if(appartient==False):
                return True
    return False

#savoir si le joueur a perdu ou si on peut enlever des lignes pleines
def complete_ligne(jeu,p):
    global jouer
    min_i=p.liste[0][0]
    for i in p.liste:
        if(i[0]<min_i):
            mini_i=i[0]
    if min_i<=0:
        print("Game Over")
        jouer=0
        return jeu
    trou=False
    for i in range(len(jeu)-1,min_i,-1):
        trou=False
        for j in range(len(jeu[0])):
            if(jeu[i][j]==(0,0,0)):
                trou=True
        if(not trou):
            print("Ligne Complete")
            for k in range(i,0,-1):
                for l in range(len(jeu[0])):
                    jeu[k][l]=jeu[k-1][l]
    if(trou==True):
        return jeu
    else:
        return complete_ligne(jeu,p)

#{main}-------------------------------------------------+
jeu=[[(0,0,0) for i in range(COL)] for i in range(ROWS)]#
pygame.init()                                           #
pygame.event.set_blocked(None)                          #
pygame.event.set_allowed((KEYDOWN,QUIT))                #
pygame.key.set_repeat(75,0)                             #
pygame.display.set_caption("Tetris")                    #
fenetre=pygame.display.set_mode((COL*25,ROWS*25))       #
pygame.display.flip()                                   #
last_line=jeu[len(jeu)-1]
jouer=1                    
while jouer:                                     
    p = random.choice([I(),O(),T(),L(),J(),S(),Z()])                  
    fenetre=affichage2(fenetre,jeu)
    jeu = ajouter(jeu,p)
    pygame.time.set_timer(KEYDOWN,500)
    for i in range(50):
        jeu[len(jeu)-1]=last_line
        if(not stop(jeu,p)):
            jeu = p.descendre(jeu)
        else:
            last_line=jeu[len(jeu)-1]
            break
        event = pygame.event.wait()
        if event.type==QUIT or event.key==K_ESCAPE: 
            exit(0)
        
        if event.key==K_DOWN and not stop(jeu,p):
            jeu=p.descendre(jeu)
        if event.key==K_RIGHT:
            jeu = p.esquive(jeu,1)
        if event.key==K_LEFT:
            jeu = p.esquive(jeu,-1)
        if event.key==K_UP:
            jeu = p.rotation(jeu)
        fenetre=affichage2(fenetre,jeu)
        pygame.display.flip()
    jeu = complete_ligne(jeu,p)
    p.liste=p.coord()
    if(jouer==0):
        break
