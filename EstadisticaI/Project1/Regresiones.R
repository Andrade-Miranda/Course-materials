rm(list = ls()) # limpiar el workspace
Locacion = c("Quito","Guayaquil","Cuenca","Ambato")
numerodeautos = c(52,40,45,43)
FrecuenciaRelativa = c(0.289,0.222,0.250,0.239)
mean(numerodeautos)
var(numerodeautos)
median(numerodeautos)
max(numerodeautos)
min(numerodeautos)
length(numerodeautos)
data.entry(x=c(NA))# defino la data conforme la escribo usando hoja similar a excel
df=data.frame(Locacion,numerodeautos,FrecuenciaRelativa)
plot(df$Locacion,df$numerodeautos)# x , y
plot(df$numerodeautos,df$FrecuenciaRelativa)
regres=lm(FrecuenciaRelativa~numerodeautos, data=df)#metodos lineales(regresion) caluclar la recta de regresion y en funcion de la variable x
regres
abline(regres,col="blue")
summary(regres)

df_pearson=read.table("http://aprender.uib.es/Rdir/pearson.txt",header=TRUE)# datos de internet
plot(df_pearson)
cor(x = df_pearson$Padres, y = df_pearson$Hijos, method = "pearson")
regres=lm(Hijos~Padres, data=df_pearson)
regres
abline(regres,col="red")
summary(regres)

