import sys
from random import randint
from time import time
import os
import tracemalloc
import os.path
import linecache
# from ConsumMemorie import display_top

class Varf: #Nod
    def __init__(self, n):
        self.nume=n
        self.vizitat=False #verificam daca am mai parcurs o data acest varf
        self.predecesor=None
        self.l_adiacente=[] #stocam muchii ce au acelasi varf
        self.minDist=sys.maxsize

class Muchie:
    def __init__(self, c, sv, vc):
        self.cost=c
        self.varf_start=sv
        self.varf_cautat=vc
    def getSv(self):
        return self.varf_start
    def getVc(self):
        return self.varf_cautat
class BellmanFord:
    areCiclu=False
    def __init__(self):
        pass

    def calcCaleIeftina(self, l_varf, l_muchie, varf_start):
        varf_start.minDist = 0

        for i in range(0, len(l_varf) - 1):
            for muchie in l_muchie:
                x = muchie.varf_start
                y = muchie.varf_cautat
                nouaDist = x.minDist + muchie.cost
                # print(nouaDist)

                if nouaDist < y.minDist:
                    y.minDist = nouaDist
                    y.predecesor = x

        for muchie in l_muchie:
            if self.areCicluMet(muchie):
                print("Ciclu negativ detectat")
                BellmanFord.areCiclu = True
                return

    def areCicluMet(self, muchie):
        if (muchie.varf_start.minDist + muchie.cost) < muchie.varf_cautat.minDist:
            return True
        else:
            return False

    def getCaleIeftina(self, varf_cautat):
        if not BellmanFord.areCiclu:
            pass
        #     print("Cea mai scurta cale spre nodul cautat este: ", varf_cautat.minDist)
        #
        # print("Calea cu costul cel mai mic este: ", varf_cautat.minDist)
        nod = varf_cautat
        lrez=[]
        while nod:
            # print("%s -> " % nod.nume, end='')
            lrez.append(nod.nume)
            nod = nod.predecesor  # parcurgem invers

        return lrez
class PrePare:
    def __init__(self,varfuri,muchi,start,stop):
        self.varfuri=varfuri
        self.muchi=muchi
        self.start=start
        self.stop=stop

    def calc(self):
       BF=BellmanFord()
       BF.calcCaleIeftina(self.varfuri,self.muchi,self.start)
       rez=BF.getCaleIeftina(self.stop)
       return rez




