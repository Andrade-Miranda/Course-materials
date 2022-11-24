

# declarar datos
Peso = 75
talla = 1.8
IMC = Peso/talla^2
IMC


# crear una funcion
imc = function(Peso, talla) 
Peso/talla^2
imc(Peso, talla)

# creación de vectores
vecy =c(2, 3, 4, 5, 6, 7)
vecx= 10:15 #creo vector con valores 10,11,12,13,..15
vecx * 2 # multiplicación por un escalar
vecx[1] 
vecx[4:5]# los elementos se enumeran desde 1 hasta longuitud máxima
vecx > 12
vecx[vecx > 12]

#creación de matrices
z1=matrix(1:12, nrow = 4, ncol = 3)
Z2 = matrix(1:12, nrow = 4, ncol = 3, byrow = TRUE)
Z3 = array(1:12, dim = c(2, 3, 2))

# tipo de dataframe 
IMCT=data.frame(
  sexe=c("H","F","F"),
  poidsT=c(76,56,57),
  tailleT=c(1.78,1.67,1.68),
  row.names=c("TOTO","TITI","TATA"))

#acceder a uno de los campos
IMCT$poidsT
IMCT[[2]] #segunda columna
IMCT[2:3]
IMCT[c("poidsT", "tailleT")]
IMCT[2:3, 2]
IMCT[2:3, 2:3]
dim(IMCT) # tamano del dataframe
nrow(IMCT) # numero de filas
ncol(IMCT) # numero de columnas
dimnames(IMCT) #nombre de filas y columnas
colnames(IMCT) #nombre de columnas
rownames(IMCT) # nombre de filas


# aumentar una variable a dataframe
data.frame(IMCT, IMCC = IMCT$poidsT/IMCT$tailleT^2) 
data.frame(IMCT, IMCC = with(IMCT, poidsT/tailleT^2))

attach(IMCT) # acceder directamente a la variable imct
IMCC = poidsT/tailleT^2
IMCC
IMCT = data.frame(IMCT, IMCC)
IMCT
detach(2)







