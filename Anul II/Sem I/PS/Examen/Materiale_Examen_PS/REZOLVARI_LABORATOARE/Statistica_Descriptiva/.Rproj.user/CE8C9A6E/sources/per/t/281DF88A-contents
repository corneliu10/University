# Statistica descriptiva

# Importare de date din fisiere .dat
d <- read.table("/Users/teo/Desktop/University/Laboartoare\ -\ Semestrul\ 1/PS/Statistica/date.dat", header = TRUE)
attach(d)
pie(facultate, labels = departament, main = "O placinta")
barplot(facultate, names.arg = departament, col = "lightblue")

sum(facultate)
barplot(facultate / 53, names.arg = departament, col = "lightblue")

e <- read.table("/Users/teo/Desktop/University/Laboartoare\ -\ Semestrul\ 1/PS/Statistica/date2.dat", header = TRUE)
attach(e)

hist(y, col = "beige")
m <- mean(y)
v <- var(y)
t <- seq(12, 34, 0.001)

hist(y, col = "beige", freq = FALSE)
lines(t, dnorm(t, m, sqrt(v)), col = "purple")


a <- qnorm(0.9) # aflu x pentru care cacat in tabelul ala imens