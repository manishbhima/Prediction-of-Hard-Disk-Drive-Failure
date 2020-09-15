# importing packages

import numpy.random as numrandom
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from sklearn import metrics



class RandomForest:
    def accuracy(self,file):
        datainput = pd.read_csv(file)

        x_train = datainput
        #x_train = datainput
        #print(x_train)
        y = datainput['failure']
        del datainput['failure']
        del datainput['sno']
        del datainput['serial_number']
        del datainput['capacity_bytes']

        # Split data into Test & Training Dataset
        # Testing data is 30% & Training data is 70%
        x_train, x_test, y_train, y_test = train_test_split(datainput, y, test_size=0.3)

        rf = RandomForestClassifier()
    # Training the model
        rf.fit(x_train, y_train)
    # Use the model on the Testing data
        predicted5 = rf.predict(x_test)
        print("RandomForest Accuracy Score:")
    # Calculate the accuracy
        accurcy = metrics.accuracy_score(y_test, predicted5)


      # Printing the accuracy
        print(accurcy)
        print('')
        print('')
    # Turns to % for graph representation.
        return accurcy

if __name__ == "__main__":
    rf = RandomForest()
    print(rf.accuracy("dataset.csv"))
