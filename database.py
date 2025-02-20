import sqlite3
import hashlib

#creating database / tables
def createDatabase(filename):
    conn = None
    try:
        conn = sqlite3.connect(filename) #creates and connects the database file
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close() #closes the database when it is no longer in use

def createTable_user():
    sql1 = """CREATE TABLE IF NOT EXISTS users (       
          username text primary key,
          password text NOT NULL,
          measurement_type bool NOT NULL,
          volume_level integer NOT NULL,
          current_level integer NOT NULL,
          current_points integer NOT NULL,
          disc_selected text NOT NULL,
          theme_selected text NOT NULL
          );"""
    sql2 = """CREATE TABLE IF NOT EXISTS shop (
          username text,
          disc1 bool NOT NULL,
          disc2 bool NOT NULL,
          disc3 bool NOT NULL,
          theme1 bool NOT NULL,
          theme2 bool NOT NULL,
          FOREIGN KEY (username) REFERENCES users(username)
          );"""
    #sql is used to create a table with the above rows
    try:
        with sqlite3.connect("user.db") as conn: #this statement closes the connection automatically
            cursor = conn.cursor() #cursor object created
            cursor.execute(sql1) #iterates through the sql statement and executes them using the method
            cursor.execute(sql2) 
            conn.commit() #creates connection to the database
    except sqlite3.Error as e:
        print(e) #error displayed if it occurs

def createTable_shop():
    #sql is used to create a table with the above rows
    try:
        with sqlite3.connect("shop.db") as conn: #this statement closes the connection automatically
            cursor = conn.cursor() #cursor object created
            #cursor.execute(sql) #iterates through the sql statement and executes them using the method
            #conn.commit() #creates connection to the database
    except sqlite3.Error as e:
        print(e) #error displayed if it occurs

def createTable_recipes():
    sql = """CREATE TABLE IF NOT EXISTS recipes (
          recipeName text primary key,         
          halal bool NOT NULL,
          vegetarian bool NOT NULL,
          vegan bool NOT NULL,
          difficulty text NOT NULL
          );"""
    #sql is used to create a table with the above rows
    try:
        with sqlite3.connect("recipes.db") as conn: #this statement closes the connection automatically
            cursor = conn.cursor() #cursor object created
            cursor.execute(sql) #iterates through the sql statement and executes them using the method
            conn.commit() #creates connection to the database
    except sqlite3.Error as e:
        print(e) #error displayed if it occurs

#sql subroutines
def addAccount_sql(conn, UserAccount, UserItems):
    sql1 = """INSERT INTO users(username, password, measurement_type, volume_level, current_level, current_points, disc_selected, theme_selected)
            VALUES(?,?,?,?,?,?,?,?)""" #the sql statements I want to use
    sql2 = """INSERT INTO shop(username, disc1, disc2, disc3, theme1, theme2)
            VALUES(?, ?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON") #we need to active the foreign key for sqlite3
    cur.execute(sql1, UserAccount) #inserts the sql statements and the lists
    cur.execute(sql2, UserItems)
    conn.commit()
    return cur.lastrowid #returns the inserted id in the table using the lastrowid property of cursor

def validateUser_sql(conn, userInput):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users""") 
    records = cur.fetchall() #the total rows
    validate = True
    for row in records:#checks each row
        if row[0] == userInput: #if the username is in there
            validate = False #it's not validated
    return validate
        
def verifyAccount_sql(conn, userInput, passInput):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users""") 
    records = cur.fetchall() #the total rows
    verified = False
    for row in records:#checks each row
        if row[0] == userInput and row[1] == passInput: #if the user and pass match any of the account
            verified = True #if it does, then it's verified
    return verified

#def changePassword_sql(conn, newPassInput, userInput):
 #   cur = conn.cursor()
  #  cur.execute("""
   #         UPDATE users
    #        SET password = ?
     #       WHERE username = ?;
      #  """, (newPassInput, userInput))

def changeData_sql(conn, data, newData, username):
    cur = conn.cursor()
    if data == "password": #checks what data is being changed
        newData = hashlib.sha256(newData.encode()).hexdigest()
        cur.execute("""
                UPDATE users
                SET password = ?
                WHERE username = ?;
            """, (newData, username)) 
        #the variables correspond to the question marks, sets the data to the new value for the correct account
    elif data == "measurement_type":
        cur.execute("""
                UPDATE users
                SET measurement_type = ?
                WHERE username = ?;
            """, (newData, username))
    elif data == "volume_level":
        cur.execute("""
                UPDATE users
                SET volume_level = ?
                WHERE username = ?;
            """, (newData, username))
    elif data == "current_level":
        cur.execute("""
                UPDATE users
                SET current_level = ?
                WHERE username = ?;
            """, (newData, username))
    elif data == "current_points":
        cur.execute("""
                UPDATE users
                SET current_points = ?
                WHERE username = ?;
            """, (newData, username))

def addRecipe_sql(conn, Recipe):
    sql = """INSERT INTO recipes(recipeName, halal, vegetarian, vegan, difficulty)
            VALUES(?,?,?,?,?)""" #inserts information into database
    cur = conn.cursor()
    cur.execute(sql, Recipe)
    conn.commit()

def searchRecipe_sql(conn, searchRecipe):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM recipes""") 
    records = cur.fetchall() #the total rows
    recipeFound = False
    recipeName = "None"
    for row in records: #checks each row
        if row[0] == searchRecipe.lower(): #if the recipe is in the database
            recipeFound = True #if it does, then it's found
            recipeName = str(row[0]) #tells us the name of the recipe that was found
        if searchRecipe == "":
            recipeFound = True
            recipeName = ""
    

    return recipeFound, recipeName 
    #returns the variables to searchRecipe_main() so it can be returned to mainScreen()

def filterRecipe_sql(conn, dietaryOption, difficultyOption, dietaryInput):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM recipes""") 
    records = cur.fetchall() #the total rows
    recipeFound = False
    recipeNames = []
    for row in records: #checks each row
        dietaryRequirements = [0, 0, 0] #sets to 0 each time a recipe is checked
        if dietaryInput: #checks if there's a dietary input
            for x in range(3): #goes through each dietary row in the database
                if row[x+1] == dietaryOption[x]: #checks if the recipe has the same requirements
                    dietaryRequirements[x] = dietaryOption[x] #if it does, added to another array
            if dietaryRequirements == dietaryOption: #compares to dietaryOption array and if they match
                if row[4] == difficultyOption or difficultyOption == "None":
                    recipeNames.append(row[0]) #adds it to recipeName to be returned to main program
                    recipeFound = True #sets that the recipe has been found to true
        elif row[4] == difficultyOption: #if the difficulty is correct
            recipeFound = True #sets to true: #if there is no dietaryInput but the difficulty is correct
            recipeNames.append(row[0])
    return recipeFound, recipeNames #returns to filterRecipe_main()

def getData_sql(conn, username, data):
    dataList = ["measurement_type", "volume_level", "current_level", "current_points", "disc_selected", "theme_selected"]
    #there are only 6 things i'll be retrieving from the user table in my database
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users""")
    records = cur.fetchall()
    for row in records: #checks each account
        if row[0] == username: #if the username matches
            for i in range(len(dataList)): #goes through the list
                if data == dataList[i]: #checks if what I want to retrieve matches the item in the list
                    returnedData = row[i+2] #if it does, store that value in a variable
    return returnedData #return to getData_main()

def getShopData_sql(conn, username, data):
    dataList = ["disc1", "disc2", "disc3", "theme1", "theme2"]
    #there are only 5 things i'll be retrieving from the shop table in my database
    cur = conn.cursor()
    cur.execute("""SELECT * FROM shop""")
    records = cur.fetchall()
    for row in records: #checks each account
        if row[0] == username: #if the username matches
            for i in range(len(dataList)): #goes through the list
                if data == dataList[i]: #checks if what I want to retrieve matches the item in the list
                    returnedData = row[i+1] #if it does, store that value in a variable
    return returnedData #return to getShopData_main()

#main subroutines
def addAccount_main(userInput, passInput):
    try:
        with sqlite3.connect("user.db") as conn:
            passInput = hashlib.sha256(passInput.encode()).hexdigest()
            #hashing algorithm for password
            UserAccount = (userInput, passInput, True, 100, 1, 0, "disc1", "theme1")
            UserItems = (userInput, True, False, False, True, False)
            addAccount_sql(conn, UserAccount, UserItems)
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
            print(passInput)
            passInput = hashlib.sha256(passInput.encode()).hexdigest()
            print(passInput)
            verified = verifyAccount_sql(conn, userInput, passInput) #sends user + pass to see if account exists
            return verified #returns that to main python file
    except sqlite3.Error as e:
        print(e)

def verifyPassword_main(oldPasswordInput, username):
    try:
        with sqlite3.connect("user.db") as conn:
            oldPasswordInput = hashlib.sha256(oldPasswordInput.encode()).hexdigest()
            verified = verifyAccount_sql(conn, username, oldPasswordInput) #sends user + pass to see if account exists
            return verified #returns that to main python file
    except sqlite3.Error as e:
        print(e)

def changeData_main(data, newData, username):
    try:
        with sqlite3.connect("user.db") as conn:
            changeData_sql(conn, data, newData, username) #sends user + pass to see if account exists
    except sqlite3.Error as e:
        print(e)

def addRecipe_main(recipeName, halal, vegetarian, vegan, difficulty):
    try:
        with sqlite3.connect("recipes.db") as conn:
            Recipe = (recipeName, halal, vegetarian, vegan, difficulty)
            recipeFound, recipeName = searchRecipe_sql(conn, recipeName) #searches if the recipe exists
            if recipeFound != True: #if it doesn't exist
                addRecipe_sql(conn, Recipe) #creates it, prevents the same recipe from being created twice
    except sqlite3.Error as e:
        print(e)

def searchRecipe_main(searchRecipe):
    try:
        with sqlite3.connect("recipes.db") as conn:
            recipeFound, recipeName = searchRecipe_sql(conn, searchRecipe) #sends recipe to see if it exists
            return recipeFound, recipeName #returns that to main python file
    except sqlite3.Error as e:
        print(e)

def filterRecipe_main(dietaryOption, difficultyOption, dietaryInput):
    try:
        with sqlite3.connect("recipes.db") as conn:
            recipeFound, recipeName = filterRecipe_sql(conn, dietaryOption, difficultyOption, dietaryInput) 
            #sends options to see if a recipe matching those requirements exist
            return recipeFound, recipeName #returns that to main python file
    except sqlite3.Error as e:
        print(e)

def getData_main(username, data):
    try:
        with sqlite3.connect("user.db") as conn:
            returnedData = getData_sql(conn, username, data) 
            #sends username and the data I want, and returns that data
            return returnedData #returns to main python file
    except sqlite3.Error as e:
        print(e)

def getShopData_main(username, data):
    try:
        with sqlite3.connect("user.db") as conn:
            returnedData = getShopData_sql(conn, username, data) 
            #sends username and the data I want, and returns that data
            return returnedData #returns to main python file
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    #createDatabase("shop.db")
    #createTable_shop()
    createDatabase("user.db")
    createTable_user()
    createDatabase("recipes.db")
    createTable_recipes()
    addRecipe_main("burger", True, True, True, "Easy")
    addRecipe_main("cake", True, True, False, "Medium")
    addRecipe_main("sushi", True, False, False, "Hard")
    addRecipe_main("cheese fondue", False, True, False, "Medium")
    addRecipe_main("croissant", True, True, False, "Hard")
    addRecipe_main("tofu", True, True, True, "Easy")

