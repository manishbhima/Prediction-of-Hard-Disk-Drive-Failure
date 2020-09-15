import sqlite3

class Signup:

	@staticmethod
	def store(name, email, ph, pwd):
		conn = sqlite3.connect('device.db')
		print(conn)
		
		try:

			conn.execute('''CREATE TABLE USERS
         	(EMAIL TEXT PRIMARY KEY     NOT NULL,
         	NAME           TEXT    NOT NULL,
         	PWD            TEXT     NOT NULL,
         	PH        CHAR(50));''')
			 
		except:
			print("Table Already Created")
		
		query = "insert into USERS values('"+email+"','"+name+"','"+pwd+"','"+ph+"')"		
		conn.execute(query)
		print(conn.commit())
		print ("Records created successfully");
		conn.close()

        





#Signup.store("sajid","sajid@gmail.com","923949832","sajid")

