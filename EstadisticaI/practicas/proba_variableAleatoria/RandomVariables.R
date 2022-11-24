library(dplyr)
dat<-read.csv("/Users/Gustavo/AnacondaProjects/R_projects/clase_estadistica/femaleMiceWeights.csv")
control<- filter(dat,Diet=="chow")%>% select(Bodyweight)%>% unlist
controls1 <- dat[ dat$Diet=="chow", colnames(dat)=="Bodyweight"]# sin usar package dplyr
Treatment <- dat[ dat$Diet=="hf", colnames(dat)=="Bodyweight"]# sin usar package dplyr
mean(controls1)
mean(Treatment)
obs <- mean(Treatment) - mean(controls1) 
#acceso a todos los mice en este caso los control que son chow
population<-read.csv("/Users/Gustavo/AnacondaProjects/R_projects/clase_estadistica/femaleControlsPopulation.csv")
population<-unlist(population)
mean(sample(population,12))

#que pasa cuando Null Hypothesis is true
n<-1000
nulls <-vector("numeric",n)
for(i in 1:n){
control <- sample(population,12)
treatment <- sample(population,12)
nulls[i] <- mean(treatment)-mean(control)
}
max(nulls)
min(nulls)
hist(nulls)
mean(abs(nulls) > obs)#nulls is bigger tha observation



library(downloader) 
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/femaleControlsPopulation.csv"
filename <- basename(url)
download(url, destfile=filename)
x <- unlist( read.csv(filename) )
mean(x)
set.seed(1)
abs(mean(x)-mean(sample(x,5)))

mean(x)
set.seed(5)
abs(mean(x)-mean(sample(x,5)))

