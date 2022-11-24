library(dplyr)
rm(list=ls()) #clear workspace
dat<-read.csv("femaleMiceWeights.csv")
control<- filter(dat,Diet=="chow")%>% select(Bodyweight)%>% unlist
controls1 <- dat[ dat$Diet=="chow", colnames(dat)=="Bodyweight"]# sin usar package dplyr
Treatment <- dat[ dat$Diet=="hf", colnames(dat)=="Bodyweight"]# sin usar package dplyr
mean(controls1)
mean(Treatment)
mean(Treatment) - mean(controls1) 
hist(control)
f=function(x){x^pi}#funcion de una variable x^pi
f(2)
g=function(x,y){(x-y)^pi}
g(5,2)
rm(f)
