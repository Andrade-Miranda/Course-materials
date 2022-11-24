



####Resolución tarea####
############################## Binomial##########################
#La probabilidad de que cierto tipo de objeto no pase una determinada
#prueba es 5/6. Se prueban 10 de tales objetos. Si X es la variable aleatoria que se
#define como el n??mero de objetos que no pasan la prueba:

#cual es la probabilidad de que 5 elementos no pasen la prueba P[X=5]
dbinom(x=5, size=10, prob=5/6)
visualize.binom(stat = 5, size = 10, prob =5/6)


#cual es la probabilidad de que mas de 5 y menos de 8 pasen la prueba
sum(dbinom(x=6:7, size=10, prob=5/6))

#cual es la probabilidad de que menos de 4 pasen la prueba
pbinom(q=4, size=10, prob=5/6)
sum(dbinom(x=0:4, size=10, prob=5/6))


#cual es la probabilidad de que mas de 4 objetos 
1-pbinom(q=4, size=10, prob=5/6,lower.tail = TRUE)

############################## Poisson##########################
#Una empresa textil produce un tipo de tela. El n??mero
#de defectos que se encuentra al desenrollar la tela es una variable aleatoria de
#Poisson que tiene en promedio 4 defectos por cada 20 metros de tela.


#a) ??Qu?? probabilidad hay de que al desenrollar la tela se encuentre menos de tres
#defectos en los 20 metros?.
ppois(3,lambda=4)

#b) ??Qu?? probabilidad hay de que al desenrollar la tela se encuentre menos de 2
#defectos en los 20 metros?.








############################## Uniforme ##########################
#La Southwest Arizona State University proporciona servicio de transporte de autob??s a los
#estudiantes mientras se encuentran en el recinto. Un autob??s llega a la parada de North Main
#Street y College Drive cada 30 minutos, entre las 6 de la ma??ana y las 11 de la noche entre
#semana. Los estudiantes llegan a la parada en tiempos aleatorios. El tiempo que espera un
#estudiante tiene una distribuci??n uniforme de 0 a 30 minutos.

a=0
b=30

#1. Trace una gr??fica de la distribuci??n.

#2. ??Cu??nto tiempo esperar?? el autob??s ???normalmente??? un estudiante? En otras palabras,
#??cu??l es la media del tiempo de espera? ??Cu??l es la desviaci??n est??ndar de los tiempos
#de espera?

#3. ??Cu??l es la probabilidad de que un estudiante espere m??s de 25 minutos?
1-punif(25, a,b)
#4. ??Cu??l es la probabilidad de que un estudiante espere entre 10 y 20 minutos?
punif(20, a,b)-punif(10, a,b)



################Normal###################################################################
#De acuerdo con el Internal Revenue Service (IRS) el reembolso medio de impuestos en 2007 fue
#de $2 708. Suponga que la desviaci??n est??ndar es de $650 y que las sumas devueltas tienen una
#distribuci??n normal.
#a) ??Qu?? porcentajes de reembolsos son superiores a $3 000?
visualize.norm(stat=3000, mu=2708, sd =650, section ="upper")
# p(x<=3000)
pnorm(3000,2708,650)
#p(x>3000)
1-pnorm(3000,2708,650)
pnorm(3000,2708,650)



#b) ??Qu?? porcentajes de reembolsos son superiores a $3 000 e inferiores a $3 500?
visualize.norm(stat =c(3000,3500), mu =2708 , sd =650, section ="bounded")

pnorm(3500,2708,650)-pnorm(3000,2708,650)



#c) ??Qu?? porcentajes de reembolsos son superiores a $2500 e inferiores a $3500?
visualize.norm(stat =c(2500,3500), mu =2708 , sd =650, section ="bounded")




