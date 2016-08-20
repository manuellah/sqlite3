import sqlite3

def Main():
    try:
        con = sqlite3.connect("test.db") #create connection
        cur = con.cursor() #creates a new cursor object which executes sql stmt for us
        cur.execute("CREATE TABLE pets(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO pets VALUES(1, 'cat',400)")
        cur.execute("INSERT INTO pets VALUES(2, 'dog',600)")
        cur.execute("INSERT INTO pets VALUES(3,'Dolly',450)")
        
        con.commit()
        
        cur.execute("SELECT * FROM pets")

        data = cur.fetchall()
        
        for row in data:
             print(row)
        
    except:
        if con:
            con.rollback()
            print("There was a problem with the SQL db")
    finally:        
        if con:    
            con.close()
    
    
if __name__ == "__main__":
    Main()
   