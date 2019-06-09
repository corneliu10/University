/*
  Adaptare dupa varianta din "The Art of Prolog" de Leon Sterling si Ehud Shapiro
  
*/
block(a).	block(b).	block(c).
place(p).	place(q). place(r).

transform(State1,State2,Plan, N) :- 
   transform(State1,State2,[State1],Plan,N).

transform(State,State,Visited,[],_).
transform(State1,State2,Visited,[Action|Actions],N) :-
   legal_action(Action,State1),                
   update(Action,State1,State), 
   \+ member(State,Visited), length(Visited,M), M < N, 
   transform(State,State2,[State|Visited],Actions,N).

legal_action(to_place(Block,Y,Place),State) :- 
   block(Block), clear(Block,State), place(Place), clear(Place,State).
legal_action(to_block(Block1,Y,Block2),State) :- 
   block(Block1), clear(Block1,State), block(Block2), 
	Block1 \== Block2, clear(Block2,State).
    


suggest(to_place(X,Y,Z) ,State) :- member(on(X,Z), State), place(Z).                                                                                                                                                                              
suggest(to_block(X,Y,Z) ,State) :- member(on(X,Z) ,State), block(Z).    

clear(X,State) :- \+ member(on(A,X),State).
on(X,Y,State) :- member(on(X,Y),State).

update(to_block(X,Y,Z),State,State1) :-
   substitute(on(X,Y),on(X,Z),State,State1).
update(to_place(X,Y,Z),State,State1) :-
   substitute(on(X,Y),on(X,Z),State,State1).

substitute(X,Y,[X|Xs],[Y|Xs]).
substitute(X,Y,[X1|Xs],[X1|Ys]) :- X \== X1, substitute(X,Y,Xs,Ys).


 /*  Testing 

se apeleaza 
?- test_plan(test1,Plan,5).
?- test_plan(test2,Plan,5).
?- test_plan(test3,Plan,3).
 */

test_plan(Name,Plan,N) :-
   initial_state(Name,I), final_state(Name,F), transform(I,F,Plan,N).


initial_state(test1,[on(a,b), on(b,p),on(c,r)]).
final_state(test1,[on(a,b),on(b,c),on(c,r)]).

% test2 nu are solutie
initial_state(test2,[on(a,r),on(b,c),on(c,p)]).
final_state(test2,[on(a,q),on(b,q),on(c,p)]).

initial_state(test3,[on(a,r),on(b,c),on(c,p)]).
final_state(test3,[on(a,q),on(b,a),on(c,p)]).

