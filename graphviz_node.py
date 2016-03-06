""" Class for each node of the graph to handle it's UI properties """

class graphviz_node:

    def __init__(self,id,label,xlabel,color='#FFFFFF'):
        self.id=id
        self.label=label
        self.xlabel=xlabel
        self.color=color

    def properties(self):
        return {'label': self.label,'xlabel':self.xlabel,'fillcolor': self.color}

