x=c(169,167,164,164,164,163,168,170,171,168,166,168,162,168,
    172,168,169,167,168,164,167,168,171,169,173,166,169,167,
    173,169,169,168,170,161,164,164,168,164,167,164)

hist(x)
hist(x,'Scott')
hist(x,'FD')
?c
?hist

mean(x)#media
median(x)#mediana
var(x)# varianza
sd(x)# desviacion standar
length(x)#tamano muestra
min(x) 
max(x)
range(x)
quantile(x)# cuantiles tipo 7 (forma de calculo)
quantile(x,type=6) #cuantiles tipo 6 (forma de calculo)
quantile(x,probs = (1:2)/3) #terciles
quantile(x,probs = (1:9)/10) #deciles

#binomial
#P(x=3)
dbinom(3,10,0.4)
?dbinom

#P(x<=3)
pbinom(3,10,0.4)

#P(x>3)
pbinom(3,10,0.4,lower.tail = FALSE)

#Simulacion de muestra aleatoria de 20 observaciones de 
rbinom(20,10,0.4)

?distribution
pbirthday(80)

#por ejemplo la probabilidad de tener que lanzar una moneda 3 veces para 
#observar la primera cara
dgeom(2,0.5)#numero de fracasos es en R


##prueba de bondad de ajuste
#la prueba de Kolmogorv - smirnov solo es valida para distribuciones continuas
# la prueba de chapiro-wilk solo sirve para verificar lnormalidad de las observaciones.
ks.test(x,pnorm,mean =mean(x), sd=sd(x))# Kolmogorv - smirnov normalidad
shapiro.test(x)





