#RIVERA VARGAS JUAN

matriz=[["111111110000000000011111111111000000000000111111111"],
   ["111111000000001111100000111000000222220000000111111"],
   ["111100000001111111111111000333333333333330000011111"],
   ["111000000011111111111111104444444444444444400001111"],
   ["110000001111111111111111111111111444444444440000111"],
   ["110000011111111111111111111111111111155555550000011"],
   ["100000111111111111111111111111111111111155550000011"],
   ["100000111111111111111111111111111111111111100000011"],
   ["110000001111111111111111111111111111111110000000111"],
   ["111000000011111111111111111111111111111100000001111"],
   ["111110000001111111111111111111111111111000000111111"],
   ["111111100000011111111111111111111111100000011111111"],
   ["111111111100000111111111111111111111000011111111111"],
   ["111111111111100001111111111111111100001111111111111"],
   ["111111111111111000011111111111110001111111111111111"],
   ["111111111111111110001111111110001111111111111111111"],
   ["111111111111111111110001111100111111111111111111111"],
   ["111111111111111111111100110011111111111111111111111"],
   ["111111111111111111111111001111111111111111111111111"]]

   # convierte la matriz anterior en una matriz numerica
z=[]
for elemento in matriz:
  for cadena in elemento:
    lista_1=[]
    for numero in cadena:
      lista_1.append(int(numero))
    z.append(lista_1)

m=len(z[0])
n=len(z)


convolucion=[[0,1,1],
[1,-4,1],
[0,1,0]]



#otra es la nueva matriz formada
otra=[]
#itera entre renglones
for r in range(1,n-1):
  #se guarda cada linea en una lista
  primera=[]
  #itera entre columnas
  for c in range(1,m-1):
    #pixeles superiores
    r_superior_izq=z[r-1][c-1]*convolucion[0][0]
    r_superior=z[r-1][c]*convolucion[0][1]
    r_superior_der=z[r-1][c+1]*convolucion[0][2]
    #pixeles centrales
    izq=z[r][c-1]*convolucion[1][0]
    centro=z[r][c]*convolucion[1][1]
    der=z[r][c+1]*convolucion[1][2]
    #pixeles inferiores
    r_inferior_izq=z[r+1][c-1]*convolucion[2][0]
    r_inferior=z[r+1][c]*convolucion[2][1]
    r_inferior_der=z[r+1][c+1]*convolucion[2][2]

    #z[r][c]= r_superior_izq + r_superior + r_superior_der + izq + centro + der + r_inferior_izq + r_inferior + r_inferior_der
    #se guarda el resultado y se añade a la lista
    a=r_superior_izq + r_superior + r_superior_der + izq + centro + der + r_inferior_izq + r_inferior + r_inferior_der
    primera.append(a)
  #se añade la lista a la matriz
  otra.append(primera)


#imprime la nueva matriz
print()
print()
for renglon in otra:
  linea=''.join(str(numero)for numero in renglon)
  #imprimimos cada linea
  print(linea)