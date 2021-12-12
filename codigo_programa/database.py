import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=omicron;"
    "Database=perguntas;"
)
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida!')