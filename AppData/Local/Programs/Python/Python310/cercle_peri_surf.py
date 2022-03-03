import math
#from math import pi # importer la constante pi=3.14... de la bibliothèque math 
def permitre_surface_cercle():
    x = float(input("entrer le rayon n :"))
    perimetre = 2*x* math.pi
    
    surface = x*x*math.pi
     
    print(perimetre)
    print(surface)
    
    
permitre_surface_cercle()
