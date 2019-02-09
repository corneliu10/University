# Marian Darius - Corneliu Dumitru
# Grupa 235
# Problema 1
# 
# # Dataset
# longley
# 
# # summary for longley
# summary(longley)
# 
# # media, varianta, quartile si boxplot - GNP.deflator
# mean(longley$GNP.deflator)
# median(longley$GNP.deflator)
# var(longley$GNP.deflator)
# quantile(longley$GNP.deflator)
# boxplot(longley$GNP.deflator, horizontal = TRUE)
# 
# # media, varianta, quartile si boxplot - GNP
# mean(longley$GNP)
# median(longley$GNP)
# var(longley$GNP)
# quantile(longley$GNP)
# boxplot(longley$GNP, horizontal = TRUE)
# 
# # media, varianta, quartile si boxplot - Unemployed
# mean(longley$Unemployed)
# median(longley$Unemployed)
# var(longley$Unemployed)
# quantile(longley$Unemployed)
# boxplot(longley$Unemployed, horizontal = TRUE)
# 
# # media, varianta, quartile si boxplot - Armed.Forces
# mean(longley$Armed.Forces)
# median(longley$Armed.Forces)
# var(longley$Armed.Forces)
# quantile(longley$Armed.Forces)
# boxplot(longley$Armed.Forces, horizontal = TRUE)
# 
# # media, varianta, quartile si boxplot - Population
# mean(longley$Population)
# median(longley$Population)
# var(longley$Population)
# quantile(longley$Population)
# boxplot(longley$Population, horizontal = TRUE)
# 
# # media, varianta, quartile si boxplot - Year
# mean(longley$Year)
# median(longley$Year)
# var(longley$Year)
# quantile(longley$Year)
# boxplot(longley$Year, horizontal = TRUE)
# 
# # media, varianta, quartile si boxplot - Employed
# mean(longley$Employed)
# median(longley$Employed)
# var(longley$Employed)
# quantile(longley$Employed)
# boxplot(longley$Employed, horizontal = TRUE)

# Problema 2

# Definim o functie care calculeaza modelul pentru o Regresie Liniara
# regresie_liniara<-function(predictor, rezultat, nume_predictor, nume_rezultat) {
#   model <- lm(rezultat ~ predictor)
#   plot(predictor,
#        rezultat, 
#        main = paste("Regresie",nume_predictor,"&",nume_rezultat),
#        abline(model, col="magenta"),
#        cex = 1.3,
#        pch = 16,
#        xlab = nume_rezultat,
#        ylab= nume_predictor)
# }
# 
# # calculam regresiile liniare pentru toate combinatiile: Employed ~ .
# # Model bun
# regresie_liniara(longley$Employed, longley$GNP.deflator, "Employed", "GNP Deflator")
# # Model bun
# regresie_liniara(longley$Employed, longley$GNP, "Employed", "GNP")
# # Model rau
# regresie_liniara(longley$Employed, longley$Unemployed,  "Employed", "Unemployed")
# # Model rau
# regresie_liniara(longley$Employed, longley$Armed.Forces,  "Employed", "Armed forces")
# # Model bun
# regresie_liniara(longley$Employed, longley$Population,  "Employed", "Population")
# # Model bun
# regresie_liniara(longley$Employed, longley$Year,  "Employed", "Year")
# 
# # Cream modelul pentru Regresie Multipla cu Relatia: Employed ~ .
# # Employed = var. raspuns si restul sunt var. predictor
# # Din teste reiese ca relatia cu Employed are eroare totala minima
# model <- lm(Employed~., data = longley)
# 
# # Show the model.
# print(model)
# 
# coefficients(model) # model coefficients
# confint(model, level=0.95) # CIs for model parameters 
# fitted(model) # predicted values
# residuals(model) # residuals
# anova(model) # anova table 
# vcov(model) # covariance matrix for model parameters 
# influence(model) # regression diagnostics
# 
# layout(matrix(c(1,2,3,4),2,2)) # 4 graph on page
# 
# # interpretare
# plot(model)

# Problem 3
# Care este probabilitatea ca o persoana sa aiba un IQ egal cu X?
# sample.range <- 50:150
# iq.mean <- 100
# iq.sd <- 15
# iq.dist <- dnorm(sample.range, mean = iq.mean, sd = iq.sd)
# iq.df <- data.frame("IQ" = sample.range, "Density" = iq.dist)
# install.packages("ggplot2")
# library(ggplot2)
# ggplot2(iq.df, aes(x = IQ, y = Density)) + geom_point()
# 
# pp <- function(x) {
#   print(paste0(round(x * 100, 3), "%"))
# }
# 
# # probabilitatea ca IQ = 140?
# pp(iq.df$Density[iq.df$IQ == 140])
# 
# # probabilitatea ca IQ >= 140?
# pp(sum(iq.df$Density[iq.df$IQ >= 140]))
# 
# # probabilitatea ca 50 < IQ <= 90?
# pp(sum(iq.df$Density[iq.df$IQ <= 90]))
