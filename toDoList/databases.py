import psycopg2

class databases():
    def __init__(self):
        self.db = psycopg2.connect(host='localhost',
                                   dbname='todolist',
                                   user='postgres',
                                   password=1,
                                   port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cousor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()