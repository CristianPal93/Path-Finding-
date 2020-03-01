import tkinter
from tkinter import *
from tkinter import ttk, filedialog, simpledialog
from tkinter.messagebox import showerror
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class FileOpener:
    def __init__(self,path):
        self.path=path
        self.city_names_and_distance_to_dest=[]
        self.nr_routes=[]
        self.endPoint=[]
        self.city_names=[]
        self.lineDistance=[]
    def open(self):
        f=open(self.path,'r')
        for lines in f:
            if lines=='\n':
                break
            else:
                temp = lines.split(',')
                temp[1]=int(temp[1])
                self.city_names_and_distance_to_dest.append(temp)
                self.lineDistance.append(temp[1])
        for lines in f:
            if lines == '\n':
                break
            temp=lines.strip().split(',')
            temp[2]=int(temp[2])
            self.nr_routes.append(temp)

        for lines in f:
             self.endPoint.append(lines.strip())

        self.copyCities(self.city_names_and_distance_to_dest)
    def copyCities(self,citynames):
        for i in citynames:
            self.city_names.append(i[0])
    def get_cities(self):
        return self.city_names
    def get_name_dist(self):
        return self.nr_routes
    def getDest(self):
        return self.endPoint
    def getLineDistance(self):
        return self.lineDistance

class MainWindow:
    def __init__(self, master):

        self.master = master
        self.master.title("Path-Finding App")
        self.master.geometry('1024x800')
        self.graph = nx.DiGraph()
        self.f = plt.Figure(figsize=(5, 5), dpi=100)
        self.right_frame = FigureCanvasTkAgg(self.f,master)
        self.right_frame.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        self.right_frame.draw()
        self.right_frame._tkcanvas.pack(side=TOP)
        self.right_frame._tkcanvas.pack(side=TOP)
        self.openButton=Button(self.master,width=5,height=2,text="Open File",command=self.load_file_path)
        self.openButton.pack(side=LEFT,fill=BOTH,expand=True)
        self.AStar = Button(self.master,width=5,height=2, text="A*", command=self.Astar)
        self.AStar.pack(side=LEFT,fill=BOTH,expand=True)
        self.AStar.config(state='disabled')
        self.Dijkstra = Button(self.master, width=5, height=2, text="Dijkstra", command=self.Dijkstra)
        self.Dijkstra.pack(side=LEFT, fill=BOTH, expand=True)
        self.Dijkstra.config(state='disabled')
        self.Bellman_Ford = Button(self.master, width=5, height=2, text="Bellmann-Ford", command=self.Bellman_Ford)
        self.Bellman_Ford.pack(side=LEFT, fill=BOTH, expand=True)
        self.Bellman_Ford.config(state='disabled')
        self.about = Button(self.master, width=5, height=2, text="About", command=self.about_dialog)
        self.about.pack(side=LEFT, fill=BOTH, expand=True)
        self.close_button = Button(self.master,width=5,height=2, text="Close", command=master.quit)
        self.close_button.pack(side=LEFT,fill=BOTH,expand=True)

    def load_weights(self,cd):
        for i in cd:
            self.graph.add_edge(i[0],i[1],weight=i[2])
        # self.graph.add_edge('A', 'B', weight=10)
        # self.graph.add_edge('A', 'C', weight=5)
        # self.graph.add_edge('B', 'D', weight=1)
        # self.graph.add_edge('D', 'F', weight=10)
        # self.graph.add_edge('F', 'A', weight=5)
        # self.graph.add_edge('E', 'A', weight=50)

    def load_nodes(self,cities):
        for i in cities:
            self.graph.add_node(i)

        # self.graph.add_node('A')
        # self.graph.add_node('B')
        # self.graph.add_node('C')
        # self.graph.add_node('D')
        # self.graph.add_node('E')
        # self.graph.add_node('F')


    def load_file_path(self):
        self.fileName = filedialog.askopenfilename(filetypes =(("Template Files", "*.tplate"),("All Files","*.*")),title = "Choose a file")
        if self.fileName:
            try:
                self.Validation()
                self.file=FileOpener(self.fileName)
                self.file.open()
                cities=self.file.get_cities()
                city_dest=self.file.get_name_dist()
                self.load_nodes(cities)
                self.load_weights(city_dest)
                self.draw()

            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % self.fileName)
            return

    def Validation(self):
        self.Astar=Button()
        self.AStar.config(state='normal')
        self.Dijkstra.config(state='normal')
        self.Bellman_Ford.config(state='normal')

    def Astar(self):
        algo=" AStar"
        from SdaProiect import prepareAStar as prep
        endpoint = self.file.getDest()
        cities = self.file.get_cities()
        distance=self.file.getLineDistance()
        dialog = ChoiceDialog(self.master, 'Pick one (Using A* algorithm)',
                              text='Please, select starting point.. endpoint is ' + endpoint[0],
                              items=cities)
        a = dialog.selection
        l=[]
        for i in range(len(distance)):
            prep.createNode(l,cities[i],distance[i])
        cities_with_distance=self.file.get_name_dist()
        for i in cities_with_distance:
            prep.adaugareVecini(l,i[0],i[1],i[2])

        result=prep.getResults(l,a,endpoint[0])
        print(result)
        resultMesssage=result[0]
        for i in range(1,len(result)):
            resultMesssage+="->"
            resultMesssage+=result[i]
        print(resultMesssage)

        self.display_results(algo, resultMesssage)
    def Dijkstra(self):
        algo="Dijkstra"
        from SdaProiect import prepareDijkstra as prepD
        endpoint = self.file.getDest()
        cities = self.file.get_cities()
        cities_with_distance = self.file.get_name_dist()
        dialog = ChoiceDialog(self.master, 'Pick one (Using Dijkstra algorithm)',
                              text='Please, select starting point.. endpoint is ' + endpoint[0],
                              items=cities)
        a = dialog.selection
        for i in cities:
            prepD.addNode(i)
        for i in cities_with_distance:
            print(i[2], i[0], i[1])
            prepD.addMuchi(i[2], i[0], i[1])
        rez = prepD.go(a, endpoint[0])
        rez.reverse()
        resultMesssage = rez[0]
        for i in range(1, len(rez)):
            resultMesssage += "->"
            resultMesssage += rez[i]
        print(resultMesssage)
        self.display_results(algo, resultMesssage)

    def Bellman_Ford(self):
        print("Bellman_Ford!")
        from SdaProiect import prepareBellmann as prepB
        endpoint=self.file.getDest()
        cities=self.file.get_cities()
        cities_with_distance = self.file.get_name_dist()
        dialog = ChoiceDialog(self.master, 'Pick one (Using Bellmann-Ford algorithm)',
                              text='Please, select starting point.. endpoint is '+endpoint[0],
                              items=cities)
        a=dialog.selection
        for i in cities:
            prepB.addNode(i)
        for i in cities_with_distance:
            print(i[2],i[0],i[1])
            prepB.addMuchi(i[2],i[0],i[1])
        rez=prepB.go(a,endpoint[0])
        rez.reverse()
        print(rez)
        resultMesssage = rez[0]
        for i in range(1, len(rez)):
            resultMesssage += "->"
            resultMesssage += rez[i]
        print(resultMesssage)
        self.display_results(" Bellmann-Ford",resultMesssage)
    def draw(self):
        self.ax1 = self.f.add_subplot(211)
        pos = nx.spring_layout(self.graph,k=100,iterations=20,scale=2)
        nx.draw(self.graph, pos, with_labels=True,ax=self.ax1,nodesize=10,arrows=False,node_color='yellow',font_color='blue')
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels,ax=self.ax1,font_color='red')
        self.right_frame.draw()


    def display_results(self,algo,result):
        if result=="No Path Found":
            self.message="No Path Found!"
        else:
            self.message = "The optim path is: "+result
        tkinter.messagebox.showinfo(title='Results from'+algo, message=self.message, icon='info')

    def about_dialog(self):
        self.message="Created by Cristian Pal"
        tkinter.messagebox.showinfo(title='About Application', message=self.message, icon='info')

class ChoiceDialog(simpledialog.Dialog):
    def __init__(self, parent, title, text, items):
        self.selection = None
        self._items = items
        self._text = text

        super().__init__(parent, title=title)

    def body(self, parent):
        self._message = tkinter.Message(parent, text=self._text, aspect=400)
        self._message.pack(expand=1, fill=tkinter.BOTH)
        self._list = tkinter.Listbox(parent)
        self._list.pack(expand=1, fill=tkinter.BOTH, side=tkinter.TOP)
        for item in self._items:
            self._list.insert(tkinter.END, item)
        return self._list

    def validate(self):
        if not self._list.curselection():
            return 0
        return 1

    def apply(self):
        self.selection = self._items[self._list.curselection()[0]]


