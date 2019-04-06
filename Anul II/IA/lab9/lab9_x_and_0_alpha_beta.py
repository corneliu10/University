import time

ADANCIME_MAX = 6

def elem_identice(lista):
    mt = set(lista)
    if (len(mt) == 1):
        castigator = list(mt)[0]
        if castigator != Joc.GOL:
            return castigator
        else:
            return False
    else:
        return False


class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 3
    JMIN = None
    JMAX = None
    GOL = '#'

    def __init__(self, tabla=None):
        self.matr = tabla or [self.__class__.GOL] * 9

    def final(self):
        rez = (elem_identice(self.matr[0:3])
               or elem_identice(self.matr[3:6])
               or elem_identice(self.matr[6:9])
               or elem_identice(self.matr[0:9:3])
               or elem_identice(self.matr[1:9:3])
               or elem_identice(self.matr[2:9:3])
               or elem_identice(self.matr[0:9:4])
               or elem_identice(self.matr[2:8:2]))
        if (rez):
            return rez
        elif self.__class__.GOL not in self.matr:
            return 'remiza'
        else:
            return False

    def mutari(self, jucator_opus):
        l_mutari = []
        for i in range(len(self.matr)):
            if self.matr[i] == self.__class__.GOL:
                matr_tabla_noua = list(self.matr)
                matr_tabla_noua[i] = jucator_opus
                l_mutari.append(Joc(matr_tabla_noua))
        return l_mutari

    # linie deschisa inseamna linie pe care jucatorul mai poate forma o configuratie castigatoare
    def linie_deschisa(self, lista, jucator):
        # obtin multimea simbolurilor de pe linie
        mt = set(lista)
        # verific daca sunt maxim 2 simboluri
        if (len(mt) <= 2):
            # daca multimea simbolurilor nu are alte simboluri decat pentru cel de "gol" si jucatorul curent
            if mt <= {self.__class__.GOL, jucator}:
                # inseamna ca linia este deschisa
                return 1
            else:
                return 0
        else:
            return 0

    def linii_deschise(self, jucator):
        return (self.linie_deschisa(self.matr[0:3], jucator)
                + self.linie_deschisa(self.matr[3:6], jucator)
                + self.linie_deschisa(self.matr[6:9], jucator)
                + self.linie_deschisa(self.matr[0:9:3], jucator)
                + self.linie_deschisa(self.matr[1:9:3], jucator)
                + self.linie_deschisa(self.matr[2:9:3], jucator)
                + self.linie_deschisa(self.matr[0:9:4], jucator)  # prima diagonala
                + self.linie_deschisa(self.matr[2:8:2], jucator))  # a doua diagonala

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
            return (self.linii_deschise(self.__class__.JMAX) - self.linii_deschise(self.__class__.JMIN))

    def __str__(self):
        sir = (" ".join([str(x) for x in self.matr[0:3]]) + "\n" +
               " ".join([str(x) for x in self.matr[3:6]]) + "\n" +
               " ".join([str(x) for x in self.matr[6:9]]) + "\n")

        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
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

    # Este intr-un interval invalid deci nu o mai procesez
    if alpha >= beta:
        return stare
    
    # Aflu mutarile posibile
    stare.mutari_posibile = stare.mutari()

    if stare.j_curent == Joc.JMAX:
        # Daca joaca max, scor curent ia o valoare foarte mica pentru inceput, apoi, mai jos, se actualizeaza cu scorul cel
        # mai avantajos al fiilor
        scor_curent = -1000

        # Pentru fiecare mutare din stare.mutari_posibile aplica alpha beta si actualizeaza scorul, starea aleasa si valoarea alpha
        # Daca intervalul devine invalid, intrerup aplicarea alpha beta pe restul mutarilor
        for mutare in stare.mutari_posibile:
            rez = alpha_beta(alpha, beta, mutare)
            if rez.scor > scor_curent:
                scor_curent = rez.scor
                stare.stare_aleasa = mutare
                if scor_curent > alpha:
                    alpha = scor_curent
                    if alpha >= beta:
                        break

    elif stare.j_curent == Joc.JMIN:
        # Daca joaca max, scor curent ia o valoare foarte mare pentru inceput, apoi, mai jos, se actualizeaza cu scorul cel
        # mai avantajos al fiilor
        scor_curent = 1000

        # Pentru fiecare mutare din stare.mutari_posibile aplica alpha beta si actualizeaza scorul, starea aleasa si valoarea alpha
        # Daca intervalul devine invalid, intrerup aplicarea alpha beta pe restul mutarilor
        for mutare in stare.mutari_posibile:
            rez = alpha_beta(alpha, beta, mutare)
            if rez.scor < scor_curent:
                scor_curent = rez.scor
                stare.stare_aleasa = mutare
                if scor_curent < beta:
                    beta = scor_curent
                    if alpha >= beta:
                        break

    stare.scor = stare.stare_aleasa.scor
    return stare


def afis_daca_final(stare_curenta):
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
    x = int(input("Introduceti 1 pt minimax sau 2 pt alpha-beta: "))
        
    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu x sau cu 0? ").lower()
        if (Joc.JMIN in ['x', '0']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie x sau 0.")
    Joc.JMAX = '0' if Joc.JMIN == 'x' else 'x'

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'x', ADANCIME_MAX)

    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            raspuns_valid = False
            while not raspuns_valid:
                try:
                    linie = int(input("linie="))
                    coloana = int(input("coloana="))

                    if (linie in range(0, 3) and coloana in range(0, 3)):
                        if stare_curenta.tabla_joc.matr[linie * 3 + coloana] == Joc.GOL:
                            raspuns_valid = True
                        else:
                            print("Exista deja un simbol in pozitia ceruta.")
                    else:
                        print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele 0,1,2).")

                except ValueError:
                    print("Linia si coloana trebuie sa fie numere intregi")

            # dupa iesirea din while sigur am valide atat linia cat si coloana
            # deci pot plasa simbolul pe "tabla de joc"
            stare_curenta.tabla_joc.matr[linie * 3 + coloana] = Joc.JMIN

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

            # setati sa se foloseasca algoritmul ales de la tastatura
            if x == 1:
                stare_actualizata = min_max(stare_curenta)
            elif x == 2:
                stare_actualizata = alpha_beta(-99, 99, stare_curenta)

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