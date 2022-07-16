import sqlite3
import pandas as pd

table1 = sqlite3.connect('Deuda.db')

cursor_obj = table1.cursor()

table = """ CREATE TABLE Deudas (Codigo VARCHAR(255), Servicio VARCHAR(255), Fecha VARCHAR(255), Precio VARCHAR(255)); """

cursor_obj.execute(table)

q=1
while (q==1):
    print("ingrese servicio: ")
    row2=input()
    print("ingrese fecha: ")
    row3=input()
    print("ingrese precio: ")
    row4=input()
    
    sqlite_insert_with_param = """INSERT INTO Deudas (codigo, servicio, fecha, precio) VALUES (?, ?, ?, ?)"""
    data_tuple = (row1,row2,row3,row4)
    cursor_obj.execute(sqlite_insert_with_param, data_tuple)
    table1.commit()
    q=int(input())
    
cursor_obj.close()

