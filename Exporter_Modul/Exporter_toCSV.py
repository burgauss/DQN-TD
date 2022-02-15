import numpy as np
from numpy.core.numeric import normalize_axis_tuple
import pandas as pd

class Exporter_toCSV():
    def __init__(self):
        self.exporter_vals = None
        self.list_vals = []

    def create_csv(self, name, specification):
        if specification == 0:
            self.exporter_vals = pd.DataFrame(self.list_vals)   
            self.exporter_vals = pd.DataFrame.transpose(self.exporter_vals)
        elif specification == 1:
            #Do not tranpose
            self.exporter_vals = pd.DataFrame(self.list_vals)
            pass
        elif specification == 2:
            #Accomodate data for q_values
            # more parameter
            self.list_vals = self.getFormatQ_Values()
            self.exporter_vals = pd.DataFrame(self.list_vals)
        else:
            raise Exception("Is not a valid specification")
        
        #self.exporter_vals = pd.DataFrame.transpose(self.exporter_vals)
        #self.exporter_vals.to_csv(r'\Users\juanb\source\repos\Temporal_Difference\state_values.csv')
        self.exporter_vals.to_csv(name)

    def add_toCSV(self, V):
        self.list_vals = V
    
    def get_dataFrame(self):
        return self.exporter_vals

    def getFormatQ_Values(self):
        new_format = []
        for i in range(len(self.list_vals)):
            for j in range(len(self.list_vals[i])):
                new_format.append(self.list_vals[i][j])
        
        return new_format
                
