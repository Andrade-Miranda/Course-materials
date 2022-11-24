x=c(3,2,5,1,3,1,5,6,2,2,2,1,3,5,2)# ingresar un vector cualquiera
table(x)# calcula frecuencia absoluta
names(table(x))
table(x)[4]#me refiero a la cuarta entrada o cuarto nivel
table(x)["3"]# me refiero a la frecuencia absoluta del nivel 3
sum(table(x))
prop.table(table(x))#frecuencias relativas

####################### tablas Bidemensionales

Respuestas = c("No","No","Si","No","Si","No","No","Si")
Sexo= c("M","M","M","H","H","H","H","H")
table(Respuestas,Sexo)
table(Respuestas,Sexo)[1,2]#accedo a valor 1,2
table(Respuestas,Sexo)["No",] # busco cuantas mujeres respondieron No
prop.table(table(Respuestas,Sexo))#frecuencias relativas globales
prop.table(table(Respuestas,Sexo),margin=1)#frecuencia relativa marginales por respuesta
prop.table(table(Respuestas,Sexo),margin=2)#frecuencia relativa marginales por sexo

####################### tablas multidimensionales
Respuesta = c("No","No","Si","No","Si","No","No","Si")
Sexo= c("M","M","M","H","H","H","H","H")
Pais= c("Fra","Ale","Ita","Ita","Ita","Ita","Ale","Fra")
table(Respuesta,Sexo,Pais)
ftable(Respuesta,Sexo,Pais, col.vars = c("Sexo","Respuesta"))#muestra en un formato plano, que variable quiero como columna
table(Respuesta,Sexo,Pais)["Si","H","Ita"]#respondieron que si son hombres italianos
table(Respuesta,Sexo,Pais)[,"H","Ale"]#hombres alemanes
table(Respuesta,Sexo,Pais)[,,"Ita"]

prop.table(table(Respuesta,Sexo,Pais))#frecuencias relativas
prop.table(ftable(Respuesta,Sexo,Pais))
prop.table(table(Respuesta,Sexo,Pais),margin=3)#frecuencias relativas por pais
prop.table(table(Respuesta,Sexo,Pais),margin=c(1,3))#frecuencias relativas por pais



###############cargar datos de una URL
Beb_Energ=read.table("http://aprender.uib.es/Rdir/bebenerg.txt",header=TRUE,encoding="UTF-8")
head(Beb_Energ)## beben bebidas energiticas
summary(Beb_Energ)#resumen de la informacion
sapply(Beb_Energ,FUN=table)# en forma de tabla de frecuencia absoluta de cada variable
table(Beb_Energ)
ftable(Beb_Energ)


#######Diagrama de barras##########
Sexo_Ger=c("Mujer","Mujer","Hombre","Mujer","Mujer","Mujer",
           "Mujer","Mujer","Hombre","Mujer","Hombre","Hombre","Mujer",
           "Mujer","Hombre","Mujer","Mujer","Mujer","Mujer","Hombre")

barplot(table(Sexo_Ger),col=c("lightblue","pink"),
main="Diagrama de barras de las frecuencias absolutas de la variable\"Sexo_Ger\"")

barplot(prop.table(table(Sexo_Ger)),col=c("lightblue","pink"),
main="Diagrama de barras de las frecuencias relativas de la variable\"Sexo_Ger\"")
           

Respuestas = c("No","No","Si","No","Si","No","No","Si")
Sexo= c("M","M","M","H","H","H","H","H")
table(Respuestas,Sexo)

barplot(table(Sexo,Respuestas))# superpuesta las graficas
barplot(table(Sexo,Respuestas),beside=TRUE)


#####################Diagrama circular

x=c(3,2,5,1,3,1,5,6,2,2,2,1,3,5,2)
pie(table(x),main="Diagrama circular de la variable \"x\"")#Grafica circular

#grafico de mosaico
Respuestas = c("No","No","Si","No","Si","No","No","Si")
Sexo= c("M","M","M","H","H","H","H","H")
table(Respuestas,Sexo)
plot(table(Sexo,Respuestas),main="Gráfico de mosaico de las variables\"Sexo\" 
           y \"Respuestas\"")

################
HairEyeColor
HEC=as.table((apply(HairEyeColor,MARGIN=c(1,2),FUN=sum)))
#tabla bidimensional 
dimnames(HEC)
dimnames(HEC)=list(Cabello=c("Negro","Castaño","Rojo","Rubio"),
                   Ojos=c("Marrones","Azules","Pardos","Verdes"))
plot(HEC,col=c("lightblue"),main="Diagrama de mosaico de la tabla bidimensional de 
     frecuencias \n de colores de cabellos y ojos")

sum(HEC) #numero total de personas
colSums(HEC) #color de ojos
rowSums(HEC) #color de cabello

barplot(prop.table(colSums(HEC)),col=c("lightblue","pink"),
        main="Diagrama de barras de las frecuencias relativas de la variable\"Sexo_Ger\"")





##################cargar datos de excel #####
#cargar datos de excel
table(calificacion$notas)
prop.table(table(calificacion$notas))


#########cargar datos de internet#########
datapersonas=read.table("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/chol.txt?tap_a=5644-dce66f&tap_s=10907-287229")
edad=datapersonas$V1[2:length(datapersonas$V1)]


###### otro Ejemplo
mym=c("cafe","rojo","amarillo","cafe","anaranjado","amarillo","verde","rojo","anaranjado","azul","azul","cafe","verde","verde","azul","cafe","azul","cafe","azul","cafe","anaranjado")
table(mym)
prop.table(table(mym))
prop.table(table(mym))*100


#completar el codigo
####### Datos Cuestionario##################
Pr1 = c("No","No","Si","No","Si","No","No","Si")# primer vector con datos de respuestas
Pr2 = c("Si","No","No","No","Si","Si","No","Si")# segundo vector con datos de respuestas
Pr3 = c("No","Si","No","Si","Si","Si","No","Si")# tercer vector con datos de respuestas
Sexo= c("M","M","M","H","H","M","H","H")# segundo vector con datos de respuestas
Facultad=c("FII","FCM","FCM","FII","FCM","FII","FCM","FII")


## Escribir la table de frecuencias absoluta multidimensional del cuestionario
## colocando los vectores  facultad y sexo como columnas

ftable(Pr1,Pr2,Pr3,Sexo,Facultad, col.vars = c("Facultad","Sexo")) 

## Escribir la table de frecuencias relativas multidimensional del cuestionario
## colocando los vectores  facultad y sexo como columnas
prop.table(ftable(Pr1,Pr2,Pr3,Sexo,Facultad, col.vars = c("Facultad","Sexo"))) 

## cuantas mujeres de FII respondieron No a la Pr1, Si a la Pr2 y No a la Pr3
table(Pr1,Pr2,Pr3,Sexo,Facultad)["No","Si","No","M","FII"]


## cuantos mujeres de FCM respondieron Si a Pr1 y "No" a la Pr2
table(Pr1,Pr2,Pr3,Sexo,Facultad)["Si","No",,"M","FCM"]

## cuantas Hombres de FCM respondieron No a las tres preguntas
table(Pr1,Pr2,Pr3,Sexo,Facultad)["No","No","No","H","FCM"]

# Dibuje el diagrama de barra de frecuencias absolutas de la primera pregunta
barplot(table(Pr1),col=c("blue","Red"), main= "Pregunta 1")

# Dibuje el diagrama de barra de frecuencias absolutas de la segunda pregunta
barplot(table(Pr2),col=c("blue","Red"), main= "Pregunta 2")

# Dibuje el diagrama de barra de frecuencias absolutas de la tercera pregunta
barplot(table(Pr3),col=c("blue","Red"), main= "Pregunta 3")







