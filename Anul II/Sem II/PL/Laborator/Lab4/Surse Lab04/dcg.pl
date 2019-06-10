
%-----------------Exemplul 1-------------------

s --> np, vp.
np --> art, n.
vp --> v.
vp --> v, np.
art --> [the].
art --> [a].
n --> [boy].
n --> [girl].
v --> [loves].
v --> [hates].

/*
?- phrase(s,SenL), atomic_list_concat(SenL,' ',Sen).
*/


%----------------Exemplul 2----------------------

nat --> [o].
nat --> [s], nat.



/*
?- phrase(nat, Num), atom_chars(Natural,Num).
*/