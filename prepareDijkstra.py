from SdaProiect.Dijkstra import *
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
    addNode('A')
    addNode('B')
    addNode('C')
    addNode('D')

    addMuchi(3, 'A', 'B')
    addMuchi(8, 'A', 'C')
    addMuchi(2, 'B', 'D')
    addMuchi(7, 'B', 'D')
    rez = go('A', 'D')
    print(rez)