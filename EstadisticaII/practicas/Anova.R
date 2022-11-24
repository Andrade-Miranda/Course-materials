#ANOVA Analisis de varianza
detach("package:plyr", unload=TRUE)
library(dplyr)
install.packages("ggpubr")#para graficar box plots
library("ggpubr")


##################EJERCICIO 1##################################################
#Estamos interesados en conocer si hay colores mas atractivos para los insectos. 
#Para ello se disenaron trampas con los siguientes colores: amarillo, azul, blanco y verde. 
#Se cuantifica el numero de insectos que quedaban atrapados:
#Azul: 16 11 20 21 14 7
#Verde: 37 32 15 25 39 41
#Blanco: 21 12 14 17 13 17
#Amarillo: 45 59 48 46 38 47

insectos=c(16,11,20,21,14,7,37,32,15,25,39,41,21,12,14,17,13,17,45,59,48,46,38,47)
colores=as.factor(c(rep(c("azul", "verde", "blanco", "amarillo"), each =6)))
boxplot(insectos ~ colores, col = c("yellow", "blue", "white","green"), ylab = "N??mero de insectos atrapados")
tapply(insectos, colores, mean)#se especifica una funcion para realizar a los datos cell
fm = aov( lm(insectos ~ colores) )#prueba de anova
summary(fm)#Pedimos un resumen de la tabla del ANOVA
#df1 = k-1 and df2=N-k,
names(fm)#Elementos generados en el ANOVA
qf(0.05, 3, 20, lower.tail = F)



######################EJERCICIO 2 ##################
crecimiento=c(0.15,0.02,0.16,0.37,0.22,1.34,0.14,0.02,0.08,0.08,0.23,
              0.04,0.34,0.16,0.05,2.03,0.27,0.92,1.07,2.38)
tratamiento=as.factor(c(rep(c("ninguno", "Fertilizante", "Riego", 
                              "FertiliznteYriego"), each =5)))

Alamos=data.frame(crecimiento,tratamiento)
levels(Alamos$tratamiento)# muestra las diferentes tratamientos

group_by(Alamos, tratamiento) %>%
  summarise(
    count = n(),
    mean = mean(crecimiento, na.rm = TRUE),
    sd = sd(crecimiento, na.rm = TRUE)
  )

# grafico de caja
# ++++++++++++++++++++
# Plot crecimiento por tratamiento 
ggboxplot(Alamos, x = "tratamiento", y = "crecimiento", 
          color = "tratamiento", palette = c("#00AFBB", "#E7B800", "#FC4E07", "#17BE67"),
          order = c("ninguno", "Fertilizante", "Riego", "FertiliznteYriego"),
          ylab = "crecimiento", xlab = "tratamiento")

# Mean plots
# ++++++++++++++++++++
# Plot crecimiento por tratamiento
# anadir barras de error : mean_se
# (other values include: mean_sd, mean_ci, median_iqr, ....)
ggline(Alamos, x = "tratamiento", y = "crecimiento", 
       add = c("mean_se", "jitter"), 
       order = c("ninguno", "Fertilizante", "Riego", "FertiliznteYriego"),
       ylab = "crecimiento", xlab = "tratamiento")

# ANOVA
res.aov = aov(crecimiento ~ tratamiento, data = Alamos)
# resumen de ANOVA
summary(res.aov)
#como  p es menor que el valor de 0.05, podemos concluir que los valores son significantes 
#y rechazo la hipotesis nula
qf(0.05, 3, 16, lower.tail = F)



#En la prueba de un factor indica que si p es significatiovo alguna de las medias es diferente 
#pero no sabemos cual de ellas son diferentes

#pruebas de comparacion multiple
TukeyHSD(res.aov)#realizar comparaciones entre la media








###########################Ejercicio 3#######################################################
#Datos que contienen el tama??o de plantas que tienen distintos tipos de tratamiento 
my_data <- PlantGrowth
set.seed(1234)
dplyr::sample_n(my_data, 10)#toma aleatoriamente un grupo de observaciones a partir de los datos

levels(my_data$group)# muestra las diferentes categorias


#calcula un resumen de las estadisticas por categoria - Numeros de datos, 
#media, standar desviacion
group_by(my_data, group) %>%
  summarise(
    count = n(),
    mean = mean(weight, na.rm = TRUE),
    sd = sd(weight, na.rm = TRUE)
  )

install.packages("ggpubr")#para graficar box plots

# Box plots
# ++++++++++++++++++++
# Plot pesos por grupo y color y grupo
ggboxplot(my_data, x = "group", y = "weight", 
          color = "group", palette = c("#00AFBB", "#E7B800", "#FC4E07"),
          order = c("ctrl", "trt1", "trt2"),
          ylab = "Weight", xlab = "Treatment")

# Mean plots
# ++++++++++++++++++++
# Plot pesos por grupo
# anadir barras de error : mean_se
# (other values include: mean_sd, mean_ci, median_iqr, ....)
ggline(my_data, x = "group", y = "weight", 
       add = c("mean_se", "jitter"), 
       order = c("ctrl", "trt1", "trt2"),
       ylab = "Weight", xlab = "Treatment")

par(mfrow=c(2,2))
### QQplot
qqnorm(Alamos$crecimiento[Alamos$tratamiento=="ninguno"],main = "Ninguno")
qqline(Alamos$crecimiento[Alamos$tratamiento=="ninguno"])

qqnorm(Alamos$crecimiento[Alamos$tratamiento=="Fertilizante"],main = "Fertilizante")
qqline(Alamos$crecimiento[Alamos$tratamiento=="Fertilizante"])

qqnorm(Alamos$crecimiento[Alamos$tratamiento=="Riego"],main = "Riego")
qqline(Alamos$crecimiento[Alamos$tratamiento=="Riego"])

qqnorm(Alamos$crecimiento[Alamos$tratamiento=="FertiliznteYriego"],main = "Fertilizante y Riego")
qqline(Alamos$crecimiento[Alamos$tratamiento=="FertiliznteYriego"])


# ANOVA
res.aov = aov(weight ~ group, data = my_data)
# Summary of the analysis
summary(res.aov)
#como  p es menor que el valor de 0.05, podemos concluir que los valores son significantes 
#y rechazo la hipotesis nula


#Multiple pairwise-comparison between the means of groups
#In one-way ANOVA test, a significant p-value indicates that 
#some of the group means are different, but we don???t know which pairs 
#of groups are different.
#It???s possible to perform multiple pairwise-comparison, to determine if 
#the mean difference between specific pairs of group are statistically significant.

#The function TukeyHD() takes the fitted ANOVA as an argument.
TukeyHSD(res.aov)#para realizar comparaciones multiples entre los datos, y conocer 
#cual de ellos tienen diferencia significativa
#los resultados muestran que solamente la diferencia entre trt2 and trt1 
#es significativa con ajuste p-value of 0.012.

#para realizar la prueba de anova se asumen ciertas condiciones que pueden demostrarse
plot(res.aov, 1)#homogenidad de la varianza





