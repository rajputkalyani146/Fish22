import config
import pickle
import json
import numpy as np
import pandas as pd

class FishSpecies:

    def __init__(self,Weight,Length1,Length2,Length3,Height,Width):
        self.model_File_Path = "Logistic_fishspecies_detection.pkl"        
        self.Weight = Weight
        self.Length1 =Length1
        self.Length2=Length2 
        self.Length3=Length3
        self.Height=Height
        self.Width=Width
       

    def load_saved_data(self):
        with open (self.model_File_Path, "rb") as f:
            self.lg_model = pickle.load(f)        
        print(self.lg_model) 

    def get_predicted_outcome(self):
        self.load_saved_data()
        Weight = self.Weight        
        Length1 = self.Length1
        Length2 = self.Length2
        Length3 = self.Length3
        Height = self.Height
        Width = self.Width
       
        test_array = np.array([Weight,Length1,Length2,Length3,Height,Width], ndmin = 2)
        print("this is array:",test_array)
        predicted_class = self.lg_model.predict(test_array)[0]
        print("Predicted Class : ", predicted_class)
        return predicted_class

if __name__ == "__main__":
    dbs = FishSpecies()


