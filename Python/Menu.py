from ctypes import sizeof
from pickle import TRUE
from numpy import size
from Facturador import facturador
#from Recibo import generador
import sqlite3
import pandas as pd
from datetime import date


table1 = sqlite3.connect('Deuda.db')
cursor_obj = table1.cursor()

table2 = sqlite3.connect('Pagos.db')
cursor_obj2 = table2.cursor()

def pago(codigo,servicio, fecha,precio,total):
    
    sql_delete_query = """DELETE from Deudas where Codigo = ?"""
    cursor_obj.execute(sql_delete_query, (codigo,))
    table1.commit()
    
    #print(codigo, " ", servicio," ", fecha, " ", precio )
    estado="pendiente"
    if float(total)-float(precio) == 0:
        estado = "Pagado"

    
    facturador(codigo,servicio,fecha,precio, str((float(total)-float(precio))), estado)
   

def servicio():
    total=0
    print ("Deudas Pendiantes: ")
    table1 = sqlite3.connect('Deuda.db')
    cursor_obj = table1.cursor()
    cursor_obj.execute("SELECT * FROM Deudas")
    
    rows = cursor_obj.fetchall()

    for row in rows:
        print(row)
        
    while TRUE:  
        print("Ingrese 1. para ver Deudas nuevamente")
        print("Ingrese 2. para pagar Agua")
        print("Ingrese 3. para pagar Luz")
        print("Ingrese 4. para pagar Gas")
        print("Ingrese Q. para Salir")
        opcion=input()
        
        
        if opcion=="1":
            cursor_obj.execute("SELECT * FROM Deudas")
            rows = cursor_obj.fetchall()

            for row in rows:
                print(row)
                    
        if opcion == "2":
            cursor_obj.execute("SELECT * FROM Deudas Where Servicio = 'agua'")
            rows = cursor_obj.fetchall()

            for row in rows:
                print(row)
                total=total+float(row[3])
            print ("Total a Pagar: " , total)
                
            print("Ingrese Codigo al Pagar: ")    
            codigo=input()
            pago(codigo,"Agua del Sur S.A",row[2],row[3],total)
        
        if opcion == "3":
            cursor_obj.execute("SELECT * FROM Deudas Where Servicio = 'luz'")
            rows = cursor_obj.fetchall()

            for row in rows:
                print(row)
                total=total+float(row[3])
            print ("Total a Pagar: " , total)
                
            print("Ingrese Codigo al Pagar: ")    
            codigo=input()
            pago(codigo,"Luz del Sur S.A",row[2],row[3],total) 
                    
        if opcion == "4":
            cursor_obj.execute("SELECT * FROM Deudas Where Servicio = 'gas'")
            rows = cursor_obj.fetchall()

            for row in rows:
                print(row)
                total=total+float(row[3])
            print ("Total a Pagar: " , total)
                
            print("Ingrese Codigo al Pagar: ")    
            codigo=input()
            pago(codigo,"Gas del Sur S.A",row[2],row[3],total)
                
        if opcion == "Q":
            main()       
        total=0 
        
    
    
    
    

    


def tarjeta():
    print ("Ingrese numero de Tarjeta: ")
    num_tarj=input()
    while (len(num_tarj)>16 or len(num_tarj)<16):
        print("numero ingresado invalido, Ingrese numero de Tarjeta: ")
        num_tarj=input() 
    servicio()
    




def historial():
    print("Ingrese 1. para ver en orden de Fechas")
    print("Ingrese 2. para ver total pagado")
    print("Ingrese 3. para ver Transaccion de la Fecha")
    print("Ingrese Q. para Salir")
    
    opcion=input()
    if opcion=="1":
        
        cursor_obj2.execute("SELECT * FROM Deudas ORDER BY estado DESC")
        rows = cursor_obj2.fetchall()

        for row in rows:
            print(row)
    if opcion=="2":
        cursor_obj2.execute("SELECT SUM(pagado) FROM Deudas") 
        rows = cursor_obj2.fetchall()
        print(str(rows)) 
    if opcion=="3":
        cursor_obj2.execute("SELECT * FROM Deudas Where fecha_pago = ?", (date.today(),))
        rows = cursor_obj2.fetchall()
        for row in rows:
            print(row)
        
            
        
        

    
    

def main():    
    print ("Sistema de Pago")
    print("####### Ingresar Fecha ###########")
    print("Ingrese Metodo de Pago")
    print("Ingrese 1. para pagar con tarjeta de debito")
    print("Ingrese 2. para pagar con tarjeta de credito")
    print("Ingrese 3. para pagar con cash")
    print("Ingrese 4. para ver Hisatorial de Pagos")
    opcion=input()
    if opcion=="1" or opcion=="2":
        tarjeta()
    if opcion=="3":
        servicio()
    if opcion == "4":
        historial()
    
        
        
        
main()