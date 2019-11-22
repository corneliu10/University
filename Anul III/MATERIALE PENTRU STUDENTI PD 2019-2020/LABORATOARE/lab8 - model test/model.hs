
data Linie = L [ Int ] 
     deriving Show
data Matrice = M [ Linie ]

-- liniiN (M [L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3
-- 	[L[1,2,3], L[8,5,3]]

-- doarPozN (M [L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3
--	True
	
-- doarPozN (M [L[1,2,-3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3
--	False

-- verifica (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 10
--	False
	
-- verifica (M[L[2,20,3], L[4,21], L[2,3,6,8,6], L[8,5,3,9]]) 25
--	True


-- M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]
-- 1 2 3
-- 4 5 
-- 2 3 6 8
-- 8 5 3