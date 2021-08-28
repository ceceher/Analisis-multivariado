head(iris)
set.seed(42)

ind <- sample(2, nrow(iris), replace = T, prob = c(0.8, 0.2))
ind

table(ind)
train <- iris[ind == 1, ]

test <- iris[ind == 2, ]
library(psych)
pairs.panels(train[, -5], 
             gap = 0, 
             bg = c("red", "blue", "yellow")[train$Species],
             pch = 21)

unique(train$Species)

#Matriz de covarianzas
cov(train[, -5])

#Componente principal

cp <- prcomp(train[, -5], center = T, scale. = T)
cp

attributes(cp) 
cp$x #indica cuales son nuestros datos 

print(cp)
#PC1 es el que capturaría mayor parte de la varianza 

summary(cp)

pairs.panels(cp$x, 
             gap = 0,
             bg = c("red", "blue", "green")[train$Species],
             pch = 21)

