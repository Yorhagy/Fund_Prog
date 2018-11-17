#%%

def coordenadas(X, Y, Z, N):
  return [(i, j, k) for i in range(X + 1) for j in range(Y + 1)
          for k in range(Z + 1) if i+j+k != N]

print('Coordenadas: ', coordenadas(5, 3, 2, 30))

#%%

def palindromos(numeros):
  return all([numero == numero[::-1] for numero in numeros.split()])

if palindromos('55 666777 153'):
    print('Son positivos y Palindromos')
else: 
    print('No lo son')

#%%

leest = [ 'We are learning Python', 'Functional programming in Python', 
  'What are this Python functions for?', 'Do we really need Python?', 'Python rulez!']

def rePython(leest):
  return sum([True for string in leest for word in string.split() if 'Python' in word]) 

print('La palabra python se repite: ', (rePython(leest)))

#%%

def resultado(numero, divisor):
  return sum([i for i in range(numero + 1) if (i**2) % divisor == 0])

print('El resultado es: ' ,resultado(50,5))

#%%
def Fibonacci(x):
  if x == 1 : return [1]
  elif x == 2 : return [1, 1]
  else : 
      f = Fibonacci(x - 1)
      return f + [f[-1] + f[-2]]
  
print('El resultado es: ', [f**3 for f in Fibonacci(30)])

#%%

def appendChar(char, grupo):
    if len(grupo) == 0:
        return  [char]
    elif char == grupo[-1][-1]:
        nuevoGrupo = grupo.copy()
        nuevoGrupo[-1] = nuevoGrupo[-1] + char 
        return nuevoGrupo
    else :
        return grupo + [char]


def groupby(chain, grupo = []):
    if len(chain) == 1:
        return appendChar(chain[0], grupo)
    else :
        return groupby(chain[1:], appendChar(chain[0], grupo))
    
recibido = '111116666677cc77777'
grupos = [(len(chain), chain[0]) for chain in groupby(recibido) ]
print('Tuplas:', grupos) 

