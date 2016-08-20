import sqlite3

def Main():
    try:
        con = sqlite3.connect("test.db") #create connection
        cur = con.cursor() #creates a new cursor object which executes sql stmt for us
        
        #cur.execute("CREATE TABLE pets(Pet_id INTEGER, Name TEXT, Price INT)")
        print("execute")
        cur.execute("INSERT INTO pets VALUES('cat',400)")
        cur.execute("INSERT INTO pets VALUES('dog',600)")
        cur.execute("INSERT INTO pets VALUES('Dolly',450)")
        
        con.commit()
        print("commit")
        cur.execute("SELECT * FROM pets")

        data = cur.fetchall()
        
        for row in data:
             print(row)
        
    except e:
        if con:
            con.rollback()
            print(e)
    finally:        
        if con:    
            con.close()
    
    
if __name__ == "__main__":
    Main()
   