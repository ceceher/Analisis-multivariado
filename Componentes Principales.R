# Análisis de componentes principales
str(iris)

# Particionar los datos
set.seed(42)
ind <- sample(2, nrow(iris),
                replace = T, 
                prob = c(0.8, 0.20))
train <- iris[ind == 1,]
test <- iris[ind == 2,]

library(psych)

pairs.panels(train[,-5],
             gap = 0,
             bg = c("blue", "yellow", "red")[train$Species],
             pch = 21)

# Componentes principales

pc <- prcomp(train[,-5],
             center = T,
             scale. = T)
attributes(pc)

pc$scale
pc
summary(pc)

pairs.panels(pc$x,
             gap = 0,
             bg = c("red", "blue", "green")[train$Species],
             pch = 21)

################################################
#### Predicción

pred <- predict(pc, train)

training <- data.frame(pred, train[5])
testing <- predict(pc, test)
testing <- data.frame(testing, test[5])

library(nnet)

training$Species
?relevel()

relevel(training$Species, ref = "setosa")

modelo <- multinom(Species ~ PC1 + PC2, data = training)

summary(modelo)

prediccion <- predict(modelo, training)
prediccion

tablita <- table(prediccion, training$Species)
1 - sum(diag(tablita)) / sum(tablita)

prediccion_test <- predict(modelo, testing)
tablita_test <- table(prediccion_test, testing$Species)
1 - sum(diag(tablita_test)) / sum(tablita_test)

