## tablas de frecuencia


# leer un data frame via un fichero
data_imcenf <-read.table("http://www.biostatisticien.eu/springeR/imcenfant.txt",header=TRUE)
head(data_imcenf)


#Plot in R
#######################################################################
# Ejemplo en R para importar datos desde excel y calcular los valores de
# las frecuencias absolutas, relativas, acumulada, media
#########################################################################

table(x) # crea la tabla frecuencias absoluta
prop.table(table(x)) #crea la tabla frecuencias relativa
cumsum(table(x))  #crea la tabla de frecuencias acumuladas
mean(x) # media
length(x) #longuitud de la variable x
sort(x) #ordenar los datos

#histograma de frecuencias absolutas
h=hist(x, main=" ",xlab="x",    
       ylab="frecuencias",border="blue",
       xlim= c(0,10),right = F,
       col="green")
par(new=TRUE)
#Poligonos de frecuencias absolutas
lines(h$mids, h$counts, type = "b", pch = 20, col = "red", lwd = 3)

################################################################################
#forma alternativa para calcular las frecuencias y medidas de tendencia central 
# incluyendo todo en un solo data frame*
# *data frame es un tipo especial de datos en R en el cuál los datos se escriben 
# en columnas usando la libreria plyr
################################################################################
x=calificacion$notas

#install.packages("plyr")
library(plyr)

y=count(x)
barplot(y$freq,names.arg=y$x, main = "Tabla de Frecuencias de notas",
        col = c("Red","Blue","Green","Yellow","Black","Purple"))
n=sum(y$freq)
rf=y$freq/n
rf=rf*100

y$freq_rela=rf
freq_acumu=cumsum(y$freq)
y$freq_acumu=freq_acumu







