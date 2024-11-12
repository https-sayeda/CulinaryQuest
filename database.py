import sqlite3

def createDatabase(filename):
    conn = None
    try:
        conn = sqlite3.connect(filename) #creates and connects the database file
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close() #closes the database when it is no longer in use

def createTable():
    sql = """CREATE TABLE IF NOT EXISTS users (
          accountID integer primary key,         
          username text NOT NULL,
          password text NOT NULL,
          measurement_type real NOT NULL,
          volume_level integer NOT NULL,
          current_level integer NOT NULL,
          current_points integer NOT NULL
          );"""
    #sql is used to create a table with the above rows
    try:
        with sqlite3.connect("user.db") as conn: #this statement closes the connection automatically
            cursor = conn.cursor() #cursor object created
            cursor.execute(sql) #iterates through the sql statement and executes them using the method
            conn.commit() #creates connection to the database
    except sqlite3.Error as e:
        print(e) #error displayed if it occurs

def addAccount_sql(conn, UserAccount):
    sql = """INSERT INTO users(username, password, measurement_type, volume_level, current_level, current_points)
            VALUES(?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, UserAccount) 
    conn.commit()
    return cur.lastrowid #returns the inserted id in the table using the lastrowid property of cursor

def validateUser_sql(conn, userInput):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users""") 
    records = cur.fetchall() #the total rows
    validate = True
    for row in records:#checks each row
        if row[1] == userInput: #if the username is in there
            validate = False #it's not validated
    return validate
        
def verifyAccount_sql(conn, userInput, passInput):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users""") 
    records = cur.fetchall() #the total rows
    verified = False
    for row in records:#checks each row
        if row[1] == userInput and row[2] == passInput: #if the user and pass match any of the account
            verified = True #if it does, then it's verified
    return verified

def addAccount_main(userInput, passInput):
    try:
        with sqlite3.connect("user.db") as conn:
            UserAccount = (userInput, passInput, True, 100, 1, 0)
            accountID = addAccount_sql(conn, UserAccount)
    except sqlite3.Error as e:
        print(e)

def validateUser_main(userInput):
    try:
        with sqlite3.connect("user.db") as conn:
            validated = validateUser_sql(conn, userInput) #sends username to check if valid
            return validated #returns that to main python file
    except sqlite3.Error as e:
        print(e)

def verifyAccount_main(userInput, passInput):
    try:
        with sqlite3.connect("user.db") as conn:
            verified = verifyAccount_sql(conn, userInput, passInput) #sends user + pass to see if account exists
            return verified #returns that to main python file
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    createDatabase("user.db")
    createTable()
