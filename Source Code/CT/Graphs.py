import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys
import sqlite3

def view():
	

	conn = sqlite3.connect('device.db')
	print(conn)
	cursor = conn.execute("SELECT * from Accuracy")
	for row in cursor:
		rlist=row

	height=rlist
	bars = ( 'Naive Bayes', 'RandomForest','SVM' )
	y_pos = np.arange(len(bars))
	plt.bar(bars, height, color=['red', 'green', 'blue'])
	plt.xlabel('Algorithms')
	plt.ylabel('Accuracy')
	plt.title('Prediction Accuracy Analysis')
	plt.show()

if __name__ == "__main__":
	view()



