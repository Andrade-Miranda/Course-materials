install.packages("dplyr")
View(dat)# observar la data
library(dplyr) 
controls <- filter(dat, Diet=="chow") #keep only the ones with chow diet, filtra los datos que quieres
controls<-select(controls,Bodyweight)
unlist(controls)
controls<-filter(dat, Diet=="chow") %>% select(Bodyweight) %>% unlist # un solo comando para hacer la linea 4,5,6
mean(controls)

library(downloader)
url="https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/msleep_ggplot2.csv"
filename <- basename(url)
download(url,filename)
read.csv("msleep_ggplot2.csv") %>% class
data<-read.csv("msleep_ggplot2.csv")
rows <- filter(data, order=="Primates") %>% nrow
filter(data, order=="Primates") %>% class
rows <- filter(data, order=="Primates") %>% nrow
controls<-filter(data, order=="Primates") %>% select(sleep_total) #usando package
controls1 <- data[ data$order=="Primates", colnames(data)=="sleep_total"]# sin usar package dplyr
class(controls)
unlist(controls) %>% mean() # separar los datos para poder ponerlo como vector y sacar la media
?summarize
#agrupo por grupo y le saco promedio por grupo
controls2<-select(data,order,sleep_total) %>% group_by(order) %>% summarise(sleep_total = mean(sleep_total))
