from random import randint

class Dé :
    
    def __init__(self):
        self.dé = randint(1,6)
        
    def __repr__(self):
        return f'{self.dé}'

class Joueur:
    
    def __init__(self, nom_joueur):
        self.joueur = nom_joueur
        self.nbjeton = 21
        self.point=0
        
    def __repr__(self):
        return f"{self.joueur, self.nbjeton, self.point}"

    
    def lancer_dé(self):
        dé1 = Dé()
        dé2 = Dé()
        dé3 = Dé()
        return sorted([dé1.dé, dé2.dé, dé3.dé])
    
    
    def combinaison(self, L):
        if L == [1, 2, 4]:
            self.point += 10
        elif L == [1, 1, 1]:
            self.point += 7
        elif L == [1, 1, 6] or L == [6, 6, 6]:
            self.point += 6
        elif L == [1, 1, 5] or L == [5, 5, 5]:
            self.point += 5
        elif L == [1, 1, 4] or L == [4, 4, 4]:
            self.point += 4
        elif L == [1, 1, 3] or L == [3, 3, 3]:
            self.point += 3
        elif L == [1, 1, 2] or L == [2, 2, 2]:
            self.point += 2
        elif L == [1, 2, 3] or L == [2, 3, 4]:
            self.point += 2
        elif L == [3, 4, 5] or L == [4, 5, 6]:
            self.point += 2
        else :
            self.point += 1
        return self.point
     
        
class Lancer:
    
    def __init__(self, lancer):
        self.valeur = lancer
        self.repr = ''.join([str(k) for k in lancer])
        
    def combinaison(self):
        L = self.valeur
        if L == [1, 2, 4]:
            return 10
        elif L == [1, 1, 1]:
            return 7
        elif L == [1, 1, 6] or L == [6, 6, 6]:
            return 6
        elif L == [1, 1, 5] or L == [5, 5, 5]:
            return 5
        elif L == [1, 1, 4] or L == [4, 4, 4]:
            return 4
        elif L == [1, 1, 3] or L == [3, 3, 3]:
            return 3
        elif L == [1, 1, 2] or L == [2, 2, 2]:
            return 2
        elif L == [1, 2, 3] or L == [2, 3, 4]:
            return 2
        elif L == [3, 4, 5] or L == [4, 5, 6]:
            return 2
        else :
            return 1
          
class Jeu :
    
    def __init__(self, nom):
        self.partie = nom
        self.joueur = {}
        self.lancer = None
        self.pot = 21
        
    def add_joueur(self, nom_du_joueur):
        self.joueur[nom_du_joueur] = Joueur(nom_du_joueur)
        
    def __repr__(self):
        res=''
        for j in self.joueur:
            res += repr(self.joueur[j]) + '\n'
        return res
    
    
jeu1 = Jeu('jeu1')
jeu1.add_joueur("Sam")
jeu1.add_joueur("Robyn")
while not jeu1.pot == 0 :
    a = jeu1.joueur["Sam"].lancer_dé()
    b = jeu1.joueur["Robyn"].lancer_dé()
    print (a)
    print (b)
    
    l = Lancer(a).combinaison()
    
    if jeu1.pot < l:
        jeu1.joueur["Sam"].nbjeton += jeu1.pot
        break
    
    
    point1 = Lancer(a).combinaison()
    print(jeu1.joueur["Sam"].nbjeton)
    jeu1.pot -= Lancer(a).combinaison()
    
    l2 = Lancer(b).combinaison()
    
    if jeu1.pot < l2:
        jeu1.joueur["Robyn"].nbjeton += jeu1.pot
        break
    
    point2 = Lancer(b).combinaison()
    print(jeu1.joueur["Robyn"].nbjeton)
    jeu1.pot -= Lancer(b).combinaison()
    
    print(jeu1.pot)
    
c = jeu1.joueur["Sam"].nbjeton
d = jeu1.joueur["Robyn"].nbjeton
    
if c < d:
    print ("Robyn a gagné")
elif c > d:
    print("Samuel a gagné")
else :
    print ("Egalité")
    
    

        
        
        
        
        
        
        
    
    
        