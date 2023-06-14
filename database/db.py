import sqlite3


class Datenbank:
    def __init__(self):
        self.__con__ = sqlite3.connect("./dame.db")
        self.__cur__ = self.__con__.cursor()
        self.__create_tables__()

    def __create_tables__(self):
        create_scoreboard = "CREATE TABLE IF NOT EXISTS Scoreboard (Username TEXT, Score INT)"
        self.__cur__.execute(create_scoreboard)
        self.__con__.commit()
        self.__cur__ = self.__con__.cursor()
        create_users = "CREATE TABLE IF NOT EXISTS Users(Username TEXT, Password TEXT)"
        self.__cur__.execute(create_users)
        self.__con__.commit()

    def login(self, username, password):
        sql = "SELECT Username, Password FROM Users WHERE Username = '" + username + "'"
        res = self.__cur__.execute(sql)
        username_check = res.fetchall()
        if any(username in sub_list for sub_list in username_check) and any(
                password in sub_list for sub_list in username_check):
            return True
        elif any(username in sub_list for sub_list in username_check) and any(
                password not in sub_list for sub_list in username_check):
            return False
        else:
            sql_username = "INSERT INTO Users(Username, Password) Values('" + username + "' , '" + password + "')"
            self.__cur__.execute(sql_username)
            self.__con__.commit()
            return True



# db = Datenbank()
# is_account_valid = db.login("username2", "password2")
# print(is_account_valid)
