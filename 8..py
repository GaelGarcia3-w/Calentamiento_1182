print()

print("Edgar Gael Garcia Camacho 1182 3w:Calentamiento")

print()

def superposicion(lista1, lista2):
    
  for elem1 in lista1:
        
   for elem2 in lista2:
            
    if elem1 == elem2:
  
     return True
    
  return False

print(superposicion([1, 2, 3], [4, 5, 6]))  

print(superposicion([1, 2, 3], [3, 4, 5]))  

print(superposicion(['a', 'b', 'c'], ['x', 'y', 'z', 'a']))  
