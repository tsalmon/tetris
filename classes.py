class piece():
    def rotation(self,jeu):
        if(type(self.point)==type(None)):
            return jeu
        else:
            self.rotation_=self._rotation()
            for i in range(len(self.rotation_[self.rot])):
                if( self.rotation_[self.rot][i][0]+self.point[0]<0 or self.rotation_[self.rot][i][1]+self.point[1]>=len(jeu[0])): 
                    return jeu
            for i in range(len(self.rotation_[self.rot])):
                jeu[self.liste[i][0]][self.liste[i][1]]=(0,0,0)
                self.liste[i][0]=self.rotation_[self.rot][i][0]+self.point[0]
                self.liste[i][1]=self.rotation_[self.rot][i][1]+self.point[1]
                jeu[self.liste[i][0]][self.liste[i][1]]=self.couleur
            self.rot=(self.rot+1)%len(self._rotation())
            return jeu
        
    def descendre(self,jeu):
        p_aux=self.liste
        for i in range(len(p_aux)-1,-1,-1):
            jeu[p_aux[i][0]][p_aux[i][1]]=(0,0,0)
            jeu[p_aux[i][0]+1][p_aux[i][1]]=self.couleur
            self.liste[i][0]+=1
        if(type(self.point)!=type(None)):
            self.point[0]+=1
        return jeu

    def esquive(self,jeu,move):
        for i in self.liste:
            if(i[1]+move==-1 or i[1]+move==len(jeu[0])):
               return jeu
            if(jeu[i[0]][i[1]+move]!=(0,0,0)):
                appartient=False
                for j in self.liste:
                    if(i[0]==j[0] and i[1]+move==j[1]):
                        appartient=True
                if(appartient==False):
                    return jeu
        p_aux=self.liste
        for i in range(len(p_aux)-1,-1,-1):
            jeu[p_aux[i][0]][p_aux[i][1]]=(0,0,0)
            jeu[p_aux[i][0]][p_aux[i][1]+move]=self.couleur
            self.liste[i][1]+=move
        if(type(self.point)!=type(None)):
            self.point[1]+=move
        return jeu
    
class I(piece):
    "cyan"
    def coord(self):
        return [[-1,5],[0,5],[1,5],[2,5]]
    def _rotation(self):
        return [
            self.coord(),
            [[0,0],[0,1],[0,2],[0,3]]
            ]
    def __init__(self):
        #self.liste=self.coord()
        self.liste=[[-1,5],[0,5],[1,5],[2,5]]
        self.couleur=(0,203,214)
        self.point=[0,5]
        self.rot=1

class O(piece):
    "bleu"
    def coord(self):
        return [[-1,5],[-1,6],[0,5],[0,6]]
    def _rotation(self):
        return []
    def __init__(self):
        self.liste=self.coord()
        self.couleur=(0,0,255)
        self.point=None
        self.rot=1

class T(piece):
    "jaune"
    def coord(self):
        return [[-1,5],[0,5],[1,5],[0,6]]
    def _rotation(self):
        return [
            self.coord(),
            [[0,0],[0,1],[0,2],[1,1]],
            [[0,1],[1,1],[2,1],[1,0]],
            [[1,0],[1,1],[1,2],[0,1]]
            ]
    def __init__(self):
        self.liste=self.coord()
        self.couleur=(255,255,0)
        self.point=[0,5]
        self.rot=1

class L(piece):
    "violet"
    def coord(self):
        return [[-1,5],[0,5],[1,5],[1,6]]
    def _rotation(self):
        return [
            self.coord(),
            [[0,0],[0,1],[0,2],[1,0]],
            [[0,0],[0,1],[1,1],[2,1]],
            [[1,0],[1,1],[1,2],[0,2]],
            ]
    def __init__(self):
        self.liste=self.coord()
        self.couleur=(161,0,206)
        self.point=[1,5]
        self.rot=1

class J(piece):
    "orange"
    def coord(self):
        return [[0,5],[1,5],[2,5],[2,4]]
    def _rotation(self):
        return [
            self.coord(),
            [[2,0],[2,1],[1,1],[0,1]],
            [[0,0],[1,0],[2,0],[1,0]],
            [[0,0],[1,0],[2,0],[2,1]]
            ]
    def __init__(self):
        self.liste=self.coord()
        self.couleur=(255,165,0)
        self.point=[2,5]
        self.rot=1

class S(piece):
    "rouge"
    def coord(self):
        return [[-1,6],[-1,7],[0,5],[0,6]]
    def _rotation(self):
        return [
            self.coord(),
            [[0,0],[1,0],[1,1],[2,1]]
            ]
    def __init__(self):
        self.liste=self.coord()
        self.couleur=(255,0,0)
        self.point=[-1,7]
        self.rot=1

class Z(piece):
    "vert"
    def coord(self):
        return [[-1,5],[-1,6],[0,6],[0,7]]
    def _rotation(self):
        return [
            self.coord(),
            [[0,1],[1,1],[1,0],[2,0]]
            ]
    def __init__(self):
        self.liste=self.coord()
        self.couleur=(0,255,0)
        self.point=[-1,6]
        self.rot=1
