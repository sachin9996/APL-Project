""" Class for each node and edge of the graph to handle properties  """

import aux_data #To be populated

class graphviz_node:

    def __init__(self,key,label,xlabel,color = '#FFFFFF', data=None):

        #Node properties (algorithm)
        self.key = key
        self.label = label
        self.xlabel = xlabel
        self.color = color

        #Node properties (UI)
        self.component = 0;
        self.index = 0
        self.lowest_link = 0
        self.is_onstack = 0

        #Anything else
        self.data = data

    def UI_properties(self):
        return {'label': self.label,'xlabel':self.xlabel,'fillcolor': self.color}

class graphviz_edge:

	def __init__(self, fro, to, color = 'black', style = 'solid'):

        #Edge properties (algorithm)
		self.fro = fro
		self.to = to

        #Edge properties (UI)
		self.color = color
		self.style = style

	def UI_properties(self):
		return {'color': self.color, 'style': self.style}
