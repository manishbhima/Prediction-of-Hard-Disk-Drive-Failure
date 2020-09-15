# importing packages

import numpy.random as numrandom
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from sklearn import metrics



class Prediction:
    def accuracy(self,file):
        """datainput = pd.read_csv(file)
        x_train = datainput"""
        #x_train = datainput
        #print(x_train)

        datainput = pd.read_csv("dataset.csv")
        testfile=file
        x_test=pd.read_csv(testfile)
        print(x_test)
        y = datainput['failure']
        del datainput['failure']
        del datainput['sno']
        del datainput['serial_number']
        del datainput['capacity_bytes']

        del x_test['sno']
        del x_test['serial_number']
        del x_test['capacity_bytes']



        # Split data into Test & Training Dataset
        # Testing data is 30% & Training data is 70%

        nn = RandomForestClassifier()
        # Training the model
        nn.fit(datainput, y)
        # Use the model on the Testing data
        predicted5 = nn.predict(x_test)

        return predicted5[0]

if __name__ == "__main__":
    rf = Prediction()
    print(rf.accuracy("Testing.csv"))
