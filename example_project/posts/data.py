from . import SQL_Database

class info():
    data = SQL_Database.select()
    print(data)
    def __str__(self):
        print(self.data)
        return self.data