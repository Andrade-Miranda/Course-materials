install.packages("devtools")
library(devtools)
dat <- read.csv("femaleMiceWeights.csv")
col(dat)
dat[12,2]#obtener un valor del arreglo
dat[,2]#obtener una columna del arreglo
which(dat[,2]==85)#cual dato de la 2 columna es 85
dat[,c("Bodyweight")] #obtener una columna del arreglo
length(dat[,c("Bodyweight")])# obtener longuitud de las observaciones
seq(3,7) # 3:7 create a sequence with value 3 4 5 6 7
mean(dat[13:24,c("Bodyweight")]) # media de una columna
?sample
set.seed(1)
sample(dat[13:24,c("Bodyweight")],1) # tomo una muestra aleatoria del peso

