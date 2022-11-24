#library(foreign)
#file.choose()
#dataset = read.spss("/Users/Gustavo/Downloads/Base de datos ENSANUT/Bases ENSANUT spss/ensanut_f1_vivienda.sav", to.data.frame=TRUE)




Nac_defun=read.csv(file.choose(),header = TRUE,sep = ";")

library(ggplot2)

# Basic histogram edad de defunción
ggplot(Nac_defun, aes(Nac_defun$est_civil)) + 
  geom_histogram(breaks=seq(0, 7, by = 1), col="red", 
                 fill="green",alpha = .2) +
  labs(x="Edad", y="conteo") + 
  labs(title="Mortalidad por edad") + 
  xlim(c(0,7))




# Basic histogram edad de defunción
  ggplot(Nac_defun, aes(Nac_defun$edad)) + 
  geom_histogram(breaks=seq(0, 110, by = 5), col="red", 
  fill="green",alpha = .2) +
  labs(x="Edad", y="conteo") + 
  labs(title="Mortalidad por edad") + 
  geom_density(aes(y=..count..*5))+
  xlim(c(0,120))

# Basic histogram provincia
ggplot(Nac_defun, aes(Nac_defun$prov_fall)) + 
  geom_histogram(breaks=seq(0, 23, by = 1), col="red", 
                 fill="green",alpha = .2, aes(y = ..density..)) +
  labs(x="provincia", y="% relative") + 
  labs(title="Mortalidad por provincia") + 
  xlim(c(0,23)) 

##
ggplot(data = Nac_defun) + 
  geom_bar(mapping = aes(x = Nac_defun$prov_fall, y = ..prop.., group = 1), stat = "count") + 
  scale_y_continuous(labels = scales::percent_format()) +
  xlim(c(0,23)) +
  labs(x="provincia", y="% relative") + 
  labs(title="Mortalidad por provincia") 

###
Frecuencia=as.data.frame(prop.table(table(Nac_defun$prov_fall)))
colnames(Frecuencia)[2] = "Porcentaje"
colnames(Frecuencia)[1] = "codigo"
Provincias = c("Azuay", "Bolívar", "Cañar","Carchi", "Cotopaxi","Chimborazo", "El Oro","Esmeraldas", "Guayas","Imbabura", "Loja","Los Ríos", "Manabí", 
       "Morona Santiago", "Napo","Pastaza", "Pichincha", "Tungurahua", "Zamora Chinchipe","Galápagos", "Sucumbios","Orellana", "Santo domingo",
       "Santa elena", "Exterior","Zona no delimitada")
Frecuencia = cbind(Frecuencia, Provincias)
ggplot(Frecuencia,aes(Provincias,Porcentaje,fill=rownames(Frecuencia)))+
  geom_bar(stat = "identity")+
  scale_y_continuous(labels = scales::percent_format()) +
  guides(fill=FALSE)+   
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5))







