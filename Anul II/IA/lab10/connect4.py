import time
import copy

ADANCIME_MAX = 4

def nu_mai_e_gol(matr):
    for linie in matr:
        for coloana in linie:
            if coloana == '#':
                return False
    return True


class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 7
    NR_LINII = 6
    JMIN = None  # 'R'
    JMAX = None  # 'G'
    GOL = '#'
    TABLA_INI = [
                 [GOL]*NR_COLOANE,
                 [GOL]*NR_COLOANE,
                 [GOL]*NR_COLOANE,
                 [GOL]*NR_COLOANE,
                 [GOL]*NR_COLOANE,
                 [GOL]*NR_COLOANE
				]

    def __init__(self, tabla=None):
        self.matr = tabla or self.__class__.TABLA_INI

    def get_diagonala1(self, linie, coloana):
		# ia elemente de pe diagonala \
        lista_return = []
        if linie + 3 < 6 and coloana + 3 < 7:
            for (i, j) in zip(range(linie, linie + 4), range(coloana, coloana+4)):
                lista_return.append(self.matr[i][j])
        return lista_return

    def get_diagonala2(self, linie, coloana):
	# ia elemente de pe diagonala /
        lista_return = []
        if linie + 3 < 6 and coloana - 3 >= 0:
            for (i, j) in zip(range(linie, linie+4), range(coloana, coloana-4, -1)):
                lista_return.append(self.matr[i][j])
        return lista_return

    def final(self):
        rez = False

        # verificam pe linii daca gasim acelasi element (!= '#') de 4 ori
        for linie_vals in self.matr:
            for col_idx in range(len(linie_vals) - 3):
                curent = linie_vals[col_idx]
                ok = True
                if curent == '#':
                    continue
                for col_ver in range(col_idx + 1, col_idx + 4):
                    if linie_vals[col_ver] != curent:
                        ok = False
                        break
                if ok:
                    return curent

        # verificam pe coloane daca gasim acelasi element (!= '#') de 4 ori
        for col in range(Joc.NR_COLOANE):
            for lin in range(Joc.NR_LINII - 3):
                curent = self.matr[lin][col]
                if curent == '#':
                    continue
                ok = True
                for lin_ver in range(lin + 1, lin + 4):
                    if self.matr[lin_ver][col] != curent:
                        ok = False
                if ok:
                    return curent
                
        # diagonale \ /
        for lin in range(Joc.NR_LINII):
            for col in range(Joc.NR_COLOANE):
                d1 = self.get_diagonala1(lin, col)
                d2 = self.get_diagonala2(lin, col)

                s1 = set(d1)
                if len(s1) == 1 and d1[0] != '#':
                    return d1[0]

                s2 = set(d2)
                if len(s2) == 1 and d2[0] != '#':
                    return d2[0]

        if rez == False and nu_mai_e_gol(self.matr):
            return 'remiza'
        else:
            return False

    def get_linie(self, coloana):
        for linie in range(len(self.matr)):
            if self.matr[Joc.NR_LINII-linie-1][coloana] == Joc.GOL:
                return Joc.NR_LINII-linie-1
        return False

    def mutari(self, jucator_opus):
        l_mutari = []
        for coloana in range(0, Joc.NR_COLOANE):
            linie = self.get_linie(coloana)
            if linie is not False:
                if self.matr[linie][coloana] == Joc.GOL:
                    # daca avem lista[liste], cum este cazul lui matr, clonarea acestei liste se face cu deepcopy
                    matr_tabla_noua = copy.deepcopy(self.matr)
                    matr_tabla_noua[linie][coloana] = jucator_opus
                    l_mutari.append(Joc(matr_tabla_noua))

        return l_mutari

    def nr_intervale_deschise(self, jucator):
        # un interval de 4 pozitii adiacente (pe linie, coloana sau diagonala)
        # este deschis pt "jucator" daca nu contine "juc_opus"

        juc_opus = Joc.JMIN if jucator == Joc.JMAX else Joc.JMAX
        rez = 0

        # linii
        for lin in range(Joc.NR_LINII):
            for col in range(Joc.NR_COLOANE - 3):
                lista_val = []
                for col_ver in range(col, col + 4):
                    lista_val.append(self.matr[lin][col_ver])
                
                if juc_opus not in lista_val:
                    rez += 1

        # coloane
        for col in range(Joc.NR_COLOANE):
            for lin in range(Joc.NR_LINII - 3):
                lista_val = []
                for lin_ver in range(lin, lin + 4):
                    lista_val.append(self.matr[lin_ver][col])
                
                if juc_opus not in lista_val:
                    rez += 1

        # diagonale \ /
        for lin in range(Joc.NR_LINII):
            for col in range(Joc.NR_COLOANE - 3):
                d1 = self.get_diagonala1(lin, col)
                d2 = self.get_diagonala2(lin, col)
                
                if juc_opus not in d1 and len(d1) > 0:
                    rez += 1
                
                if juc_opus not in d2 and len(d2) > 0:
                    rez += 1

        return rez

    def fct_euristica(self):
        # TO DO: alte variante de euristici? .....

        # intervale_deschisa(juc) = cate intervale de 4 pozitii
        # (pe linii, coloane, diagonale) nu contin juc_opus
        return self.nr_intervale_deschise(Joc.JMAX) - self.nr_intervale_deschise(Joc.JMIN) - 1

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        # if (adancime==0):
        if t_final == self.__class__.JMAX:
            return (99 + adancime)
        elif t_final == self.__class__.JMIN:
            return (-99 - adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return self.fct_euristica()

    def __str__(self):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7']
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        sir = "        0       1      2       3       4      5       6     "
        sir += "   \n     _____________________________________________________\n"
        for ind, i in enumerate(self.matr):
            sir += numbers[ind] + '|'
            for j in i:
                if j == '#':
                    sir += "   |  " + " "
                else:
                    sir += "   |  " + j
            sir += "   \n     _____________________________________________________\n"
        return sir
        #########################33
        # sir = ''
        # for nr_col in range(self.NR_COLOANE):
        #     sir += str(nr_col) + ' '
        # sir += '\n'
        #
        # for lin in range(self.NR_LINII):
        #     k = lin * self.NR_COLOANE
        #     sir += (" ".join([str(x) for x in self.matr[k: k + self.NR_COLOANE]]) + "\n")
        # return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari(self):
        l_mutari = self.tabla_joc.mutari(self.j_curent)
        juc_opus = self.jucator_opus()
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    if alpha > beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')

        for mutare in stare.mutari_posibile:
            # calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if (alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')

        for mutare in stare.mutari_posibile:

            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent > stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if (beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break
    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    # TO DO:
    # de adagat parametru "pozitie", ca sa nu verifice mereu toata tabla,
    # ci doar linia, coloana, 2 diagonale pt elementul nou, de pe "pozitie"

    final = stare_curenta.tabla_joc.final()
    if (final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu G sau cu R? ").upper()
        if (Joc.JMIN in ['G', 'R']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie G sau R.")
    Joc.JMAX = 'R' if Joc.JMIN == 'G' else 'G'

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'G', ADANCIME_MAX)

    linie = -1
    coloana = -1
    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            raspuns_valid = False
            while not raspuns_valid:
                try:
                    coloana = int(input("coloana = "))

                    if (coloana in range(0, Joc.NR_COLOANE)):
                        linie = Joc.NR_LINII - 1
                        while linie >= 0:
                            if stare_curenta.tabla_joc.matr[linie][coloana] == Joc.GOL :
                                raspuns_valid = True
                                break
                            else:
                                linie -= 1


                        if linie < 0:
                            print("Toata coloana este ocupata.")
                    else:
                        print("Coloana invalida (trebuie sa fie un numar intre 0 si {}).".format(Joc.NR_COLOANE - 1))

                except ValueError:
                    print("Coloana trebuie sa fie un numar intreg.")

            # dupa iesirea din while sigur am valida coloana
            # deci pot plasa simbolul pe "tabla de joc"
            stare_curenta.tabla_joc.matr[linie][coloana] = Joc.JMIN

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()
# connect4_Minimax_AlphaBeta.py
# Displaying
# connect4_Minimax_AlphaBeta.py.