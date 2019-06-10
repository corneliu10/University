""" definirea problemei"""
import copy


class Nod:
    NR_LINII = 9
    NR_COLOANE = 9
    NR_LINII_BLOC = 3
    NR_COLOANE_BLOC = 3

    def __init__(self, info, h = 0):
        self.info = info
        self.h = h

    def __str__(self):
        sir = "\n"
        for ind, i in enumerate(self.info):
            if ind % 3 == 0:
                sir += '\n'
            sir += '\n'
            for indj, j in enumerate(i):
                if indj % 3 == 0 and indj != 0:
                    sir += '   '
                if j == '0':
                    sir += "  "
                else:
                    sir += ' ' + str(j)


        sir += "   \n"
        return sir


    def __repr__(self):
        sir = '\n'
        sir += str(self.info)
        return sir


class Graf:
    def __init__(self, nod_start):
        self.nod_start = Nod(list(nod_start))

    def scop(self, nod):
        # verificati daca jocul s-a incheiat, adica daca nu mai apare cifra 0 in matrice
        # ---------------------------------------
        for lin in range(Nod.NR_LINII):
            for col in range(Nod.NR_COLOANE):
                if nod.info[lin][col] == 0:
                    return False
        
        return True

    def calculeaza_h(self, nod_info):
        # numarul de linii, coloane, blocuri 3x3 care nu sunt completate
        # ---------------------------------------
        rez = 0
        # VERIFICA PE COLOANE
        # ---------------------------------------
        for col in range(Nod.NR_COLOANE):
            for lin in range(Nod.NR_LINII):
                if nod_info[lin][col] == 0:
                    rez += 1
                    break

        # ---------------------------------------
        # VERIFICA PE LINII
        # ---------------------------------------
        for lin in range(Nod.NR_LINII):
            for col in range(Nod.NR_COLOANE):
                if nod_info[lin][col] == 0:
                    rez += 1
                    break
        # ---------------------------------------
        # VERIFICA IN CADRANE
        # ---------------------------------------
        for lin in range(0, Nod.NR_LINII, Nod.NR_LINII_BLOC):
            for col in range(0, Nod.NR_COLOANE, Nod.NR_COLOANE_BLOC):
                for l in range(lin, lin + Nod.NR_LINII_BLOC):
                    for c in range(col, col + Nod.NR_COLOANE_BLOC):
                        if nod_info[l][c] == 0:
                            rez += 1

        return rez #nr_linii+nr_coloane+nr_intervale

    def get_topleft_corner(self, i, j):
        # returneaza elementul din stanga sus
        # a cadranului in care se afla elem (i, j)
        l_cadran = int(i / Nod.NR_LINII_BLOC)
        c_cadran = int(j / Nod.NR_COLOANE_BLOC)

        return (l_cadran * Nod.NR_LINII_BLOC, c_cadran * Nod.NR_COLOANE_BLOC)

    def valid(self, matrice, i, j, element):
        # linii
        for col in range(Nod.NR_COLOANE):
            if matrice[i][col] == element:
                return False
        # coloane
        for lin in range(Nod.NR_LINII):
            if matrice[lin][j] == element:
                return False
        # cadrane
        lin_cadran, col_cadran = self.get_topleft_corner(i, j)
        for lin in range(lin_cadran, lin_cadran + Nod.NR_LINII_BLOC):
            for col in range(col_cadran, col_cadran + Nod.NR_COLOANE_BLOC):
                if matrice[lin][col] == element:
                    return False
        
        return True

    def calculeaza_succesori(self, nod):
        # ! o copie a matricei de sudoku se face astfel:
        # matrice_copie = copy.deepcopy(nod.info)
        l_succesori = []
        for lin in range(Nod.NR_LINII):
            for col in range(Nod.NR_COLOANE):
                if nod.info[lin][col] == 0:
                    for val in range(1, 10):
                        if self.valid(nod.info, lin, col, val):
                            matrice_copie = copy.deepcopy(nod.info)
                            matrice_copie[lin][col] = val
                            h = self.calculeaza_h(matrice_copie)
                            l_succesori.append((Nod(matrice_copie, h), 1))

        return l_succesori

""" Sfarsit definire problema """

""" Clase folosite in algoritmul A* """

class NodCautare:
    def __init__(self, nod_graf, succesori=[], parinte=None, g=0, f=None):
        self.nod_graf = nod_graf
        self.succesori = succesori
        self.parinte = parinte
        self.g = g
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def drum_arbore(self):
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum

    def contine_in_drum(self, nod):
        nod_c = self
        while nod_c.parinte is not None:
            if nod.info == nod_c.nod_graf.info:
                return True
            nod_c = nod_c.parinte
        return False

    def __str__(self):
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        # return "("+str(self.nod_graf)+", parinte="+", f="+str(self.f)+", g="+str(self.g)+")";
        return str(self.nod_graf)


""" Algoritmul A* """

def debug_str_l_noduri(l):
    sir = ""
    for x in l:
        sir += str(x) + "\n"
    return sir

def get_lista_solutii(l):
    drum = []
    for x in l:
         drum.append(x.nod_graf.info)
    return drum

def in_lista(l, nod):
    for x in l:
        if x.nod_graf.info == nod.info:
            return x
    return None

def a_star(graf):
    rad_arbore = NodCautare(nod_graf=graf.nod_start)
    open = [rad_arbore]
    closed = []
    drum_gasit = False
    while len(open) > 0:
        nod_curent = open.pop(0)
        closed.append(nod_curent)
        if graf.scop(nod_curent.nod_graf):
            drum_gasit = True
            break
        l_succesori = graf.calculeaza_succesori(nod_curent.nod_graf)
        for (nod, cost) in l_succesori:
            if (not nod_curent.contine_in_drum(nod)):
                x = in_lista(closed, nod)
                g_succesor = nod_curent.g + cost
                f = g_succesor + nod.h
                if x is not None:
                    if (f < nod_curent.f):
                        x.parinte = nod_curent
                        x.g = g_succesor
                        x.f = f
                else:
                    x = in_lista(open, nod)
                    if x is not None:
                        if (x.g > g_succesor):
                            x.parinte = nod_curent
                            x.g = g_succesor
                            x.f = f
                    else:  # cand nu e nici in closed nici in open
                        nod_cautare = NodCautare(nod_graf=nod, parinte=nod_curent,
                                                 g=g_succesor);  # se calculeaza f automat in constructor
                        open.append(nod_cautare)

        open.sort(key=lambda x: (x.f, -x.g))

    if drum_gasit == True:
        print("-----------------------------------------")
        print("Drum de cost minim: \n" + debug_str_l_noduri(nod_curent.drum_arbore()))
    else:
        print("\nNu exista solutie!")
        return []

    return get_lista_solutii(nod_curent.drum_arbore())



def main():
    nod_start = [
                    [1,3,9,    2,5,8,  0,4,7],
                    [5,6,4,    3,1,7,  0,8,2],
                    [7,8,2,    6,4,9,  0,0,3],

                    [8,5,3,    9,7,2,  4,6,1],
                    [6,2,7,    1,8,4,  3,5,9],
                    [9,4,1,    5,6,3,  2,7,8],

                    [0,7,0,    4,0,0,  8,2,0],
                    [2,1,0,    8,0,6,  7,0,0],
                    [4,9,8,    7,2,0,  0,0,6]
                ]
    # SCOPUL este acela de a inlocui cifrele 0 cu cifre intre 1 si 9, astfel incat aceeasi cifra sa nu apara de doua ori
    # pe aceeasi linie, coloana, sau in interiorul unui bloc de 3x3

    problema = Graf(nod_start)
    return a_star(problema)


# Apel:
main()