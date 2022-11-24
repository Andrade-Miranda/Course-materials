##### ###############################################################

####TABLAS UNIDIMENSIONALES

x=c(3,2,5,1,3,1,5,6,2,2,2,1,3,5,2)# ingresar un vector cualquiera
table(x)# calcula frecuencia absoluta
table(x)[4]# accedo a la cuarta entrada o cuarto nivel del vector x
sum(table(x))#sumo todos los elementos
prop.table(table(x))#frecuencias relativas
cumsum(table(x))# suma acumulativa

####################### TABLAS BIDIMENSIONALES

Respuestas = c("No","No","Si","No","Si","No","No","Si")# primer vector con datos de respuestas
Sexo= c("M","M","M","H","H","H","H","H")# segundo vector con datos de respuestas
table(Respuestas,Sexo)#creo tabla bidimensional
table(Respuestas,Sexo)[1,2]#accedo al valor de la primera fila segunda columna
table(Respuestas,Sexo)["No",] # busco cuantas personas respondieron No
table(Respuestas,Sexo)["No","M"] # busco cuantas respuesta No de mujeres
table(Respuestas,Sexo)["Si","H"] # busco cuantos respuesta si en hombres
prop.table(table(Respuestas,Sexo))#frecuencias relativas globales

####################### TABLAS MULTIDIMENSIONALES
Respuesta = c("No","No","Si","No","Si","No","No","Si") # VECTOR RESPUESTA
Sexo= c("M","M","M","H","H","H","H","H") #VECTOR SEXO
Pais= c("Fra","Ale","Ita","Ita","Ita","Ita","Ale","Fra") #VECTOR PAIS
table(Respuesta,Sexo,Pais)#creo tabla multidimensional, donde las respuesta y sexo se tabulan por pais
ftable(Respuesta,Sexo,Pais, col.vars = c("Sexo","Respuesta"))#ftable permite escoger el formato de presentacion de la tabla, 
#en este caso sexo y respuesta se presentan como columnas
table(Respuesta,Sexo,Pais)["Si","H","Ita"]#respondieron Si hombres italianos
table(Respuesta,Sexo,Pais)[,"H","Ale"]#que respondieron los hombres alemanes
table(Respuesta,Sexo,Pais)[,,"Ita"]#que respondieron las personas italianas

prop.table(table(Respuesta,Sexo,Pais))#frecuencias relativas
prop.table(ftable(Respuesta,Sexo,Pais))#frecuencias relativas tabuladas con ftable



#######Diagrama de barras##########
Sexo_Ger=c("Mujer","Mujer","Hombre","Mujer","Mujer","Mujer",
           "Mujer","Mujer","Hombre","Mujer","Hombre","Hombre","Mujer",
           "Mujer","Hombre","Mujer","Mujer","Mujer","Mujer","Hombre")

barplot(table(Sexo_Ger),col=c("lightblue","pink"),
        main="Diagrama de barras de las frecuencias absolutas de la variable\"Sexo_Ger\"")
# diagrama de barras de las frecuencias absolutas

barplot(prop.table(table(Sexo_Ger)),col=c("lightblue","pink"),
        main="Diagrama de barras de las frecuencias relativas de la variable\"Sexo_Ger\"")
# diagrama de barras de las frecuencias relativas


### otro ejemplo con datos multidimensionales
Respuestas = c("No","No","Si","No","Si","No","No","Si")
Sexo= c("M","M","M","H","H","H","H","H")
table(Respuestas,Sexo)
barplot(table(Sexo,Respuestas))# superpuesta las graficas de barras
barplot(table(Sexo,Respuestas),beside=TRUE)# gráficas de barras colocadas una a lado de la otra


#####################Diagrama circular

x=c(3,2,5,1,3,1,5,6,2,2,2,1,3,5,2)
pie(table(x),main="Diagrama circular de la variable \"x\"")#Grafica circular o pastel

#grafico de mosaico
Respuestas = c("No","No","Si","No","Si","No","No","Si")
Sexo= c("M","M","M","H","H","H","H","H")
table(Respuestas,Sexo)
plot(table(Sexo,Respuestas),main="Gráfico de mosaico de las variables\"Sexo\" 
     y \"Respuestas\"")


##################cargar datos de excel #####
#cargar datos a partir de una hoja de excel en la option import dataset
table(calificacion$notas)#frecuencias absolutas de la columna notas del archivo calificaciones
prop.table(table(calificacion$notas))#frecuencias relativas de la columna notas del archivo calificaciones


#########cargar datos de internet#########
datapersonas=read.table("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/chol.txt?tap_a=5644-dce66f&tap_s=10907-287229")










