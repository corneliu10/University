""" definirea problemei"""

class Nod:
    NR_MISIONARI = 3
    NR_CANIBALI = 3
    NR_LOCURI_BARCA = 2

    def __init__(self, info, h):
        '''
        info: [mal_barca in ['est', 'vest'],
                nr_Mis_Est, nr_Can_Est,
                nr_Mis_Vest, nr_Can_Vest]
        '''
        self.info = info
        self.h = 0

    def __str__(self):
        sir = ''
        if self.info[0] == 'est':
            sir += str("(vest -> {} Mis, {} Can, ............ Barca, {} Mis, {} Can <- est)\n" \
                       .format(self.info[3],self.info[4], self.info[1], self.info[2]))
        elif self.info[0] == 'vest':
            sir += str("(vest -> {} Mis, {} Can, Barca ............, {} Mis, {} Can <- est)" \
                       .format(self.info[3], self.info[4], self.info[1], self.info[2]))
        return sir

    def __repr__(self):
        sir = '\n'
        sir += str(self.info)
        return sir


class Graf:
    def __init__(self, nod_start, nod_scop):
        self.nod_start = Nod(list(nod_start), float('inf'))
        self.nod_scop = Nod(list(nod_scop), 0)

    def scop(self, nod):
        return nod.info == self.nod_scop.info

    def calculeaza_h(self, nod_info):
        # Folositi unul dintre cele doua apeluri de mai jos, in functie de euristica pe care vreti sa o testati
        return self.fct_euristica_h1(nod_info)
        # SAU
        # return self.fct_euristica_h2(nod_info)

    def fct_euristica_h1(self, nod_info):
        return (nod_info[1] + nod_info[2]) / Nod.NR_LOCURI_BARCA

    def fct_euristica_h2(self, nod_info):
        if nod_info[1] + nod_info[2] != 0:
            if nod_info[0] == 'est':
                return 2 * ((nod_info[1] + nod_info[2] - 2) / (Nod.NR_LOCURI_BARCA - 1)) + 1
            else:
                return 2 * ((nod_info[1] + nod_info[2] - 1) / (Nod.NR_LOCURI_BARCA - 1)) + 2
        else:
            return 0

    def muta_barca(self, nod_info, nr_mis, nr_can):
        if nod_info[0] == 'est':
            new_est_mis = nod_info[1] - nr_mis
            new_est_can = nod_info[2] - nr_can
            new_vest_mis = nod_info[3] + nr_mis
            new_vest_can = nod_info[4] + nr_can

            if (new_est_can <= new_est_mis or new_est_mis == 0) and (new_vest_can <= new_vest_mis or new_vest_mis == 0):
                nod_info[0] = 'vest'
                nod_info[1] -= nr_mis
                nod_info[3] += nr_mis
                nod_info[2] -= nr_can
                nod_info[4] += nr_can
            else:
                return None
        else:
            new_est_mis = nod_info[1] + nr_mis
            new_est_can = nod_info[2] + nr_can
            new_vest_mis = nod_info[3] - nr_mis
            new_vest_can = nod_info[4] - nr_can

            if (new_est_can <= new_est_mis or new_est_mis == 0) and (new_vest_can <= new_vest_mis or new_vest_mis == 0):
                nod_info[0] = 'est'
                nod_info[1] += nr_mis
                nod_info[3] -= nr_mis
                nod_info[2] += nr_can
                nod_info[4] -= nr_can
            else:
                return None

        return nod_info

    def calculeaza_succesori(self, nod):
        l_succesori = []

        for m in range(min(Nod.NR_LOCURI_BARCA, Nod.NR_MISIONARI) + 1):
            for c in range(min(Nod.NR_LOCURI_BARCA, Nod.NR_CANIBALI) + 1):        
                if m + c <= Nod.NR_LOCURI_BARCA and m + c >= 1:
                    nod_info_nou = self.muta_barca(nod.info.copy(), m, c)
                    if nod_info_nou != None:
                        h = self.calculeaza_h(nod_info_nou)
                        l_succesori.append((Nod(nod_info_nou, h), 1))

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
    """ added by Cristina .......... De modificat??"""
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
    #Nod.NR_MISIONARI = Nod.NR_CANIBALI = int(str(input("Nr misionari = Nr canibali = ")))
    #Nod.NR_LOCURI_BARCA = int(str(input("Nr locuri barca = ")))
    # print(Nod.NR_MISIONARI, Nod.NR_CANIBALI, Nod.NR_LOCURI_BARCA)

    # nod_start = ['est', 3, 3, 0, 0]
    # nod_scop = ['vest', 0, 0, 3, 3]
    nod_start = ['est', Nod.NR_MISIONARI, Nod.NR_CANIBALI, 0, 0]
    nod_scop = ['vest', 0, 0, Nod.NR_MISIONARI, Nod.NR_CANIBALI]

    problema = Graf(nod_start, nod_scop)
    #print(a_star(problema))
    return a_star(problema)


# Apel:
# main()