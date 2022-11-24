install.packages("ggpubr")
library("ggpubr")
my_data <- mtcars
head(my_data, 6)
ggscatter(my_data, x = "mpg", y = "wt", add = "reg.line", conf.int = TRUE, cor.coef = TRUE, cor.method = "pearson",
          xlab = "Miles/(US) gallon", ylab = "Weight (1000 lbs)")

#c??lculo de correlaci??n usando paquete por defecto de R
cor(x = my_data$mpg, y = my_data$wt, method = "pearson")
cor.test(x = my_data$mpg, y = my_data$w, method="pearson")


#There are different methods to perform correlation analysis:
#Pearson correlation (r), which measures a linear dependence 
#between two variables (x and y). It???s also known as a parametric 
#correlation test because it depends to the distribution of the data. 
#It can be used only when x and y are from normal distribution. 
#The plot of y = f(x) is named the linear regression curve.
#Kendall tau and Spearman rho, which are rank-based correlation 
#coefficients (non-parametric).


#C??lculo de r Utilice la muestra aleatoria simple de datos que
#aparece al margen para calcular el valor del coeficiente de correlaci??n lineal r
x=c(3,1,3,5)
y=c(5,8,6,4)
datar=data.frame(x,y)

ggscatter(datar, x="x" , y="y" , add = "reg.line", conf.int = TRUE, cor.coef = TRUE, cor.method = "pearson",
          xlab = "x", ylab = "y")
cor(x = datar$x, y = datar$y, method = c("pearson", "kendall", "spearman"))
cor.test(x = datar$x, y = datar$y, method=c("pearson", "kendall", "spearman"))

install.packages("ISLR")
library(MASS)
library(ISLR)
