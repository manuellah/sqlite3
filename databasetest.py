import sqlite3

def Main():
    con = sqlite3.connect("test.db") #create connection
    cur = con.cursor() #creates a new cursor object which executes sql stmt for us
    cur.execute("SELECT SQLITE_VERSION()")
    
    data = cur.fetchone()
    
    print ("SQLITE version  "+str(data))
    
    con.close()
    
    
if __name__ == "__main__":
    Main()
    
    
    
     
    
    