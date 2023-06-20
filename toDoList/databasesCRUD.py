from databases import databases

class CRUD(databases):
    def insertDB(self, schema, table, column, data):
        sql = f" INSERT INTO {schema}.{table}({column}) VALUES ('{data}');".format(schema=schema,table=table,column=column,data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("add success!")
        except Exception as e:
            print(" inser DB err", e)
    
    def readDB(self, schema, table, column, condition):
        sql = f" SELECT {column} from {schema}.{table} {condition};".format(column=column,schema=schema,table=table,condition=condition)
        print(f'sql:{sql}')
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            result = (" read DB err", e)

        return result

    def updateDB(self, schema, table, column, value, condition):
        sql = f" UPDATE {schema}.{table} SET {column}='{value}' WHERE {condition};".format(schema=schema,table=table,column=column,value=value,condition=condition)
        print(f'sql:{sql}')
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" update DB err",e)
        
    def deleteDB(self, schema, table, condition):
        sql = f" DELETE FROM {schema}.{table} where {condition};".format(schema=schema,table=table,condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("delete DB err", e)

if __name__ == "__main__":
    db = CRUD()
    db.insertDB(schema='', table='', column='', data='')
    print(db.readDB(schema='',table='',column=''))
    db.updateDB(schema='',table='',column='',value='',condition='')
    db.deleteDB(schema='',table='',condition='')