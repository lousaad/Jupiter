def verifie(liste):
    i=1
    while i < len(liste):
        if liste[i] > liste[i-1]:
            i+=1
        else:
            return False
    return True
print(verifie([0,5,6,7,8]))
print(verifie([0,5,9,7,8]))
print(verifie([]))

    
