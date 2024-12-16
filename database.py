import sqlite3

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
    sql = """CREATE TABLE IF NOT EXISTS users (
          accountID integer primary key,         
          username text NOT NULL,
          password text NOT NULL,
          measurement_type bool NOT NULL,
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

def changePassword_sql(conn, newPassInput, userInput):
    cur = conn.cursor()
    cur.execute("""
            UPDATE users
            SET password = ?
            WHERE username = ?;
        """, (newPassInput, userInput))

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

def getLevel_sql(conn, username):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users""")
    records = cur.fetchall()
    for row in records: #checks each account
        if row[1] == username: #if the username matches
            current_level = row[5] #get the level from that account
    return current_level

def getPoints_sql(conn, username):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users""")
    records = cur.fetchall()
    for row in records: #checks each account
        if row[1] == username: #if the username matches
            current_points = row[6] #get the points from that account
    return current_points

#main subroutines
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

def verifyPassword_main(oldPasswordInput, username):
    try:
        with sqlite3.connect("user.db") as conn:
            verified = verifyAccount_sql(conn, username, oldPasswordInput) #sends user + pass to see if account exists
            return verified #returns that to main python file
    except sqlite3.Error as e:
        print(e)

def changePassword_main(newPassInput, username):
    try:
        with sqlite3.connect("user.db") as conn:
            changePassword_sql(conn, newPassInput, username) #sends user + pass to see if account exists
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

def getLevel_main(username):
    try:
        with sqlite3.connect("user.db") as conn:
            current_level = getLevel_sql(conn, username) #sends username and returns the level
            return current_level #returns to main python file
    except sqlite3.Error as e:
        print(e)

def getPoints_main(username):
    try:
        with sqlite3.connect("user.db") as conn:
            current_points = getPoints_sql(conn, username) #sends username and returns the points
            return current_points #returns to main python file
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
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

