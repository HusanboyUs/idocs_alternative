import sqlite3



class Modal:

    def __init__(self):
        logs=[]
        self.connection = sqlite3.connect('timedb.sqlite3')
        self.c = self.connection.cursor()
    

    def create_table(self):
        self.c.execute(""" CREATE TABLE times (
                username text,
                worked_time INTEGER,
                date INTEGER        
        )""")
        self.connection.commit()

    def show_db(self):
        self.c.execute("SELECT * FROM times")
        items= self.c.fetchmany(3)
        return items
        
    def insert_time(self,data):
        self.c.execute("INSERT INTO times VALUES (?, ?, ?)", data)
        self.connection.commit()

    def delete_time(self):
        pass

    def edit_time(self):
        pass

modal =Modal()
modal.show_db()






