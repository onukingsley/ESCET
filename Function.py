import sqlite3
Db = sqlite3.connect('db.sql' , check_same_thread=False)
cursor =Db.cursor()
from passlib.hash import crypt16 as cr

def replacer(statement, old, new):
    return statement.replace(old, new)

def temp(temperature):
    return int(273 - temperature)

def checkempty(array):
    msg= False
    for i in array:
        if not i:
            msg = True
        return msg

def select( table, column= '*', condition=''):
    sql = f"""select {column} from {table} {condition}"""
    try:
       result = cursor.execute(sql).fetchall()
       print(result)
       print(sql)
    except Exception as err:
        print(sql)
        result=str(err)
    finally:
        return result


def verify(password, dbpassword):
    cr.verify(password,dbpassword)

def encrypt(password):
    cr.encrypt(password)