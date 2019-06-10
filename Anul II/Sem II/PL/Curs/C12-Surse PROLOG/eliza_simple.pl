/*
  Adaptare dupa varianta din "The Art of Prolog" de Leon Sterling si Ehud Shapiro
  
*/



eliza :- write('tell me'),nl,read(AInput), atomic_list_concat(Input,' ',AInput), eliza(Input).

eliza([bye]) :-
   writeln(['Goodbye. I hope I have helped you']).
eliza(Input) :-
   pattern(Stimulus,Response),
   match(Stimulus,Table,Input),
   make(Response,Table,Output),
   reply(Output),
   read(AInput1), atomic_list_concat(Input1,' ',AInput1),
    eliza(Input1).




match([N|Pattern],Table,Target) :-
   integer(N), 
   lookup(N,Table,LeftTarget), LeftTarget \== [],
   append(LeftTarget,RightTarget,Target),    
   match(Pattern,Table,RightTarget).
match([N|Pattern],Table,Target) :-
   integer(N), append(LeftTarget,RightTarget,Target), LeftTarget \== [],
   match(Pattern,[nw(N,LeftTarget)|Table],RightTarget).
match([X],_,Target):- member(X,Target),important(X).
match([Word|Pattern],Table,[Word|Target]) :-
   atom(Word),
   match(Pattern,Table,Target).
match([],Table,[]).


make([N|Pattern],Table, Target) :-
   integer(N), 
   lookup(N,Table,LeftTarget),
   make(Pattern,Table,RightTarget), append(LeftTarget,RightTarget,Target).
make([Word|Pattern],Table,[Word|Target]) :-
   atom(Word),
   make(Pattern,Table,Target).
make([],Table,[]).





pattern([i,am,1],['How',long,have,you,been,1,?]).
pattern(R,['What',makes,you,think,'I',2,you,?]) :-  member(R,[[i,know,you,2,me], [i,think,you,2,me],[i,belive,you,2,me],[can, you, 2, me]]).
pattern([i,like,1],['Does',anyone,else,in,your,family,like,1,?]).
pattern([i,feel|_],['Do',you,often,feel,that,way,?]).
pattern([X],['Please',you,tell,me,more,about,X]) :- important(X).
pattern(G,AG) :- member(G,[[hi],[hello]]), random_select(AG,[['Hi',there,!], ['Hello',!,'How',are,you,today,?]],_).
pattern(_,['Please',go,on,'.']).

 important(father).			important(mother).
    important(sister).			important(brother).
    important(son).			important(daughter).

reply([Head|Tail]) :- write(Head), write(' '), reply(Tail).
reply([]) :- nl.

lookup(X,[np(X,V)|XVs],V).
lookup(X,[np(X1,V1)|XVs],V) :- X \== X1, lookup(X,XVs,V).
lookup(X,[],[]).


