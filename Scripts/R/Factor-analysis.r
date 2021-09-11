library(psych)

df_bfi <- bfi

head(df_bfi)
help(bfi)

prop.table(table(bfi$A1))

df_bfi <- df_bfi[complete.cases(df_bfi),] #Elimina los NA

mcbfi <- cor(df_bfi)

#Factor analysis
?fa()
factores <- fa(r = mcbfi, nfactors = 6)
factores

fa.diagram(factores)

