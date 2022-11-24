
############################## Binomial##########################

## Ejemplos de la moneda
## lanzo una moneda 15 veces. cuál es la probabilidad que salgan 5 caras
#P[X=5]
dbinom(x=5, size=15, prob=1/2) #Distribución  variable aleatoria 5, 15 lanzamientos y probabilidad de evento 0.5

#P[X=3] #Distribución normal variable aleatoria 3, 15 lanzamientos y probabilidad de evento 0.5
dbinom(x=3, size=15, prob=1/2)

#P[X<=3] # acumulada distribución acumulada, probabilidad de que sea 0,1,2,o 3 caras
# primera alternativa
dbinom(x=0:3, size=15, prob=1/2) 
sum(dbinom(x=0:3, size=15, prob=1/2))
#segunda alternativa
pbinom(q=3, size=15, prob=1/2, lower.tail = TRUE)

#Gráfico de una variable aleatoria binomial
x = 0:15 
pdf = dbinom(x,15, 1/2)
plot(x, pdf, type="h", lwd=3, col="blue",main="PDF of Binomial")
points(x,pdf,pch=16,cex=1,col="dark red")


#El 30% de un determinado pueblo ve un concurso que hay en televisión.
#Desde el concurso se llama por teléfono a 10 personas del pueblo elegidas al azar.
#Calcular la probabilidad de que, entre las 10 personas, estuvieran viendo el programa:
#a) Más de ocho personas
#b) Alguna de las diez personas
#c) Calcular la media y desviación típica

#binom(10,0.3)
#a) Más de ocho personas P[x>8]
sum(dbinom(x=9:10,size=10,prob=0.3))
pbinom(q=8, size=10, prob=0.3, lower.tail = FALSE)
#b) Algunas de las diez personas P[x>0]=1-P[x=~10]
sum(dbinom(x=1:10,size=10,prob=0.3))
1-dbinom(x=0,size=10,prob=0.3)
#c) Calcular la media y desviación típica
mb=10*0.3
sigmb=sqrt(10*0.3*0.7)


#Ejercicio 2.- El jefe de recursos humanos de una empresa realiza un test de diez ítems
#a los aspirantes a un puesto, teniendo en cada ítems cuatro posibles respuestas, de las
#que sólo una es correcta. Suponiendo que los aspirantes teniendo la misma probabilidad
#de responder. Se pide hallar las probabilidades para el aspirante:
#binom(10,1/4) X=contestar bien
#a) Conteste todos los ítems mal
dbinom(x=0,size=10,prob=1/4)

#b) Conteste al menos cuatro ítems bien p[x>=4]
pbinom(q=3, size=10, prob=1/4, lower.tail = FALSE)
sum(dbinom(x=4:10,size=10, prob=1/4))


#c) Conteste entre cuatro y seis ítems bien P[4<=X<=6]
sum(dbinom(x=4:6,size=10,prob=1/4))

#d) Conteste todos los ítems bien P[X=10]
dbinom(x=10,size=10,prob=1/4)

#e) Conteste menos de tres ítems bien P[x<3]
sum(dbinom(x=0:2,size=10,prob=1/4))



############################## Poisson##########################

#ejemplo
#Suponga X es el número de mensajes de textos que recibe una persona cualquiera por día
# en promedio ellos reciben 8 mensajes de textos por día. X se puede modelar como una
#distribución Poisson con lambda=8

#Que tan probable es que el individuo reciba 10 textos en un dia P[X=10]
dpois(x=10,lambda = 8)

#Que tan probable es que el individuo reciba 3 textos o menos en un dia P[X<=3]
ppois(q=3,lambda = 8) #P[x<=3] distribución acumulada

#Que tan probable es que el individuo reciba mas de un texto en un dia P[X>1]
#P[X>1]=1-P[X<=1]=1-(P[X=0]+P[X=1])
1-ppois(q=1,lambda = 8)

#Gráfico de una variable aleatoria
x = 0:16;  pdf = dpois(x, 8)
plot(x, pdf, type="h", lwd=3, col="blue",main="PDF of POIS(8)")
points(x,pdf,pch=16,cex=1,col="dark red")





################  DISTRIBUCION CONTINUA  ###################################

############################## Uniforme ##########################
#Un sistema genera un número aleatorio entre 351 y 358 para solucionar 
#un problema en particular, los valores generados tienen únicamente un valor decimal (0,01).
# a) Dibujar la distribución
# b) cual es la probabilidad de que el valor este dentro de 1 standard deviation de la media
# d) 35% de todos los valores seran mayor a cual valor??

a=351
b=358

# a) Grafico de la distribucion distribucion
range = seq(a,b,0.01) #se crea los valores en el eje de la x de la funcion entre a y b con un incremento de 0.01
y =dunif(range,a,b) # se crea  la distribucion uniforme

#codigo para graficar la distribucion uniforme 
plot(range, y, type='l', ylim=c(0,max(y)+0.1))
cord.a = c(a,seq(a,b,0.01),b)
cord.b = c(0,dunif(seq(a,b,0.01),a,b),0)
polygon(cord.a, cord.b, col="grey")

#b) valores dentro de un standar deviation
E.X=(a+b)/2#calculo de la media o valor esperado de la distribuci????n uniforme
SD.X=sqrt((b-a)^2/12)#calculo de la desviacion estandar
punif(E.X+SD.X, a,b) - punif(E.X-SD.X,a,b)#calculo del valor dentro de una desviacion estandar

SD_M=E.X+SD.X
SD_L=E.X-SD.X
#grafico de la probabilidad de estar entre una desviacion estandar sobre toda la distribucion
plot(range, y, type='l', ylim=c(0,max(y)+0.1))
cord.a = c(a,seq(a,b,0.01),b)
cord.b = c(0,dunif(seq(a,b,0.01),a,b),0)
polygon(cord.a, cord.b, col="grey")
# Porci??n que pertenece a una desviaci??n estandar se gr??fica en azul
cord.a = c(SD_L,seq(SD_L,SD_M,0.01),SD_M)
cord.b = c(0,dunif(seq(SD_L,SD_M,0.01),a,b),0)
polygon(cord.a, cord.b, col="blue")

#c)  35%
# 65th percentile
qunif(0.65,a,b) # cuartiles



############################## Normal ##########################
mu =2 #media
sigma =0.6 #variación estandar
x = 1.5 # variable aleatoria x

#dibujar la distribuci??n normal
range =seq(mu-4*sigma,mu+4*sigma,0.01)
y= dnorm(range,mu,sigma)
plot(range,y,main=, type='l',ylim=c(0,max(y)+0.01), axes=TRUE)

# P(X<=x) area a la izquierda de x
pnorm(x,mu,sigma)# probabilidad P(X<=x)
#grafico normal y sombreo en azul P(X<=x)
range =seq(mu-4*sigma,mu+4*sigma,0.01)
y= dnorm(range,mu,sigma)
plot(range,y,main=, type='l',ylim=c(0,max(y)+0.01), axes=FALSE)
axis(1,at=seq(mu-3*sigma,mu+3*sigma,sigma))
cord.a =c(0,seq(min(range),x,0.01),x)
cord.b =c(0,dnorm(seq(min(range),x,0.01),mu,sigma),0)
polygon(cord.a,cord.b, col="blue")

# P(X>x) area a la derecha de x
1-pnorm(x,mu,sigma)# probabilidad P(X>x)
#grafico normal y sombreo en rojo P(X>x)
range =seq(mu-4*sigma,mu+4*sigma,0.01)
y= dnorm(range,mu,sigma)
plot(range,y,main=, type='l',ylim=c(0,max(y)+0.01), axes=FALSE)
axis(1,at=seq(mu-3*sigma,mu+3*sigma,sigma))
cord.c =c(x,seq(x,max(range),0.01),0)
cord.d =c(0,dnorm(seq(x,max(range),0.01),mu,sigma),0)
polygon(cord.c,cord.d, col="red")

# P(1.5<X<3) 
pnorm(3,mu,sigma) - pnorm(1.5,mu,sigma)


# 90th percentile
qnorm(0.9,mu,sigma)

#instalación de un paquete que permite visualizar de mejor manera
#las distribuciones de probabilidad de variables aleatorias
install.packages("visualize")# instalacion del paquete solo una vez

library("visualize")#carga de la libreria

#Ejemplos
#Los ingresos semanales de los supervisores de turno de la industria del vidrio se rigen por una
#distribución de probabilidad normal con una media de $1000 y una desviación estándar de
#$100. 

#?Cuál es la probabilidad de seleccionar a un supervisor cuyo ingreso semanal 
#sea menor que $1 100? 
visualize.norm(stat=1100, mu=1000, sd =100, section ="lower")
#Cuál es la probabilidad de seleccionar a un supervisor cuyo ingreso semanal 
#oscile entre $1 000 y $1 100? 
visualize.norm(stat =c(1000,1100), mu =1000 , sd =100, section ="bounded")
#Cuál es la probabilidad de seleccionar a un supervisor cuyo ingreso semanal 
#sea mayor que $1 100? 
visualize.norm(stat =1100, mu=1000, sd =100, section="upper")


x=seq(0, 1, by=0.01) # secuencia
integrand = function(x) {1.25*(1-x^4)}
integrate(integrand, lower = 0, upper = 1)



