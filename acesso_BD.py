__author__='AlVictor'

def method_name():
    import pyodbc
    return pyodbc

pyodbc = method_name()

strCnx = pyodbc.connect("Driver={SQL Server};"
                                             "Server=wasql02;"
                                             "Database=wa_bi_teste;"
                                             "Integrated Security=SSPI")
cursor = strCnx.cursor()
cursor.execute("SELECT DATAINICIO,DATAFIM FROM TB_DATAS;") 
row = cursor.fetchone() 
while row: 
    print (row[0],row[1])
    row = cursor.fetchone()
