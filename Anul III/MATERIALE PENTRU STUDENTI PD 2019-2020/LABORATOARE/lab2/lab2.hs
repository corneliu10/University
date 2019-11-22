-- la nevoie decomentati liniile urmatoare:

-- import Data.Char
-- import Data.List
import Data.Char

---------------------------------------------
-------RECURSIE: FIBONACCI-------------------
---------------------------------------------

fibonacciCazuri :: Integer -> Integer
fibonacciCazuri n
  | n < 2     = n
  | otherwise = fibonacciCazuri (n - 1) + fibonacciCazuri (n - 2)

fibonacciEcuational :: Integer -> Integer
fibonacciEcuational 0 = 0
fibonacciEcuational 1 = 1
fibonacciEcuational n =
    fibonacciEcuational (n - 1) + fibonacciEcuational (n - 2)

{-| @fibonacciLiniar@ calculeaza @F(n)@, al @n@-lea element din secvența
Fibonacci în timp liniar, folosind funcția auxiliară @fibonacciPereche@ care,
dat fiind @n >= 1@ calculează perechea @(F(n-1), F(n))@, evitănd astfel dubla
recursie. Completați definiția funcției fibonacciPereche.

Indicație:  folosiți matching pe perechea calculată de apelul recursiv.
-}
fibonacciLiniar :: Integer -> Integer
fibonacciLiniar 0 = 0
fibonacciLiniar n = snd (fibonacciPereche n)
  where
    fibonacciPereche :: Integer -> (Integer, Integer)
    fibonacciPereche 1 = (0, 1)
    fibonacciPereche n = (first, second)
        where
			(a, b) = fibonacciPereche(n-1)
			first = b
			second = a + b

---------------------------------------------
----------RECURSIE PE LISTE -----------------
---------------------------------------------
semiPareRecDestr :: [Int] -> [Int]
semiPareRecDestr l
	| null l = l
	| even h = h `div` 2 : t'
	| otherwise = t'
	where
		h = head l
		t = tail l
		t' = semiPareRecDestr t

semiPareRecEq :: [Int] -> [Int]
semiPareRecEq [] = []
semiPareRecEq (h:t)
	| even h = h `div` 2 : t'
	| otherwise = t'
	where
		t' = semiPareRecEq t

---------------------------------------------
----------DESCRIERI DE LISTE ----------------
---------------------------------------------
semiPareComp :: [Int] -> [Int]
semiPareComp l = [x `div` 2 | x <- l, even x]
 
-- L2.2
inIntervalRec :: Int -> Int -> [Int] -> [Int]
inIntervalRec l h [] = []
inIntervalRec low hi (h:t)
	| h >= low && h <= hi = h:t'
	| otherwise = t'
	where 
		t' = inIntervalRec low hi t

inIntervalComp :: Int -> Int -> [Int] -> [Int]
inIntervalComp lo hi [] = []
inIntervalComp lo hi l = [x | x <- l, x >= lo && x <= hi]

-- L2.3

pozitiveRec :: [Int] -> Int
pozitiveRec [] = 0
pozitiveRec (h:t)
	| h > 0 = r' + 1
	| otherwise = r'
	where
		r' = pozitiveRec t

pozitiveComp :: [Int] -> Int
pozitiveComp l = r
	where
		r = length [x | x <- l, x > 0]

testPozitive :: [Int] -> Bool
testPozitive l = pozitiveRec l == pozitiveComp l

-- L2.4 
aux :: [Int] -> Int -> [Int]
aux [] _ = []
aux (h:t) poz
	| h `mod` 2 == 1 = poz : t'
	| otherwise = t'
	where
		t' = aux t (poz+1) 

pozitiiImpareRec :: [Int] -> [Int]
pozitiiImpareRec l = aux l 0


pozitiiImpareComp :: [Int] -> [Int]
pozitiiImpareComp l = [y | (x,y) <- zip l [0..], odd x]


-- L2.5

multDigitsRec :: String -> Int
multDigitsRec [] = 1
multDigitsRec (h:t)
	| isDigit h = digitToInt h * t'
	| otherwise = t'
	where
		t' = multDigitsRec t

multDigitsComp :: String -> Int
multDigitsComp sir = undefined

-- L2.6 

discountRec :: [Float] -> [Float]
discountRec [] = []
discountRec (h:t)
	| h' < 200 = h':t'
	| otherwise = t'
	where
		h' = h * 3/4
		t' = discountRec t

discountComp :: [Float] -> [Float]
discountComp l = [x * 3/4 | x <- l, x * 3/4 < 200]