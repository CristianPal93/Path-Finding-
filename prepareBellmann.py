
from SdaProiect import Bellmann_Ford
from SdaProiect.Bellmann_Ford import *
l=[]
lm=[]
def addNode(numeNod):
    l.append(Varf(numeNod))

def getVarf(l,nume):
    for i in l:
        if i.nume==nume:
            return i

def addMuchi(data,varfA,varfB):
    var=getVarf(l,varfA)
    var1=getVarf(l,varfB)
    lm.append(Muchie(data,var,var1))


def go(start,stop):
    start1=getVarf(l,start)
    stop1=getVarf(l,stop)
    p = PrePare(l, lm, start1, stop1)
    rez=p.calc()
    return rez


if __name__=='__main__':
    # a = Varf('A')
    # b = Varf('B')
    # c = Varf('C')
    # d = Varf('D')
    # l=[]
    # l.append(a)
    # l.append(b)
    # l.append(c)
    # l.append(d)
    #
    # m1 = Muchie(3, a, b)
    # m2 = Muchie(5, b, d)
    # m3 = Muchie(7, a, d)
    # m4 = Muchie(4, a, c)
    # lm = []
    # lm.append(m1)
    # lm.append(m2)
    # lm.append(m3)
    # lm.append(m4)
    # start='A'
    # stop='D'
    # p=PrePare(l,lm,start,stop)
    # p.calc()

  addNode('A')
  addNode('B')
  addNode('C')
  addNode('D')

  #
  #
  addMuchi(3,'A','B')
  addMuchi(3,'A','C')
  addMuchi(3,'A','D')
  addMuchi(3,'B','D')
  rez=go('A','B')
  print(rez)


# alg
# nod1=Varf("SF")
# nod2=Varf("NY")
# nod3=Varf("LA")
# nod4=Varf("C")
# m1=Muchie(2, nod1, nod2)
# m2=Muchie(1, nod2, nod3)
# m3=Muchie(5, nod1, nod3)
# m4=Muchie(3, nod2, nod4)
#
# nod1.l_adiacente.append(m1)
# nod2.l_adiacente.append(m2)
# nod1.l_adiacente.append(m3)
# nod2.l_adiacente.append(m4)
# l_varf={nod1, nod2, nod3, nod4}
# alg.calcCaleIeftina(l_varf, nod1)
# alg.getCaleIeftina(nod4)