import sqlite3

class AccuracyStore:

	@staticmethod
	def store(c,val):
		conn = sqlite3.connect('device.db')
		
		
		
		query = "update Accuracy set "+str(c)+"='"+str(val)+"' "
		print(query)		
		conn.execute(query)
		conn.commit()
		print ("Records created successfully");
		conn.close()

        




if __name__ == "__main__":
	AccuracyStore.store('rf',3)

