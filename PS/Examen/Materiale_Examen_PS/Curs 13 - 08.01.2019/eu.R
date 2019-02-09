
x = c(5,6,11,23,13,21,3,15,3,9,2,11,8,5,17,23,11,12,6,24,7,10,23,12,9,25,22,4,13,13,3,  7,10,1,8,9,5,20,17,18,2,3,7,19,1,10,3,22,42,68,25,30,5,8)
length(x)
mean(x)
var(x)

# Verificati ipoteza H: X are rep. normala de medie 10 si dispersie 100 la un nivel de semnificatie de 5%

#1)
range(x)

#Impartim R in 10 intervale disjuncte
d = 68 - 1

y = integer(11)
y
y[1] = -Inf

for (i in 2:10) y[i] = 1 + (i-1) * d / 10
y[11] = Inf
y

# A1 = (-infinit, 7.7], A2 = (7.7, 14.4], ..., A10 = (61.3, Inf)
# determinam nr. de valori ale selectiei din fiecare interval
n = integer(10)
n

for (i in 1:54) {
  for (j in 1:10) {
    if (y[j] < x[i] && x[i] <= y[j+1]) {
      n[j] = n[j] + 1
    }
  }
}
n

#verificare
sum(n)

# nj < 5, pentru orice j = 5,...,10
# Combinam intervalele A4, A5, ..., A10
k = 4
n = c(18,18,7,11)

#verificari:
length(n)
sum(n)

y = c(-Inf, 7.7, 14.4, 21.1, Inf)
# A1 = (-Inf, 7.7], A2 = (7.7, 14.4], ..., A4 = (21.1, Inf]

# 2)
# determinam probabilitatitle teoretice
p = integer(4)

# pnorm(y[i], medie, sqrt(dispersie))
p[1] = pnorm(y[2], 10, 10)
for (i in 2:3) {
  p[i] = pnorm(y[i+1], 10, 10) - pnorm(y[i], 10, 10)
}
p[4] = 1 - pnorm(y[4], 10, 10)
p

sum(p)

# 3)
# determinam d
d = sum(n^2 / (54*p)) - 54
d

# 4)
# determinam chi^2 indice k-1, alfa
chi = qchisq(1 - 0.05, 4 - 1)

# 5)
# d <= chi^2 indice k-1, alfa, deci acceptam ipoteza



# cu aceleasi date, determinati daca o repartitie normala e potrivita la un nivel de semnificatie de 0.1 %
# 1) ca mai sus
# 2)
m = mean(x)
m

sigma = sqrt((53/54) * var(x))
sigma

# 3)
p[1] = pnorm(y[2], m, sigma)
for (i in 2:3) {
  p[i] = pnorm(y[i+1], m, sigma) - pnorm(y[i], m, sigma)
}
p[4] = 1 - pnorm(y[4], m, sigma)

p
sum(p)

# 4)
d =  sum(n^2 / (54*p)) - 54
d


# 5) k-r-1 = 4-2-1
# determinam chipatrat indice k-r-1, alfa
chi = qchisq(1 - 0.001, 1)
chi

# 6) d <= chipatrat indice k - r - 1, alfa -> deci acceptam ipoteza repartitiei normale
#    cu parametrii estimati m, sigma la nivelul de 0.1%








