class Node:
    def __init__(self,nume,data,parent=None):
        self.data=data
        self.nume=nume
        self.children=[]
        self.distance=[]
        self.parent=parent
    def addChildren(self,child,val):
        self.children.append(child)
        self.distance.append(val)
    def getData(self):
        return self.data
    def getName(self):
        return self.nume
    def getParent(self):
        if(self.parent is None):
            return None
        else:
            return self.parent
    def getOnlyChildren(self):
        return self.children
    def getChildren(self):
        return self.children,self.distance
    def heuristicFunction(self,heuristicValue):
        x=self.data+heuristicValue
        return x
    def getDistance(self):
        return self.distance
def getNodefromKey(dic,value):
    for key,val in dic.items():
        if value==val:
            return key
def removeFromDictionary(dic,val):
    del dic[val]
    return dic
def existaInVecinatate(l,goalNode):
    for i in l:
        if i.getName()==goalNode:
            return True
    return False
def verifyBox(l):
    return list(dict.fromkeys(l))

def createScore(numeNod,valoriNod,valori):
    for i in range(len(valoriNod)):
        if numeNod.getName()==valoriNod[i].getName():
            return valori[i]
        else:
            return 0
def Astart(startNodePoint,goalNode,list):
    listaTraseu=[]
    dicValori={}
    startScore=0
    for i in list:
        if startNodePoint==i.getName():
            startPoint=i
    listaTraseu.append(startPoint.getName())
    listaVecini,listaCosturi=startPoint.getChildren()
    if existaInVecinatate(listaVecini,goalNode)==True:
        listaTraseu.append(goalNode)
        return listaTraseu

    else:
        while startPoint.getName()!=goalNode:

            for i in range(len(listaVecini)):
                dicValori[listaVecini[i]] = listaVecini[i].heuristicFunction(listaCosturi[i] + startScore)
            pasUrmator = min(dicValori.values())
            if existaInVecinatate(listaVecini, goalNode) == True:
                listaTraseu.append(goalNode)
                return listaTraseu
            nodUrmator = getNodefromKey(dicValori, pasUrmator)
            startScore += createScore(nodUrmator, listaVecini, listaCosturi);
            listaTraseu.append(nodUrmator.getName())

            for i in list:
                if nodUrmator.getName() == i.getName():
                    startPoint = i
                    listaVecini, listaCosturi = i.getChildren()
            dicValori = removeFromDictionary(dicValori, nodUrmator)
            listaTraseu = verifyBox(listaTraseu)
    return listaTraseu