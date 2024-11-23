print()
print("Edgar Gael Garcia Camacho 1182 3w:calentamiento")
print()
def es_palindromo(palabra):
   
    palabra = palabra.lower()
    
   
    if palabra == palabra[::-1]:
        return True
    else:
        return False

print(es_palindromo("pollos"))   
print(es_palindromo("los mejores")) 
print(es_palindromo("ojo"))    
