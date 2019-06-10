import random

GOL = '#'

def __str__(matr):
    sir = (" ".join([str(x) for x in matr[0:3]]) + "\n" +
           " ".join([str(x) for x in matr[3:6]]) + "\n" +
           " ".join([str(x) for x in matr[6:9]]) + "\n")

    return sir


def elem_identice(lista):
    '''
    lista contine elementele de pe linie, coloana  sau
     diagonale si verifica daca are doar valori de x
    sau doar valori de 0

    Daca lista contine un castigator, il intoarce pe acesta (x sau 0), altfel intoarce False
    '''
    set_lista = set(lista)
    if len(set_lista) == 1 and list(set_lista)[0] != '#':
        return list(set_lista)[0]
    
    return False

def final(matr):
    '''
    verifica liniile, coloanele si diagonalele cu ajutorul lui elem_identice si intoarce, dupa caz, castigatorul,
    remiza, sau False
    '''
    if elem_identice(matr[0:3]):
        return elem_identice(matr[0:3])
    elif elem_identice(matr[3:6]):
        return elem_identice(matr[3:6])
    elif elem_identice(matr[6:9]):
        return elem_identice(matr[6:9])
    elif elem_identice(matr[::3]):
        return elem_identice(matr[::3])
    elif elem_identice(matr[1::3]):
        return elem_identice(matr[1::3])
    elif elem_identice(matr[2::3]):
        return elem_identice(matr[2::3])
    elif elem_identice([matr[0], matr[4], matr[8]]):
        return elem_identice([matr[0], matr[4], matr[8]])
    elif elem_identice([matr[2], matr[4], matr[6]]):
        return elem_identice([matr[2], matr[4], matr[6]])
    
    if '#' not in matr:
        return "remiza"
    
    return False
    
def afis_daca_final(stare_curenta):
    final_ans = final(stare_curenta)
    if (final_ans):
        if (final_ans == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final_ans)

        return True

    return False


def main():
    print('Incepe jocul x si 0')

    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        JMIN = input("Doriti sa jucati cu x sau cu 0? ").lower()
        if (JMIN in ['x', '0']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie x sau 0.")
    JMAX = '0' if JMIN == 'x' else 'x'

    # initializare tabla
    tabla_curenta = [GOL] * 9
    print("Tabla initiala")
    print(__str__(tabla_curenta))

    # creare stare initiala
    j_curent = 'x'

    def move(table_curenta):
        while (True):
            x = random.randint(0, 8)
            if tabla_curenta[x] == '#':
                tabla_curenta[x] = j_curent
                break
        
        return tabla_curenta
    
    def jucator_opus(j_curent):
        if j_curent == '0':
            return 'x'
        return '0'
    

    while True:
        if j_curent == JMIN:
            # muta jucatorul 'x'
            tabla_curenta = move(tabla_curenta)

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(__str__(tabla_curenta))

            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(tabla_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            j_curent = jucator_opus(j_curent)

        # --------------------------------
        else:  # jucatorul e JMAX
            if j_curent == JMAX:
                # muta jucatorul '0'
                tabla_curenta = move(tabla_curenta)

                # afisarea starii jocului in urma mutarii utilizatorului
                print("\nTabla dupa mutarea jucatorului")
                print(__str__(tabla_curenta))

                # testez daca jocul a ajuns intr-o stare finala
                # si afisez un mesaj corespunzator in caz ca da
                if (afis_daca_final(tabla_curenta)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                j_curent = jucator_opus(j_curent)


if __name__ == "__main__":
    main()
