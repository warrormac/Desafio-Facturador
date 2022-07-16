import sqlite3
import pandas as pd
from datetime import date

def facturador(codigo,servicio,fecha,precio,total,estado):
    table1 = sqlite3.connect('Pagos.db')

    cursor_obj = table1.cursor()
    table = """ CREATE TABLE  if not exists Deudas (Codigo VARCHAR(255), Servicio VARCHAR(255), Fecha_Deuda VARCHAR(255), Fecha_Pago VARCHAR(255), Pagado VARCHAR(255), Precio_Restante VARCHAR(255), Estado VARCHAR(255) ); """

    cursor_obj.execute(table)

    sqlite_insert_with_param = """INSERT INTO Deudas (codigo, servicio, fecha_deuda, fecha_pago, pagado, precio_restante, estado) VALUES (?, ?, ?, ?, ?, ?, ?)"""
    data_tuple = (codigo,servicio,fecha,date.today() ,precio, total, estado)
    cursor_obj.execute(sqlite_insert_with_param, data_tuple)
    table1.commit()
    
    cursor_obj.close()