import sys

def adauga(heap, el):
    # Adauga elementul in heap si mentine proprietatea lui
    heap.append(el)
    coboram(heap, 0, len(heap) - 1)

def sterge(heap):
    # Sterge cel mai mic element din heap si mentine proprietatea unui heap
    ultim = heap.pop()  # Daca coada este vida, avem eroare de indexare
    if heap:
        elem = heap[0]
        heap[0] = ultim
        ridicam(heap, 0)
        return elem
    return ultim

def heapify(x):
    # Transforma lista in heap
    n = len(x)
    for i in reversed(range(n // 2)):
        ridicam(x, i)

def coboram(heap, start, pos):
    nou = heap[pos]
    # Urmeaza calea spre radacina, coborand parintii
    while pos > start:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if nou < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = nou

def ridicam(heap, pos):
    final = len(heap)
    start = pos
    nou = heap[pos]
    # Ridicam nodul cel mai mic pana nu dam de frunza
    copil = 2 * pos + 1  # pozitia copilului cel mai din stanga
    while copil < final:
        # Setam 'copil' ca fiind nodul cu valoarea minima
        dr = copil + 1
        if dr < final and not heap[copil] < heap[dr]:
            copil = dr
        heap[pos] = heap[copil]
        pos = copil
        copil = 2 * pos + 1
    # Frunza la pozitia 'pos' nu exista; inseram un nou element si il ridicam pana la pozitia adecvata
    heap[pos] = nou
    coboram(heap, start, pos)

class Varf:  # Nod
    def __init__(self, n):
        self.nume = n
        self.vizitat = False  # verificam daca am mai parcurs o data acest varf
        self.predecesor = None
        self.l_adiacente = []  # stocam muchii ce au acelasi varf
        self.minDist = sys.maxsize

    def __cmp__(self, altVarf):
        return self.cmp(self.minDist, altVarf.minDist)  # comparam costul distantelor a doua varfuri

    def __lt__(self, altVarf):
        cost_crt = self.minDist
        altCost = altVarf.minDist
        return cost_crt < altCost

class Muchie:
    def __init__(self, c, sv, vc):
        self.cost=c
        self.varf_start=sv
        self.varf_cautat=vc
    def getSV(self):
        return self.varf_start

class Dijkstra:
    def __init__(self):
        pass

    def calcCaleIeftina(self, l_varf, varf_start):
        q = []  # initializam coada de prioritate (heap-ul)
        varf_start.minDist = 0
        adauga(q, varf_start)
        while len(q) > 0:
            crtVarf = sterge(q)  # extragem elementele din coada de prioritate
            for muchie in crtVarf.l_adiacente:
                x = muchie.varf_start
                y = muchie.varf_cautat
                nouDist = x.minDist + muchie.cost
                # print(nouDist)

                if nouDist < y.minDist:
                    y.predecesor = x
                    y.minDist = nouDist
                    # print(y.minDist)
                    adauga(q, y)

    def getCaleIeftina(self, varf_cautat):
        # print("Calea cu costul cel mai mic este: ", varf_cautat.minDist)
        rez=[]
        nod = varf_cautat
        while nod:
            # print("%s -> " % nod.nume, end='')
            rez.append(nod.nume)
            nod = nod.predecesor  # parcurgem invers
        return rez

class PrePare:
    def __init__(self,varfuri,muchi,start,stop):
        self.varfuri=varfuri
        self.muchi=muchi
        self.start=start
        self.stop=stop
    def addAdiacenta(self,listaMuchi,listaNoduri):
        for i in range(len(listaNoduri)):
            for j in range(len(listaMuchi)):
                if listaNoduri[i].nume==listaMuchi[j].varf_start.nume:
                    listaNoduri[i].l_adiacente.append(listaMuchi[j])



    def calc(self):
       BF=Dijkstra()
       self.addAdiacenta(self.muchi,self.varfuri)
       BF.calcCaleIeftina(self.varfuri,self.start)
       rez=BF.getCaleIeftina(self.stop)
       return rez



# if __name__=='__main__':
#     alg = Dijkstra()
#     nod1 = Varf("SF")
#     nod2 = Varf("NY")
#     nod3 = Varf("LA")
#     nod4 = Varf("C")
#     m1 = Muchie(2, nod1, nod2)
#     m2 = Muchie(1, nod2, nod3)
#     m3 = Muchie(5, nod1, nod3)
#     m4 = Muchie(3, nod2, nod4)
#
#     nod1.l_adiacente.append(m1)
#     nod2.l_adiacente.append(m2)
#     nod1.l_adiacente.append(m3)
#     nod2.l_adiacente.append(m4)
#
#     l_varf=[]
#     l_varf.append(nod1)
#     l_varf.append(nod2)
#     l_varf.append(nod3)
#     l_varf.append(nod4)
#     alg.calcCaleIeftina(l_varf, nod1)
#     alg.getCaleIeftina(nod4)