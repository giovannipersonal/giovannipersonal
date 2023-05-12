import pandas as pd
import numpy as np
#import DatabaseConnections as dc
import pyodbc as po


#sqlConnection = str(dc.SqlServerConnection('NTBK-BH4122','sandbox','esquilo','N0zes!'))
#sqlsrcconn = po.connect(sqlConnection)
connstr = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=NTBK-BH4122;DATABASE=sandbox;UID=esquilo;PWD=N0zes!;TrustServerCertificate=yes;'

#connect to SQLServer
with po.connect(connstr) as sqlconn:

    strSQL = 'SELECT DISTINCT \
                s1.Schema_Name+\'.\'+s1.Table_Name Source_table \
                ,s2.Schema_Name+\'.\'+s2.Table_Name destination_table \
                ,m.Source_Table_ID \
                ,m.Destination_Table_ID \
                FROM [metamart].[StageMap] m \
                    inner join [metamart].[StageTable] s1 on s1.Table_ID = m.Source_Table_ID \
                    inner join [metamart].[StageTable] s2 on s2.Table_ID = m.Destination_Table_ID'
    
    dfTable = pd.read_sql_query(strSQL,sqlconn)
    for index, tabrow in dfTable.iterrows():

        strSQL = 'SELECT [Map_ID] \
                ,s1.Schema_Name+\'.\'+s1.Table_Name Source_table \
                ,s2.Schema_Name+\'.\'+s2.Table_Name destination_table \
                ,[Destination_Table_ID] \
                ,coalesce([Source_Column],[Source_Expression]) sourcecolumn_expr \
                ,[Destination_Column] \
            FROM [metamart].[StageMap] m \
                inner join [metamart].[StageTable] s1 on s1.Table_ID = m.Source_Table_ID \
                inner join [metamart].[StageTable] s2 on s2.Table_ID = m.Destination_Table_ID  \
            WHERE m.Source_Table_ID=' + tabrow['Source_Table_ID'] +' and \
                m.Destination_Table_ID =  ' + tabrow['Destination_Table_ID']
        #load dataframe -- yet to dynamize table names and filter above query

        dfMap = pd.read_sql_query(strSQL,sqlconn)
        sqlheader = 'INSERT INTO ' + tabrow['destination_table'] + '('
        sqlBody = 'SELECT '
        sqlTail = 'From ' + tabrow['destination_table']


        # loop through the dataframe
        for index, row in dfMap.iterrows():
            sqlheader = sqlheader + row['Destination_Column'] + ','
            sqlBody
            #print(row['sourcecolumn_expr'], row['Destination_Column'])
print(sqlheader+' '+sqlBody + ' ' + sqlTail)
#output = print(dfSource.head())