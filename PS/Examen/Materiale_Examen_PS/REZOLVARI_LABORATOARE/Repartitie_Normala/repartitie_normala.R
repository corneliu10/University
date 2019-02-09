# Repartitie normala de medie m si dispersie sigma^2

m <- 0
sigma <- 1
x <- seq(-5, 5, 0.001)

plot(x, dnorm(x, m, sigma), col = "magenta")
for (i in -3:3)
  lines(x, dnorm(x, i, sigma), col = i + 4)

plot(x, dnorm(x, m, sigma), col = "magenta", xlim = c(-2, 2), ylim = c(0, 0.3))
for (i in -3:3)
  lines(x, dnorm(x, m, i + 4), col = i + 4)

# functia de repartitie
plot(x, pnorm(x, m, sigma), col = "magenta")
for (i in -3:3)
  lines(x, pnorm(x, i, sigma), col = i + 4)

# Proprietatile functiei FI
y <- rep(0.5, 10001)
plot(x, pnorm(x), col = "blue")
lines(x, y, col = "red")

f <- function(x, p) {
  x^3 * exp(-x / p)
}

I <- integrate(f, lower = 0, upper = Inf)

1 - pnorm(0,269679945)