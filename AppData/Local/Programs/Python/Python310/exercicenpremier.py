import math
def dviseurdeNBrePremier():
    listdediviseurdeN = []
    print(listdediviseurdeN)
    x =  int(input("entrer le nombre entier n : "))
    for i in range(1, x+1):
        a = (math.fmod(x,i))
        if a == 0:
            #print(int(i))
            listdediviseurdeN.append(i)
    print(listdediviseurdeN)
    #if len(listdediviseurdeN)==2:
    if listdediviseurdeN[1]==x:
        print(x," : est un nombre premier")
    else:
         print(x," : n'est pas un nombre premier")
           

            
    
    
    
dviseurdeNBrePremier()
