#El teorema del limite central es un fenomeno verdaderamente fascinante e 
#intrigante de la estadistica ya que al obtener muestras de cualquier distribucion 
#podemos crear una distribucion de medias muestrales que es normal o al menos 
#aproximadamente 
#normal. 

######################Simulacion con digitos aleatorios ##################################
#Con frecuencia las computadoras se utilizan para generar digitos aleatorios de numeros telefonicos
#para realizar encuestas. (Por ejemplo, el Pew Research Center genera aleatoriamente
#los ultimos dos digitos de numeros telefonicos para evitar un ("sesgo de
#lista"). Los digitos 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 se generan de forma que todos son
#igualmente probables.

# la poblacion sera 500000 numeros generados aleatoriamente
sizPo=5000000; #tamano de la poblacion

Data_Poblacion=floor(runif(sizPo, min=0, max=10))#la distribucion de los numeros aleatorios es casi uniforme
#porque todos los valores tienen la misma probabilidad de suceder

po.avg=mean(Data_Poblacion)#media de la poblacion
po.sd=sd(Data_Poblacion)#desviacion estandar de la poblacion
barplot(table(Data_Poblacion),col=c("lightblue"),
        main="Frecuencia de x")

#############muestreo de toda la poblacion#############################
n = 100; #cantidad de datos en la muestra
rows=sizPo/n   #cantidad de ensayos o muestreos realizados
m=matrix(Data_Poblacion,rows)#poner todo los ensayos en una matriz donde las filas representan los muestreos
sample.means=rowMeans(m)#media de cada muestreo

#sm.avg=po.avg  la media de las medias muestrales es igual a la media de la poblacion
sm.avg=mean(sample.means)#media de la distribucion de medias muestrales
sm.sd.clt=po.sd/sqrt(n)# Desviacion estandar de las muestras
hist(sample.means)#histograma de las medias muestrales

#Dibujo la normal sobre el histograma
range =seq(sm.avg-(5*sm.sd.clt),sm.avg+(5*sm.sd.clt),0.001)#creo rango utilizando media y desviacion

# n = 100; con 100 muestras
n = 100
sm.sd.clt=po.sd/sqrt(n)
y= dnorm(range,sm.avg,sm.sd.clt) #calculo la normal
par(new='true')
plot(range,y,main=, type='l',col="blue",ylim=c(0,max(y)+0.01),axes=FALSE,ylab='',xlab='')


# n = 30; con 30 muestras
n = 30
sm.sd.clt=po.sd/sqrt(n)
rows=sizPo/n   #cantidad de ensayos o muestreos realizados
m=matrix(Data_Poblacion,rows)#poner todo los ensayos en una matriz donde las filas representan los muestreos
sample.means=rowMeans(m)#media de cada muestreo
hist(sample.means)#histograma de las medias muestrales
range =seq(sm.avg-(5*sm.sd.clt),sm.avg+(5*sm.sd.clt),0.001)#creo rango utilizando media y desviacion
y1= dnorm(range,sm.avg,sm.sd.clt) #calculo la normal
par(new='true')
plot(range,y1,main=, type='l',col="red",ylim=c(0,max(y1)+0.01),axes=FALSE,ylab='',xlab='')



#EJERCICIO

#Los hombres suelen ser m??s pesados que las mujeres y los ni??os; por lo tanto, supongamos que al cargar un
#taxi acu??tico la situaci??n extrema es aquella en la que todos los pasajeros son hombres.
#En concordancia con los datos de la National Health and Nutrition Examination
#Survey, suponga que los pesos de los hombres se distribuyen normalmente,
#con una media de 172 libras y una desviaci??n est??ndar de 29 libras.
library("visualize") #uso la libreria visualize que facilita el c??lculo de z

mu=170
sigma=25
SizeMuestra=20

#a. Calcule la probabilidad de que, si se selecciona un hombre al azar, su peso
#sea mayor que 175 libras.
visualize.norm(stat =173, mu=mu, sd =sigma, section="upper")

#b. Calcule la probabilidad de que 20 hombres elegidos al azar tengan una media
#mayor que 175 libras (de manera que su peso total exceda la capacidad segura de 3500 libras).
smPeso.mean=mu
smPeso.sd= sigma/sqrt(SizeMuestra)#desviacion standar para muestra de 20 hombres

x =seq(smPeso.mean-4*sigma,smPeso.mean+4*sigma,0.01)#creo rango utilizando media y desviacion
a=dnorm(x,mu,sigma)#distribuci??n normal de toda la poblaci??n
b=dnorm(x,smPeso.mean,smPeso.sd)#distribuci??n normal de la muestra de 20

#Gr??fico la distribuci??n normal de toda la poblaci??n en rojo
plot(x,a, type="l", lwd=1, ylim=c(0,1.2*max(a,b)), ylab="a",col="Red")
segments(mu,0, mu, a[which(x==mu)], lwd=2, lty=2,col="red")#media poblacional
text(mu, a[which(x==smPeso.mean)], smPeso.mean, col="Red", pos=2)

#Gr??fico la distribuci??n normal de toda la muestra en azul
lines(x,b, type="l", lwd=1, col="blue")
segments(smPeso.mean,0, smPeso.mean, b[which(x==smPeso.mean)], lwd=2, lty=2, col="blue")
text(smPeso.mean, b[which(x==smPeso.mean)], smPeso.mean, col="blue", pos=2)

#calculo la probabilidad de que 20 hombres elegidos al azar tengan una media
#mayor que 175 libras con la nueva desviaci??n standar
visualize.norm(stat =173, mu=smPeso.mean, sd =smPeso.sd, section="upper")



#######Tarea############
#Resolver los siguientes enunciados usando R y la libreria visualize

#Uso del teorema del l??mite central.suponga que las estaturas de
#mujeres se distribuyen de manera normal, con una media de 63.6 pulgadas y una
#desviaci??n est??ndar de 2.5 pulgadas (seg??n datos de la National Health Survey).
mu=63.9
sigma=2.5



#a.Si se selecciona a una mujer al azar, calcule la probabilidad de que mida menos de 64 pulgadas
visualize.norm(stat =64, mu=mu, sd =sigma, section="lower")



#b.Si se seleccionan 36 mujeres al azar, calcule la probabilidad de que tengan una estatura
#media menor que 64 pulgadas
SizeMuestra=36
visualize.norm(stat =64, mu=mu, sd =sigma/(sqrt(SizeMuestra)), section="lower")

#c. Si se seleccionan 100 mujeres al azar, calcule la probabilidad de que tengan una estatura 
#media mayor que 63 pulgadas.
SizeMuestra=100
visualize.norm(stat =63, mu=mu, sd =sigma/(sqrt(SizeMuestra)), section="upper")



#d. Si se selecciona a una mujer al azar, calcule la probabilidad de que mida entre 63.5
#64.5 pulgadas.

visualize.norm(stat =c(63.5,64.5), mu=mu, sd =sigma, section="bounded")


#e Si se seleccionan 9 mujeres al azar, calcule la probabilidad de que tengan una estatura
#media entre 63.5 y 64.5 in.

SizeMuestra=9
pepito= sigma/sqrt(SizeMuestra)
visualize.norm(stat =c(63.5,64.5), mu=mu, sd =pepito, section="bounded")





