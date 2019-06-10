# Problema cu testul de paternitate
# p = probabilitatea ca Gigel sa fie tatal copilului
# pnorm = probabilitate normala

p <- 1 - pnorm(2) + 1 - pnorm(3)
p

integrate(dnorm, -Inf, 2)

a <- pnorm(1.555)
b <- (pnorm(1.55) + pnorm(1.56)) / 2
c <- integrate(dnorm, -Inf, 1.555)
c

teutu <- function(x) {
  x^3
}

d <- integrate(teutu, -1, 1)
e <- integrate(teutu, -Inf, 2)

g <- gamma(1/ 2)
spi <- sqrt(pi)

rez <- gamma(11 / 2)
var <- qnorm(0.9)

myFnc <- function(x) {
  x^5 * (1 - x)^7
}

myIntegral <- integrate(myFnc, 0, 1)
1 / myIntegral$value