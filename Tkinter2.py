from tkinter import *
import sqlite3

# login window, checks user name & password with the db one. 
def loginwindow():
    def loginget():
        username, userpassword = userName.get(), userPassword.get()
        cursor.execute("""SELECT user_password FROM user_data WHERE user_name = :user_name""", {'user_name': userName.get()})
        connection_login.commit()
        if username != "" or userpassword !="":
            info = cursor.fetchall()
            try:
                db_password = ''.join(info[0])
                error_check = True
            except IndexError:
                error_message = Label(logInWindow, text = "Username or password incorrect", fg = "red").grid(row = 3, columnspan = 2)
                error_check = False
            if error_check == True:
                if db_password == userpassword:
                    logInWindow.destroy()
                    menuWindow(username)
                else:
                    error_message = Label(logInWindow, text = "Username or password incorrect", fg = "red").grid(row = 3, columnspan = 2)
    def destroy():
        logInWindow.destroy()
        registerWindow()
    def return_login(event):
        loginget()
    logInWindow = Tk()
    logInWindow.title("Snake")
    logInWindow.resizable(False, False)
    title = Label(logInWindow, text = "Log In").grid(row = 0, columnspan = 2)
    userNameLabel = Label(logInWindow, text = "Username").grid(row = 1, column = 0)
    userPasswordLabel = Label(logInWindow, text = "Password").grid(row = 2, column = 0)
    userName = Entry(logInWindow)
    userName.grid(row = 1, column = 1)
    userPassword = Entry(logInWindow, show="*")
    userPassword.grid(row = 2, column = 1)
    loginButton = Button(logInWindow, text = "    Log in    ", command = loginget).grid(row = 4, column = 0)
    registerButton = Button(logInWindow, text = "        Registration        ", command = destroy).grid(row = 4, column = 1)
    logInWindow.bind("<Return>", return_login)
    logInWindow.mainloop()

def registerWindow():
    def destroy():
        RegisterWindow.destroy()
        loginwindow()
    def registration():
        username, userpassword, checkuserpassword = userName.get(), userPassword.get(), userPasswordCheck.get()
        if username != "" and userpassword != "":
            if userpassword == checkuserpassword:
                try:
                    cursor.execute("""INSERT INTO user_data VALUES (:user_name, :user_password, :high_score )""",{'user_name': username,'user_password': userpassword, 'high_score': 0})
                    connection_login.commit()
                    error_check = True
                except sqlite3.IntegrityError:
                    error_message = Label(RegisterWindow, text = "Username already exists", fg = "red").grid(row = 4, columnspan = 2)
                    error_check = False
                if error_check == True:
                    destroy()
            else:
                no_match_message = Label(RegisterWindow, text = "Passwords do not match", fg = "red").grid(row = 4, columnspan = 2)
                #cursor.execute("INSERT INTO user_data VALUES (:user_name, :user_password, :high_score )",{'user_name': username,'user_password': userpassword, 'high_score': 0})
                #connection_login.commit()
    RegisterWindow = Tk()
    RegisterWindow.title("Snake")
    RegisterWindow.resizable(False, False)
    title = Label(RegisterWindow, text = "Registration").grid(row = 0, columnspan = 2)
    userNamelabel = Label(RegisterWindow, text = "Username").grid(row = 1, column = 0)
    userPasswordlabel = Label(RegisterWindow, text = "Password").grid(row = 2, column = 0)
    userPasswordChecklabel = Label(RegisterWindow, text = "Password check").grid(row = 3, column = 0)
    userName = Entry(RegisterWindow)
    userName.grid(row = 1, column = 1)
    userPassword = Entry(RegisterWindow, show="*")
    userPassword.grid(row = 2, column = 1)
    userPasswordCheck = Entry(RegisterWindow, show="*")
    userPasswordCheck.grid(row = 3, column = 1)
    LogInButton = Button(RegisterWindow, text = "        Login        ", command = destroy).grid(row = 5, column = 0)
    RegisterButton = Button(RegisterWindow, text = "            Register            ", command = registration).grid(row = 5, column = 1)
    RegisterWindow.mainloop()

def menuWindow(UserName):
    def rules():
        MenuWindow.destroy()
        ruleWindow(UserName)
    def game():
        MenuWindow.destroy()
        try1 = Gamemode()
        try1.Tkinter_window()
        #test1()
    def highscore():
        MenuWindow.destroy()
        highscoreWindow(UserName)
    MenuWindow = Tk()
    MenuWindow.title("Snake")
    MenuWindow.resizable(False, False)    
    nameLabel = Label(MenuWindow, text = "Welcome "+UserName).pack()
    startGameButton = Button(MenuWindow, text = "Start Game", command = game).pack(fill=BOTH, side = TOP)
    rulesButton = Button(MenuWindow, text = "Rules", command = rules).pack(fill=BOTH)
    highScore = Button(MenuWindow, text = "High Score", command = highscore).pack(fill=BOTH, side = BOTTOM)
    MenuWindow.mainloop()

def ruleWindow(UserName):
    def destroy():
        RuleWindow.destroy()
        menuWindow(UserName)
    RuleWindow = Tk()
    RuleWindow.title("Snake")
    RuleWindow.resizable(False, False)    
    ruleLabel = Label(RuleWindow, text = "The rules:\n The snake starts at the center of the board, moving north (upward). \n The snake moves at a constant speed. \n The snake moves only north, south, east, or west. \n Apples appear at random locations. \n There is always exactly one apple visible at any given time. \n When the snake eats (runs into) an apple, it gets longer. \n The game continues until the snake dies. \n A snake dies by by running into its own tail. \n The final score is based on the number of apples eaten by the snake.").pack()
    MenuWindowButton = Button(RuleWindow, text = "Menu", command = destroy).pack()
    RuleWindow.mainloop()

def highscoreWindow(UserName):
    def destroy():
        HighScoreWindow.destroy()
        menuWindow(UserName)
    HighScoreWindow = Tk()
    HighScoreWindow.title("Snake")
    HighScoreWindow.resizable(False, False)
    HighScoreLabelTitle = Label(HighScoreWindow, text = "High Score Table").grid(row = 0, columnspan = 3)
    HighScoreLabelNameTitle = Label(HighScoreWindow, text = "Name").grid(row = 1, column = 1)
    HighScoreLabelScoreTitle = Label(HighScoreWindow, text = "Score").grid(row = 1, column = 2)
    MenuWindowButton = Button(HighScoreWindow, text = "Menu", command = destroy).grid(row = 11, columnspan = 3)
    cursor.execute("""SELECT high_score, user_name FROM user_data ORDER By high_score DESC LIMIT 10""")
    raw_highscore = cursor.fetchall()
    print(raw_highscore)
    for count in range(10):
        highscore_conversion = raw_highscore[count]
        print(highscore_conversion)
        HighScoreLabelText = Label(HighScoreWindow, text = count+1).grid(row = count+2, column = 0)
        HighScoreLabelName = Label(HighScoreWindow, text = highscore_conversion[1]).grid(row = count+2, column = 1)
        HighScoreLabelScore = Label(HighScoreWindow, text = highscore_conversion[0]).grid(row = count+2, column = 2)
        
    HighScoreWindow.mainloop()

class Gamemode(): 
    def __init__(self):
        self.map_size = 0
        self.gameModeSelection = Tk()

    def state_change(self):
        if self.map_size == 1: self.smallgame, self.mediumgame, self.biggame = "active", "disabled", "disabled"
        elif self.map_size == 2: self.smallgame, self.mediumgame, self.biggame = "disabled", "active", "disabled"
        elif self.map_size == 3: self.smallgame, self.mediumgame, self.biggame = "disabled", "disabled", "active"
        elif self.map_size == 4: self.smallgame, self.mediumgame, self.biggame, self.customgame = "disabled", "disabled", "disabled", "disabled"
        elif self.map_size == 0: self.smallgame, self.mediumgame, self.biggame, self.customgame = "active", "active", "active", "active"
        #self.smallGameCheck.config(state = self.smallgame)
        self.smallGameCheck.deselect()
        self.mediumGameCheck.config(state = self.mediumgame)
        self.bigGameCheck.config(state = self.biggame)
        self.customGameCheck.config(state = self.customgame)
             
        
    def small_game(self):
        if self.map_size == 0: self.map_size = 1
        elif self.map_size == 1: self.map_size = 0
        self.state_change()

    def medium_game(self):
        if self.map_size == 0: self.map_size = 2
        elif self.map_size == 2: self.map_size = 0 
        self.state_change()

    def big_game(self):
        if self.map_size == 0: self.map_size = 3
        elif self.map_size == 3: self.map_size = 0 
        self.state_change()

    def classic_game(self):
        if self.map_size == 0: self.map_size, self.size = 4, (1080, 720)
        elif self.map_size == 4: self.map_size = 0
        self.state_change()

    def custom_game(self):
        pass
    def start_game1(self):
        pass


    def Tkinter_window(self):
        self.classicGameCheck = Checkbutton(self.gameModeSelection, text = "Classic game?", command = self.classic_game)
        self.customGameCheck = Checkbutton(self.gameModeSelection, text = "Custom game?", command = self.custom_game)
        self.beginGameButton = Button(self.gameModeSelection, text = "Start Game", command = self.start_game1).pack()
        self.bigGameCheck = Checkbutton(self.gameModeSelection, text = "Big Map", command = self.big_game)
        self.mediumGameCheck = Checkbutton(self.gameModeSelection, text = "Medium Map", command = self.medium_game)
        self.smallGameCheck = Checkbutton(self.gameModeSelection, text = "Small Map", command = self.small_game)
        self.classicGameCheck.pack()
        self.customGameCheck.pack()
        self.bigGameCheck.pack()
        self.mediumGameCheck.pack()
        self.smallGameCheck.pack()
        #self.gameModeSelection.mainloop()


connection_login = sqlite3.connect("user_data.db")
cursor = connection_login.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS user_data (user_name text, user_password text, high_score intiger)""")
cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS IDX_Login ON user_data(user_name, user_password)""")
loginwindow()
connection_login.close()
