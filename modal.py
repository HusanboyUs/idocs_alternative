import sqlite3



class Modal:

    _logs = []

    def __init__(self):
        self.connection = sqlite3.connect('timedb.sqlite3')
        self.c = self.connection.cursor()
 
    def create_table(self):
        try:
            self.c.execute(""" CREATE TABLE times (
                    username text,
                    worked_time INTEGER,
                    date INTEGER        
            )""")
            self.connection.commit()
            Modal._logs.append('<<Table  times has been created!>>>')
        except:
            Modal._logs.append(Exception)
    
    def show_db(self):
        try:
            self.c.execute("SELECT * FROM times")
            items= self.c.fetchmany(3)
            return items
        except:
            Modal._logs.append(Exception)
        
    def insert_time(self,data):
        try:
            self.c.execute("INSERT INTO times VALUES (?, ?, ?)", data)
            self.connection.commit()
            Modal._logs.append('<<Data connection has been committed>>>')
        except:
             Modal._logs.append(Exception)

    def delete_time(self):
        pass

    def edit_time(self):
        pass








