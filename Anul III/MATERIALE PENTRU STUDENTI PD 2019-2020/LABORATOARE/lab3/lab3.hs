import   Data.List

-- L3.1 Încercati sa gasiti valoarea expresiilor de mai jos si
-- verificati raspunsul gasit de voi în interpretor:

-- [x^2 | x <- [1 .. 10], x `rem` 3 == 2]
-- [(x, y) | x <- [1 .. 5], y <- [x .. (x+2)]]
-- [(x, y) | x <- [1 .. 3], let k = x^2, y <- [1 .. k]]
-- [x | x <- "Facultatea de Matematica si Informatica", elem x ['A' .. 'Z']]
-- [[x .. y] | x <- [1 .. 5], y <- [1 .. 5], x < y ]


factori :: Int -> [Int]
factori x = [y | y <- [1..x], x `rem` y == 0]

prim :: Int -> Bool
prim n = if length (factori n) == 2 then True else False 

numerePrime :: Int -> [Int]
numerePrime n = [x | x <- [2..n], prim x == True]

-- L3.2 Testati si sesizati diferenta:
-- [(x,y) | x <- [1..5], y <- [1..3]]
-- zip [1..5] [1..3]

myzip3 :: [Int] -> [Int] -> [Int] -> [(Int, Int, Int)]
myzip3 [] l2 l3 = []
myzip3 l1 [] l3 = [] 
myzip3 l1 l2 [] = [] 
myzip3 (h1 : t1) (h2 : t2) (h3 : t3) = (h1, h2, h3) : myzip3 t1 t2 t3

--------------------------------------------------------
----------FUNCTII DE NIVEL INALT -----------------------
--------------------------------------------------------
aplica2 :: (a -> a) -> a -> a
--aplica2 f x = f (f x)
--aplica2 f = f.f
--aplica2 f = \x -> f (f x)
aplica2  = \f x -> f (f x)

-- L3.3
{-

map (\ x -> 2 * x) [1 .. 10]
map (1 `elem` ) [[2, 3], [1, 2]]
map ( `elem` [2, 3] ) [1, 3, 4, 5]

-}

-- firstEl [ ('a', 3), ('b', 2), ('c', 1)]
firstEl :: [(a, b)] -> [a]
firstEl l = map (\ (ch, val) -> ch) l

sumList :: [[Int]] -> [Int]
sumList l = map (sum) l
-- sumList [[1, 3],[2, 4, 5], [], [1, 3, 5, 6]]

prel2 :: [Integer] -> [Integer]
prel2 l = map (\x -> if x `rem` 2 == 0 then x `div` 2 else x * 2) l
-- prel2 [2,4,5,6]

caracterInSir :: Char -> [[Char]] -> [[Char]]
caracterInSir c l = filter (elem c) l

patrateImpare :: [Int] -> [Int]
patrateImpare l = map (^2) (filter odd l) 

patratePozImpare :: [Int] -> [Int]
patratePozImpare l = map (\(a,b) -> b^2) (filter (\ (a, b) -> a `rem` 2 == 1) (zip [1..] l))

numaiVocale :: [[Char]] -> [[Char]]
numaiVocale l = map (\a -> filter (`elem` "aeiouAEIOU") a) l

myMap :: (a -> b) -> [a] -> [b]
myMap _ [] = []
myMap f (h:t) = f h : myMap f t

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = []
myFilter f (h:t)
    | f h == True = h:t'
    | otherwise = t'
    where
        t' = myFilter f t