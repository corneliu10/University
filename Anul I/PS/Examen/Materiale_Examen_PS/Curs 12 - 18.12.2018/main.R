
x = c(3.7, 4.2, 5.8, 6.9, 2.7, 5.5, 6.3, 1.7, 2.0, 3.2, 2.3, 0.2, 3.5, 7.2, pi, 6.0, 3.0, 8.1, 8.0, 10.0, 13.0)
x2 = c(5, 14, 3, 11, 23, 17, 15, 18, 10, 16, 7, 4, 13, 3, 2, pi, 1, 9, 7, 8, 2)
length(x2)
y = c(3, 20, 6, 8, 6, 10, 5, 11, 23, 21, 5, 29, 14, 7, 2, 24, 13, 6, 5 , 4, 9)
length(y)

x1 = x
# regresie dubla - comentariu 1
# Y = beta 0 + beta 1 x1 + beta 2 x2 + Z

# Comentariu 2:
# Determinati estimarile prin metoda celor mai mici patrate pentru beta 0, beta 1. beta 2
C = cbind(1, x1, x2)
C

# comentariu 3
# teta^ = (CTC)^-1 CTy

solve(t(C) %*% C, t(C) %*% y)

# comentariu 4
# beta 0^ = 17.48089866
# beta 1^ = -1.10038398
# beta 2^ = -0.09925756

# exemplul 2
# E(Y) = beta0 + beta1x + beta2x^2
# Calculam estimarile prin metoda celor mai mici patrate pt. beta0, beta1, beta2
C = cbind(1,x,x^2)
solve(t(C)%*%C, t(C)%*%y)

# q()

# beta 0^ = 21.3926437
# beta 1^ = -3.2737866
# beta 2^ = 0.1784249

# exemplul 3
# Calculam estimarile prin metoda celor mai mici patrate pentru beta0, beta1
# lnY = ln(beta0) + beta1x + Z

C = cbind(1, x)
solve(t(C)%*%C, t(C) %*% log(y))

# ln(beta0^) = 2.52015885
# beta1 ^= -0.07227934

exp(2.52015885)

# beta0^ = 12.43057


# exemplul 4
# Y = beta0 + beta1 x1 + beta2 x2 + beta11 x1^2 + beta22 x2^2 + beta12 x1x2
# Calculati estimarile prin metoda celor mai mici patrate pt beta0, beta1, beta2, beta11, beta22, beta12
C = cbind(1, x1, x2, x1^2, x2^2, x1*x2)
solve(t(C)%*%C, t(C)%*%y)

# beta0^ = 16.83272155
# beta1^ = -3.04018413
# beta2^ = 1.39388267
# beta11^ = 0.17684970
# beta22^ = -0.05739009
# beta12^ = -0.05657813




