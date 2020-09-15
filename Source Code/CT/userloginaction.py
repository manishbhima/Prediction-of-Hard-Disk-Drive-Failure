import sqlite3


class UserLoginCheck:

    def datacheck(self,uid,pwd):
        if uid == "" or pwd == "":
            return True
        else:
            return False
    @staticmethod
    def logincheck(uid,pwd):
        conn = sqlite3.connect('device.db')
        print("select name from users where email='"+uid+"' and pwd='"+pwd+"' ")
        cursor=conn.execute("select name from users where email='"+uid+"' and pwd='"+pwd+"' ")
        print(cursor)
        print(type(cursor))

        if cursor.fetchone() is not None:
            print("login success")
            return True
        else:
            print("login fail")
            return False

        
        

#UserLoginCheck.logincheck("sajid@gmail.com","sajid")