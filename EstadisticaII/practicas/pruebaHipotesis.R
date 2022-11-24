#prueba de hipotesis


#Lanzamiento de moneda 10 veces
# H0-> theta=0.5
# H1-> theta=0.6


## significancia y poder
x=0:10
PMF_H0=dbinom(x, size=10, prob=1/2) #hipotesis nula

#Gráfico de una variable aleatoria binomial
plot(x, PMF_H0, type="h", lwd=3, col="blue",main="PDF of Binomial")
points(x,PMF_H0,pch=16,cex=1,col="dark red")

PMF_H1=dbinom(x, size=10, prob=0.6) #hipotesis alternativa H1=0.6
#Gráfico de una variable aleatoria binomial
plot(x, PMF_H1, type="h", lwd=3, col="blue",main="PDF of Binomial")
points(x,PMF_H1,pch=16,cex=1,col="dark red")


PMF_H1=dbinom(x, size=10, prob=0.7) #hipotesis alternativa H1=0.7
plot(x, PMF_H1, type="h", lwd=3, col="blue",main="PDF of Binomial")
points(x,PMF_H1,pch=16,cex=1,col="dark red")




library(pwr)
pwr.t.test(n=NULL,d=.5,sig.level=0.05,power=.8, type="two.sample",alternative="two.sided")



#critical values 95%
#one side right
x_0.05=qnorm(0.95,100,15) # n(100,15^2)
library("visualize")
visualize.norm(stat =x_0.05, mu=100, sd =15, section="upper")


##one side left
x_0.95=qnorm(0.05,100,15) # n(100,15^2)
library("visualize")
visualize.norm(stat =x_0.95, mu=100, sd =15, section="lower")

##two side 
#x_0.975=q_0.025
#x_0.025=q_0.975
x_0.975=qnorm(0.025,100,15) 
x_0.025=qnorm(0.975,100,15) 
library("visualize")
visualize.norm(stat =c(x_0.975,x_0.025), mu=100, sd =15, section="bounded")




#Example 1. A company that manufactures light bulbs claims that a particular 
#type of light bulb will last 850 hours on average with standard deviation of 50.
#A consumer protection group thinks that the manufacturer has overestimated the 
#lifespan of their light bulbs by about 40 hours. How many light bulbs does the 
#consumer protection group have to test in order to prove their point with 
#reasonable confidence?
#H0=> mu=850
#H1=> mu=810
#alpha= 0.05
#power=0.90

library(pwr)
pwr.t.test(d=(850-810)/50,power=0.9,sig.level=0.05,type="one.sample",alternative="two.sided")


####################EJERCICIOS RESUELTOS CON R###########################################


#Control de calidad de los dulces M&M El conjunto de
#datos 13 incluye los pesos de 13 dulces M&M rojos, elegidos al
#azar de una bolsa que contiene 465 M&M. A continuación se presentan los pesos
#(en gramos), los cuales tienen una media de 0.8635 y una desviacion
#estandar de s=0.0576 g. 
# 0.751,0.841,0.856,0.799,0.966,0.859,0.857,0.942,0.873,0.809,0.890,0.878,0.905
#En el empaque se afirma que el peso neto del contenido
#es 396.9 g, de manera que los M&M deben tener un peso medio de al menos
#396.9/465=0.8535 g para dar la cantidad anunciada. Utilice los datos
#muestrales con un nivel de significancia de 0.05, para probar la aseveraci??n
#que hizo un gerente de producci??n de que los M&M tienen en realidad una media
#mayor que 0.8535 g, de manera que los consumidores est??n recibiendo m??s
#que la cantidad indicada en la etiqueta.

x=c(0.751,0.841,0.856,0.799,0.966,0.859,0.857,0.942,0.873,0.809,0.890,0.878,0.905)
t.test(x, alternative ="greater", mu=0.8535,conf.level = 0.95)
# t.test cuando el estadistico de prueba es con respecto a la media
#no rechazo hipotesis nula -  p-value = 0.2707



#Una encuesta de n=703
#empleados seleccionados al azar, revelo que el 61% de ellos consiguio
#trabajo por medio de una red de contactos. Calcule el valor del estadistico de
#prueba para la aseveracion de que la mayoria de los empleados (mas del 50%)
#consiguen trabajo por medio de una red de contactos. Calcule el valor de p? y decida si
#se rechaza o no la hipotesis nula

# hay dos formas de resolver este problema
# primera forma
# Haciendo los cálculos paso por paso
library("visualize")

n=703 #numero de muestras
p_sombrero=0.61 #61% de ellos consiguio trabajo por medio de una red de contactos
p=0.5 #hipotesis nula
q=0.5

mu=p #media
sigma=sqrt((p*q)/n) #desviacion standar
x =seq(mu-5*sigma,mu+5*sigma,0.01)
z = (p_sombrero-p)/sqrt((p*q)/n)#calculo del estadistico de prueba
#calculo de p utilizando la distribucion normal
visualize.norm(stat =p_sombrero, mu=mu, sd =sigma, section="upper")

# segunda forma
#calculo de p utilizando funcion prop.test para proporciones
# 703*0.61-numero de sucesos
# 703 - numero de muestras
# alt="greater" - hipotesis alternativa
# p=0.5 - hipotesis nula

prop.test(703*0.61, 703, alt="greater",p=0.5, correct=FALSE) 
# Resultado de prop.test(703*0.61, 703, alt="greater",p=0.5, correct=FALSE)

#data:  703 * 0.61 out of 703, null probability 0.5
#X-squared = 34.025, df = 1, p-value = 2.72e-09
#alternative hypothesis: true p is greater than 0.5
#95 percent confidence interval:
#0.5793749 1.0000000
#sample estimates:
#p 
#0.61

#X-squared = 34.025 es igual a z al cuadrado, z=5.833 
#p-value = 2.72e-09, por ende se rechaza la hypotesis nula


#Experimentos gen??ticos de Mendel Cuando Gregor Mendel realiz??
#sus famosos experimentos de hibridaci??n con guisantes, uno de ellos dio por
#resultado descendencia que consist??a en 428 plantas de guisantes con vainas verdes
#y 152 plantas de guisantes con vainas amarillas. Seg??n la teor??a de Mendel,
#1/4 de los v??stagos de guisantes deb??an tener vainas amarillas. Utilice un nivel
#de significancia de 0.05, con el m??todo del valor P, para probar la aseveraci??n de
#que la proporci??n de v??stagos de guisantes con vainas amarillas es igual a 1/4

# 1era forma
prop.test(152, 580, alt="two.sided",p=0.25, correct=FALSE) 



#2da forma
n=580 #n??mero de muestras
p_sombrero=152/580 #61% de ellos consigui?? trabajo por medio de una red de contactos
p=0.25 #hipotesis nula
q=0.75

mu=p #media
sigma=sqrt((p*q)/n) #desviacion standar
x =seq(mu-5*sigma,mu+5*sigma,0.01)
z = (p_sombrero-p)/sqrt((p*q)/n)#calculo del estadistico de prueba
#calculo de p utilizando la distribucion normal
visualize.norm(stat =p_sombrero, mu=mu, sd =sigma, section="upper")
pValue=(1-pnorm(p_sombrero,mu,sigma))*2# calculo mayor que p_sombrero y multiplico x2 por ser dos colas


#Estaturas de supermodelos. Se midio la estatura de las supermodelos Niki Taylor,
#Nadia Avermann, Claudia Schiffer, Elle MacPherson, Christy Turlington, Bridget
#Hall, Kate Moss, Valeria Mazza y Kristy Hume. Ellas tienen una media de 70.2 in y
#una desviacion estandar de 1.5 in. Utilice un nivel de significancia de 0.01 para probar
#la aseveraci??n de que las supermodelos tienen estaturas con una media que es mayor
#a la media de 63.6 in de las mujeres en la poblacion general. Dado que solo contamos
#con nueve estaturas, ??realmente podemos concluir que las supermodelos son mas altas
#que la mujer tipica?

modelosData=rnorm(9,mean = 70.2, sd = 1.5)

t.test(modelosData, alternative ="greater", mu=63.6,conf.level = 0.99)
#rechazo hipotesis nula, Existe evidencia suficiente
#para sustentar la aseveracion de que las supermodelos tienen una
#estatura media mayor que 63.6 pulgadas. Si, la evidencia es fuerte.


#Azucar en el cereal. Se seleccionaron al azar diferentes cereales y se obtuvo el
#contenido de az??car (gramos de az??car por gramo de cereal), con los siguientes
#resultados para Cheerios, Harmony, Smart Start, Cocoa Puffs, Lucky Charms, Corn
#Flakes, Fruit Loops, Wheaties, Cap??n Crunch, Frosted Flakes, Apple Jacks, Bran Flakes,
#Special K, Rice Krispies, Corn Pops y Trix. Utilice un nivel de significancia
#de 0.05 para probar la aseveraci??n de un cabildero de que la media de todos los
#cereales es menor que 0.3 g.
#0.03 0.24 0.30 0.47 0.43 0.07 0.47 0.13
#0.44 0.39 0.48 0.17 0.13 0.09 0.45 0.43

x=c(0.03,0.24,0.30,0.47,0.43,0.07,0.47,0.13,0.44,0.39,0.48,0.17,0.13,0.09,0.45,0.43)
t.test(x, alternative ="less", mu=0.3,conf.level=0.95) 


#El mam??fero m??s peque??o del mundo. El mam??fero m??s peque??o del mundo es el
#murci??lago abejorro, tambi??n conocido como murci??lago nariz de cochino (o Craseonycteris
#thonglongyai). Estos animales apenas alcanzan el tama??o de un abejorro
#grande. A continuaci??n se incluyen los pesos (en gramos) de una muestra de estos
#murci??lagos. Ponga a prueba la aseveraci??n de que estos murci??lagos provienen de la
#misma poblaci??n con un peso medio de 1.8 g.
#
x=c(1.7,1.6,1.5,2.0,2.3,1.6,1.6,1.8,1.5,1.7,2.2,1.4,1.6,1.6,1.6)
t.test(x, alternative ="two.sided", mu=1.8)


#Las piezas de grava se clasifican como pequeñas, medianas o grandes. Una distribuidora 
#afirma que al menos 10% de las piezas de grava de su planta son grandes. En una muestra 
#aleatoria de 1 600 piezas, 150 se clasificaron como grandes.¿Representa esto suficiente 
#evidencia para rechazar la afirmación?

prop.test(150,1600,alt="less",p=0.10, correct=FALSE)


#Una muestra de 18 piezas de material laminado tenía una media de deformación de 
#1.88 mm y una desviación estándar de 0.21 mm. ¿Se puede concluir que la media de la 
#deformación de este tipo de laminado es menor a 2 mm?
rnorm2=function(n,mean,sd) { mean+sd*scale(rnorm(n)) }
x=rnorm2(18,1.88,0.21)
t.test(x, alternative ="less", mu=2)


#Un fabricante de estaciones de trabajo de computadora está probando un nuevo proceso 
#de ensamble automatizado. El proceso actual tiene una tasa de defectos de 5%. En una 
#muestra de 400 estaciones de trabajo ensambladas con el nuevo proceso, 15 tenían defectos. 
#¿Se puede concluir que el nuevo proceso tiene una tasa menor de defectos?(TALLER)  nivel 
#de significancia 0.05

prop.test(15,400,alt="less",p=0.05, correct=FALSE)








########################tarea##################################################

# La tarea debe presentar la captura de pantalla obtenida luego de utilizar los comandos en R
# a su vez debe contener el análisis estadisitico del porque se rechaza o no la hipotesis nula


#Seleccion del genero para ninas. El Genetics and IVF Institute llevo a cabo un ensayo
#clinico del metodo XSORT, disenado para incrementar la probabilidad de concebir una
#nina. Mientras se escribia este libro, ya habian nacido 325 bebes de padres que utilizaron
#el metodo XSORT, y 295 de ellos fueron ninas. Utilice los datos muestrales con un nivel
#de significancia de 0.01 para probar la aseveracion de que, con este metodo, la probabilidad
#de que un bebe sea nina es mayor que 0.5. Parece que el metodo funciona?

prop.test(295,325,alt="greater",p=0.5,conf.level = 0.99)



#Accidentes automovilisticos. En un estudio de 11,000 accidentes automovilisticos, se
#descubrio que 5720 de ellos ocurrieron a 5 millas de casa del conductor (segun datos de
#Progressive Insurance (compania de seguros)). Utilice un nivel de significancia de 0.01 para probar la aseveracion
#de que mas del 50% de los accidentes automovilisticos ocurren dentro de 5 millas de
#distancia de la casa del conductor. ??Los resultados son cuestionables porque se basan en
#una encuesta patrocinada por una compania de seguros???



#Tiempos de espera de clientes bancarios. Los valores listados son tiempos de espera
#(en minutos) de clientes del banco Jefferson Valley, donde los clientes se forman en
#una sola fila atendida por tres ventanillas. Ponga a prueba la aseveración de que la
#desviación estándar de los tiempos de espera es menor que 1.9 minutos, que es la desviación
#estándar de los tiempos de espera del mismo banco cuando se utilizan filas separadas
#para cada ventanilla. Utilice un nivel de significancia de 0.05. ¿Parece que el
#uso de una sola fila reduce la variación entre los tiempos de espera? ¿Cuál es una de
#las ventajas de reducir la variación entre los tiempos de espera?
#  6.5 6.6 6.7 6.8 7.1 7.3 7.4 7.7 7.7 7.7


install.packages('EnvStats')
library(EnvStats)

#use la funcion varTest
#ejemplo
#varTest(x, alternative = "two.sided", conf.level = 0.95, sigma.squared = 1, data.name = NULL)
# ayuda sobre la función: https://www.rdocumentation.org/packages/EnvStats/versions/2.3.1/topics/varTest


#Temperaturas corporales. Se toma una muestra de 106 temperaturas 
#corporales con una media de 98.20°F y una desviación estándar de 0.62°F.
#Utilice un nivel de significancia de 0.05 para probar la aseveración de que la temperatura
#media corporal es menor que 98.6°F. Con base en esos resultados, ¿parece que la
#media de 98.6°F que suele utilizarse es errónea?


#Tratamiento del síndrome de fatiga crónica. Se sometió a prueba a pacientes con
#síndrome de fatiga crónica, luego se les dio un tratamiento con fludrocortisona y después
#se sometieron a prueba nuevamente. Se utilizó una escala estándar de -7 a 	+7
#para medir la fatiga antes y después del tratamiento. Los cambios se resumen con los
#siguientes estadísticos: n=21, media=4 y s=2.17 (según datos de “The Relationship
#Between Neurally Mediated Hypotension and the Chronic Fatigue Syndrome” de
#BouHolaigah, Rowe, Kan y Calkins, Journal of the American Medical Association,
#vol. 274, núm. 12). Los cambios se calcularon de tal forma que los valores positivos
#representan mejorías. Utilice un nivel de significancia de 0.01 para probar la aseveración
#de que el cambio medio es positivo. ¿Parece ser efectivo el tratamiento?







