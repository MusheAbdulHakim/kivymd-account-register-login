import sqlite3
import mysql.connector
import bcrypt


class SQLite:

    def __init__(self):
        self.db = sqlite3.connect('./db/assetmanager.db').cursor()
        self.create_users_table()

    def create_users_table(self):
        """ create users table """
        self.db.execute("CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY AUTOINCREMENT,name varchar(255) NOT NULL, username varchar(255) NOT NULL, email varchar(255) NOT NULL, password varchar(255) NOT NULL)")
        

    def create_user(self,name,username,email,password):
        self.db.execute("INSERT INTO users(name,username,email,password) VALUES(?,?,?,?)",(name,username,email,password))

    def delete(self,table,id):
        self.db.execute("DELETE FROM table=? WHERE id=?", (table,id))    

    def close_db_connection(self):
        self.db.close()



class MySQLdb:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="kivy_login"
            )
        self.cursor = self.db.cursor()
    
    
    def create_database(self):
        self.cursor.execute("CREATE DATABASE kivy_myasset")


    def show_databases(self):
        databases = self.cursor.execute("SHOW DATABASES")
        for x in self.cursor:
            print(x)

    def create_users_table(self):
        """ create users table """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY AUTO_INCREMENT,name varchar(255) NOT NULL, username varchar(255) NOT NULL, email varchar(255) NOT NULL UNIQUE, password varchar(255) NOT NULL)")

    def create_user(self,name,username,email,password):
        password_bytes = bytes(password,'utf-8')
        password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        sql = "INSERT INTO users (name, username,email,password) VALUES (%s, %s, %s, %s)"
        values = (name,username,email,password_hash)
        self.cursor.execute(sql,values)
        self.db.commit()

    def login(self,username,password):
        query = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(query,(username,))
        users = self.cursor.fetchall()
        for user in users:
            if bcrypt.checkpw(bytes(password,'utf-8'), bytes(user[-1],'utf-8')):
                print("it matches")
                return user
            else: 
                print("password doesn't match")

    def delete_user(self,id):
        sql = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(sql,(id,))
        self.db.commit()


        



