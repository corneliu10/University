import Data.List

myInt = 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555

double :: Integer -> Integer
double x = x+x


--maxim :: Integer -> Integer -> Integer
maxim x y = if (x > y)
               then x
          else y

max3 x y z = let
             u = maxim x y
             in (maxim  u z)


max3 x y z = let
				u = (maxim x y)
			 in (maxim u z)

max4 :: Int->Int->Int->Int->Int			 
max4 x y z v = let 
				u = (max3 x y z)
			   in (maxim u v)

testmax4 a b c d = max4 a b c d >= a && max4 a b c d >= b 
				&& max4 a b c d >= c && max4 a b c d >= d

data Rezultat 
	= Vic | Inf | Eq
	deriving (Eq, Show)
	
data Alegere
	= Piatra
	| Foarfeca
	| Hartie
	deriving (Eq, Show)
	
partida :: Alegere -> Alegere -> Rezultat
partida Piatra Foarfeca = Vic
partida Hartie Piatra = Vic
partida Foarfeca Hartie = Vic
partida x y = if (x==y) then
				Eq
			  else
				Inf
