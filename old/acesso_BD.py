__author__='AlVictor'

import pyodbc

strCnx = pyodbc.connect("Driver={SQL Server};"
                            "Server=wadb02.webaula.dc;"
                                "Database=waControlesAutomatizadosCGE;"
                                    "uid=alexandre;pwd=Balao#13") #"Integrated Security=SSPI")
cursor = strCnx.cursor()
cursor.execute("SELECT TOP 10 * FROM TB_BASE_FTP;") 
row = cursor.fetchone() 
while row: 
    print (row[0],row[1])
    row = cursor.fetchone()
