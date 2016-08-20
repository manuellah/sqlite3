import sqlite3

def Main():
    try:
        con = sqlite3.connect("test.db") #create connection
        cur = con.cursor() #creates a new cursor object which executes sql stmt for us
        cur.execute("SELECT SQLITE_VERSION()")

        data = cur.fetchone()

        print ("SQLITE version  "+str(data))
    except:
        if con:
            con.rollback()
    finally:        
        if con:    
            con.close()
    
    
if __name__ == "__main__":
    Main()
   