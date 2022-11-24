mouse.data=data.frame(peso=c(0.9,1.8,2.4,3.5,3.9,4.4,5.1,5.6,6.3),
                     size=c(1.4,2.6,1.0,3.7,5.5,3.2,3.0,4.9,6.3))

mouse.data
plot(mouse.data$peso,mouse.data$size)
mouse.regression=lm(size ~ peso, data=mouse.data)
summary(mouse.regression)
abline(mouse.regression,col='blue')


mouse.data=data.frame(peso=c(0.9,1.8,2.4,3.5,3.9,4.4,5.1,5.6,6.3),
                      size=c(1.4,2.6,1.0,3.7,5.5,3.2,3.0,4.9,6.3),
                      cola=c(0.7,1.3,0.7,2,3.6,3,2.9,3.9,4))

plot(mouse.data)
multiple.regression=lm(size ~ peso + cola, data=mouse.data)
summary(multiple.regression)
