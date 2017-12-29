from django.shortcuts import render
from django.http import HttpResponse
import pyodbc,os

def index(request):

    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=D:\clouds\OneDrive\Projetos\_WEB\costureirasweb\colecao\Costureiras_db.mdb;'
        )
    oras =[x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]
    print(oras)
    # cnxn = pyodbc.connect(conn_str)
    # crsr = cnxn.cursor()
    # for table_info in crsr.tables(tableType='TABLE'):
        # print(table_info.table_name)
        
    # # cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=managermeta.mdb;')
    # access_database_file = 'D:\\clouds\\OneDrive\\Projetos\\_WEB\\costureirasweb\\colecao\Costureiras_db.mdb'       
    # connStr = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;' %access_database_file
    # cnxn = pyodbc.connect(connStr)
    # crsr = cnxn.cursor()
    # for table_info in crsr.tables(tableType='TABLE'):
        # print(table_info.table_name)
        
    # connStr = (
        # r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        # r"DBQ=C:\OneDrive\Daniel\OneDrive\Projetos\_WEB\costureirasweb\colecao\Costureiras_db.mdb;"
        # )
    # cnxn = pyodbc.connect(connStr)  
    print('Vamos meu filho')
    # conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\OneDrive\Daniel\OneDrive\Projetos\_WEB\costureirasweb\colecao\Costureiras_db.mdb;'
    # cnxn = pyodbc.connect(conn_str)
    # crsr = cnxn.cursor()
    # for table_info in crsr.tables(tableType='TABLE'):
        # print(table_info.table_name)
        
    # db_path = os.path.join('Costureiras_db.mdb')
    # odbc_connection_str = 'DRIVER={MDBTools};DBQ=%s'%db_path
    # connect=pyodbc.connect(odbc_connection_str)
    # cursor=connection.cursor()
    # query = 'select * from clientes'
    # cursor.execute(query)
    # rows= cursor.fetchall()
    # for row in rows:
        # print(row)
    return HttpResponse('Index')
    
    

  
    
    
    # db_path = os.path.join("path", "toyour", "db.mdb")
# odbc_connection_str = 'DRIVER={MDBTools};DBQ=%s;' % (db_path)
# connection = pyodbc.connect(odbc_connection_str)
# cursor = connection.cursor()

# query = "SELECT * FROM MSysObjects WHERE Type=1 AND Flags=0"
# cursor.execute(query)
# rows = cursor.fetchall()
# for row in rows:
    # print row
