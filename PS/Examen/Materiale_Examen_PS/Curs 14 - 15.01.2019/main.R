x = c(12,11,3,23,8,5,9)
m = mean(x)
m

sigma = sqrt(var(x))
sigma
ks.test(x, "pnorm", m, sigma)

# Nivel de semnificatie 5%
# p-value = 0.7139 > 0.05 => acceptam ipoteza H 
# "X are repartitie normala cu media 10.14286 si dispersia 6.491753^2" la nivel de semnificatie de 5%


# testati ipoteza "X are repartitie uniforma pe intervalul [2,24]" la nivel de semnificatie de 5%
ks.test(x, "punif", 2, 24)

# p-value = 0.1545 > 0.05 => acceptam ipoteza


# testati ipoteza "X are repartitie uniforma pe intervalul [0,100]" la nivel de semnificatie de 5%
ks.test(x, "punif", 0, 100)

# p-value = 7.282e-05 <= 0.05 => respingem ipoteza 




# testati ipoteza "X are repartitie exponentiala de parametru 1" la nivel de semnificatie de 1%
ks.test(x, "pexp", 1)

# p-value = 1.517e-09 <= 0.01 => respingem ipoteza






