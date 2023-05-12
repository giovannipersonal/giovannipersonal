

class SqlServerConnection:
    def __init__(self,server,database,username,password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
    def connecttoSql(self):
        connStr = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password + ';TrustServerCertificate=yes;'
        return str(connStr)