

%% definirea operatorilor

:- op(630, xfy, sau).      
:- op(620, xfy, si).        
:- op(610, fy,  nu). 
:- op(640, xfy, imp). 



%% is_var(X) :- member(X,[a,b,c,d,e]).

is_var(a). is_var(b). is_var(c). is_var(d). is_var(e).

            

find_vars(X si Y,Vin,Vout) :- find_vars(X,Vin,Vtemp),
                               find_vars(Y,Vtemp,Vout).
find_vars(X sau Y,Vin,Vout) :-  find_vars(X,Vin,Vtemp),
                               find_vars(Y,Vtemp,Vout).
find_vars(X imp Y,Vin,Vout) :-  find_vars(X,Vin,Vtemp),
                               find_vars(Y,Vtemp,Vout).
find_vars(nu X,Vin,Vout) :-   find_vars(X,Vin,Vout).

find_vars(X,Vin,Vin) :- is_var(X), member(X,Vin).

find_vars(X,Vin, [X|Vin]):- is_var(X).


