
% Dumitru Corneliu
% grupa 235
% Numarul 2

aparitiiTotale([], _, 0).
aparitiiTotale([cn(Cuv, Aparitii)|T], Cuv1, R) :- 
    aparitiiTotale(T, Cuv1, R1),
    (member(Cuv1, [Cuv]) -> 
        R is R1+Aparitii;
    not(member(Cuv1, [Cuv])) ->
        R is R1
    ).

% aparitiiTotale([cn(apa, 4), cn(si, 9), cn(apa,2), cn(pahar, 6)], apa, T).

% P1
aparitii(L, Cuv1, Cuv2) :-
    aparitiiTotale(L, Cuv1, Ap1),
    aparitiiTotale(L, Cuv2, Ap2),
    Ap1 = Ap2.

% aparitii([cn(apa, 4), cn(si, 9), cn(apa,2), cn(pahar, 6)], apa, pahar).
% aparitii([cn(apa, 4), cn(si, 9), cn(apa,2), cn(pahar, 6), cn(carte, 9)], apa, si).

% P2
exista([], 0, []).
exista([c(Cuv, Len)|T], N, MultimeC) :- 
    N1 is N-Len,
    exista(T, N1, MultimeC1),
    append([Cuv], MultimeC1, MultimeC).
exista([c(_, _)|T], N, MultimeC) :- 
    N1 is N,
    exista(T, N1, MultimeC1), 
    append([], MultimeC1, MultimeC).

% exista([c(testul, 6), c(usor, 4), c(este, 4), c(ada, 3), c(car, 3), c(ler, 3), c(carte, 5)],9,MultimeC).
% exista([c(testul, 6), c(usor, 4), c(este, 4), c(ada, 3), c(car, 3), c(ler, 3), c(carte, 5)],2,MultimeC).

isvar(X) :- member(X, [u,v,w,x,y]).
isexp(X) :- member(X, [nul,u,v,w,x,y]).

% P3 a
simplifica(X, Z) :- isexp(X), Z = X.
simplifica(mu(_, Y), Z) :- Y = nul, Z = nul.
simplifica(mu(X, _), Z) :- X = nul, Z = nul.
simplifica(mu(X, Y), Z) :- isvar(X), isvar(Y), Z = mu(X, Y).
simplifica(mu(X, Y), Z) :- simplifica(X, Z1), simplifica(Y, _), Z1 = nul, Z = nul.
simplifica(mu(X, Y), Z) :- simplifica(X, _), simplifica(Y, Z2), Z2 = nul, Z = nul.
simplifica(mu(X, Y), Z) :- simplifica(X, Z1), simplifica(Y, Z2), Z = mu(Z1, Z2).
simplifica(ad(X, Y), Z) :- Y = nul, X = nul, Z = nul.
simplifica(ad(X, Y), Z) :- X = nul, isvar(Y), Z = Y.
simplifica(ad(X, Y), Z) :- Y = nul, isvar(X), Z = X.
simplifica(ad(X, Y), Z) :- isvar(X), isvar(Y), Z = ad(X, Y).
simplifica(ad(X, Y), Z) :- simplifica(X, Z1), simplifica(Y, Z2), Z1 = nul, Z = Z2.
simplifica(ad(X, Y), Z) :- simplifica(X, Z1), simplifica(Y, Z2), Z2 = nul, Z = Z1.
simplifica(ad(X, Y), Z) :- simplifica(X, Z1), simplifica(Y, Z2), Z = ad(Z1, Z2).

% simplifica(mu(mu(nul, v), mu(mu(x,y), nul)), Z).
% simplifica(ad(nul, v), v).
% simplifica(mu(ad(nul, v), ad(u, nul)), mu(v,u)).

val(nul, 0).
val(u, 3).
val(v, -4).
val(x, 2).
val(y, 7).
val(w, 7).

% P3 b
valoare(X, Rez) :- isexp(X), val(X, X1), Rez = X1.
valoare(mu(X, Y), Rez) :- isexp(X), isexp(Y), val(X, X1), val(Y, Y1), Rez is (X1*Y1).
valoare(mu(X, Y), Rez) :- valoare(X, Rez1), valoare(Y, Rez2), Rez is Rez1*Rez2.
valoare(ad(X, Y), Rez) :- isexp(X), isexp(Y), val(X, X1), val(Y, Y1), Rez is(X1+Y1).
valoare(ad(X, Y), Rez) :- valoare(X, Rez1), valoare(Y, Rez2), Rez is Rez1+Rez2.

% valoare(mu(mu(u, v),x), Rez).
% valoare(ad(mu(u,v),x), Rez).