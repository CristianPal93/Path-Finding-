from SdaProiect import Astar
def createNode(l,numeNod,distanta,parinte=None):
    Retea = Astar.Node
    if parinte is not None:
        r=Retea(numeNod,distanta,parinte)
    else:
        r=Retea(numeNod,distanta)
    l.append(r)
    return l
def creareNodParinte(l,numeNod):
    for i in l:
        if i.getName() == numeNod:
            return i
    return None

def adaugareVecini(l,numeNode,parinteNod,val):
    r=[]
    for i in l:
        if i.getName()== numeNode:
            r.append(i)
    for i in l:
        if i.getName()== parinteNod:
            r.append(i)
    r[0].addChildren(r[1],val)

def getNode(l,numeNod):
    for i in l:
        if i.getName()==numeNod:
            return i
    return None

def getResults(l,startPoin,endPoint):
    lista_finalaTraseu = Astar.Astart(startPoin,endPoint, l)
    return lista_finalaTraseu


if __name__=='__main__':
    l = []
    createNode(l, "Arad", 366)
    createNode(l, "Zerind", 374)
    createNode(l, "Timisoara", 329)
    createNode(l, "Oradea", 380)
    createNode(l, "Lugoj", 248)
    createNode(l, "Drobeta", 242)
    createNode(l, "Mehadia", 241)
    createNode(l, "Sibiu", 253)
    createNode(l, "Craiova", 160)
    createNode(l, "Ramnicul Valcea", 193)
    createNode(l, "Pitesti", 98)
    createNode(l, "Fagaras", 178)
    createNode(l, "Bucuresti", 0)
    createNode(l, "Giurgiu", 77)
    createNode(l, "Urziceni", 80)
    createNode(l, "Vaslui", 199)
    createNode(l, "Iasi", 226)
    createNode(l, "Neamt", 234)
    createNode(l, "Hirsova", 151)
    createNode(l, "Eforie", 161)
    adaugareVecini(l, "Arad", "Zerind", 75)
    adaugareVecini(l, "Arad", "Timisoara", 118)
    adaugareVecini(l, "Arad", "Sibiu", 140)
    adaugareVecini(l, "Zerind", "Oradea", 71)
    adaugareVecini(l, "Zerind", "Arad", 75)
    adaugareVecini(l, "Oradea", "Sibiu", 151)
    adaugareVecini(l, "Oradea", "Zerind", 71)
    adaugareVecini(l, "Timisoara", "Lugoj", 111)
    adaugareVecini(l, "Timisoara", "Arad", 118)
    adaugareVecini(l, "Lugoj", "Timisoara", 111)
    adaugareVecini(l, "Lugoj", "Mehadia", 60)
    adaugareVecini(l, "Mehadia", "Lugoj", 60)
    adaugareVecini(l, "Mehadia", "Drobeta", 75)
    adaugareVecini(l, "Drobeta", "Mehadia", 75)
    adaugareVecini(l, "Drobeta", "Craiova", 120)
    adaugareVecini(l, "Craiova", "Drobeta", 120)
    adaugareVecini(l, "Craiova", "Ramnicul Valcea", 146)
    adaugareVecini(l, "Craiova", "Pitesti", 138)
    adaugareVecini(l, "Ramnicul Valcea", "Craiova", 146)
    adaugareVecini(l, "Ramnicul Valcea", "Pitesti", 97)
    adaugareVecini(l, "Ramnicul Valcea", "Sibiu", 80)
    adaugareVecini(l, "Sibiu", "Ramnicul Valcea", 80)
    adaugareVecini(l, "Sibiu", "Fagaras", 99)
    adaugareVecini(l, "Sibiu", "Oradea", 151)
    adaugareVecini(l, "Sibiu", "Arad", 140)
    adaugareVecini(l, "Fagaras", "Sibiu", 99)
    adaugareVecini(l, "Fagaras", "Bucuresti", 211)
    adaugareVecini(l, "Pitesti", "Bucuresti", 101)
    adaugareVecini(l, "Pitesti", "Craiova", 138)
    adaugareVecini(l, "Pitesti", "Ramnicul Valcea", 97)
    adaugareVecini(l, "Bucuresti", "Pitesti", 101)
    adaugareVecini(l, "Bucuresti", "Giurgiu", 90)
    adaugareVecini(l, "Bucuresti", "Fagaras", 211)
    adaugareVecini(l, "Bucuresti", "Urziceni", 85)
    adaugareVecini(l, "Giurgiu", "Bucuresti", 90)
    adaugareVecini(l, "Urziceni", "Bucuresti", 85)
    adaugareVecini(l, "Urziceni", "Vaslui", 142)
    adaugareVecini(l, "Urziceni", "Hirsova", 98)
    adaugareVecini(l, "Vaslui", "Urziceni", 142)
    adaugareVecini(l, "Vaslui", "Iasi", 92)
    adaugareVecini(l, "Iasi", "Vaslui", 92)
    adaugareVecini(l, "Iasi", "Neamt", 87)
    adaugareVecini(l, "Neamt", "Iasi", 87)
    adaugareVecini(l, "Hirsova", "Urziceni", 98)
    adaugareVecini(l, "Hirsova", "Eforie", 86)
    adaugareVecini(l, "Eforie", "Hirsova", 86)
    print(l)
    # print(getResults(l,"Lugoj","Bucuresti"))