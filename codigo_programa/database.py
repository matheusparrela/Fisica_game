import sqlite3 as sq

def conecta_database():

    database = sq.connect('database/fisicagame_database')
    return database


def select_questao(pergunta):
    #Seleciona questão no banco de dados

    db = conecta_database()
    cursor = db.cursor()

    cursor.execute(f'''SELECT COUNT(*) FROM perguntas WHERE id_pergunta = {pergunta}''')
    verifica = (cursor.fetchall())
    
    verifica = str(verifica[0])
    verifica = int(verifica[1:2])
    
    #Verifica se a questão existe
    if verifica == 0:
        return 1

    else:

        questao = []
        
        cursor.execute(f'''SELECT questao FROM perguntas WHERE id_pergunta = {pergunta}''')
        questao.append(cursor.fetchall())
        
        cursor.execute(f'''SELECT opcao_1 FROM perguntas WHERE id_pergunta = {pergunta}''')
        questao.append(cursor.fetchall())

        cursor.execute(f'''SELECT opcao_2 FROM perguntas WHERE id_pergunta = {pergunta}''')
        questao.append(cursor.fetchall())

        cursor.execute(f'''SELECT opcao_3 FROM perguntas WHERE id_pergunta = {pergunta}''')
        questao.append(cursor.fetchall())

        cursor.execute(f'''SELECT opcao_4 FROM perguntas WHERE id_pergunta = {pergunta}''')
        questao.append(cursor.fetchall())

        cursor.execute(f'''SELECT opcao_5 FROM perguntas WHERE id_pergunta = {pergunta}''')
        questao.append(cursor.fetchall())

        cursor.execute(f'''SELECT resposta FROM perguntas WHERE id_pergunta = {pergunta}''')
        questao.append(cursor.fetchall())

        return questao


def select_classificacao():

    db = conecta_database()
    cursor = db.cursor()
    
    classificacao = []
    i = 0  

    while i < 5:
        i = i + 1
        cursor.execute(f'''SELECT nome FROM classificacao WHERE id_posicao = {i}''')
        classificacao.append(cursor.fetchall())

    return classificacao


def select_pontuacao():
    
    db = conecta_database()
    cursor = db.cursor()
    
    #Seleciona nome e pontuação do banco de dados
    pontuacao = []
    i = 0
    
    while i < 5:
        i = i + 1
        cursor.execute(f'''SELECT pontuacao FROM classificacao WHERE id_posicao = {i}''')
        pontuacao.append(cursor.fetchall())

    print(pontuacao)
    return pontuacao


def update_classificacao(new_nome, new_pontuacao,):
    
    #Atualiza classificação no banco de dados
    i = 0
    db = conecta_database()
    cursor = db.cursor()

    print(new_nome)

    while i < 5:
        
        cursor.execute(f'''UPDATE classificacao SET pontuacao = {new_pontuacao[i]} WHERE id_posicao = {i+1}''')
        cursor.execute(f'''UPDATE classificacao SET nome = '{new_nome[i]}' WHERE id_posicao = {i+1}''')  
        i = i+1
    db.commit()
    return 0


def exclue_pergunta(pergunta):

    db = conecta_database()
    cursor = db.cursor()

    #Exclue pergunta do banco de dados
    cursor.execute(f'''DELETE FROM perguntas WHERE id_pergunta = {pergunta}''') 
    db.commit()

def adiciona_pergunta(id_pergunta, questao, opcao_1, opcao_2, opcao_3, opcao_4, opcao_5, resposta):
    
    db = conecta_database()
    cursor = db.cursor()

    #Adiciona questão ao banco de dados
    cursor.execute(f'''INSERT INTO perguntas (id_pergunta, questao, opcao_1, opcao_2, opcao_3, opcao_4, opcao_5, resposta) VALUES ({id_pergunta}, {questao}, {opcao_1}, {opcao_2}, {opcao_3}, {opcao_4}, {opcao_5}, {resposta})''') 

    db.commit()


def verifica_tamanho():

    db = conecta_database()
    cursor = db.cursor()

    #Retorna o tamanho da tabela perguntas
    cursor.execute(f'''SELECT COUNT(*) AS tamanho FROM perguntas''')
    tamanho = cursor.fetchall()

    tamanho = str(tamanho[0])
    return int(tamanho[1:3])


def reseta_perguntas():

    db = conecta_database()
    cursor = db.cursor()

    #Exclue pergunta do banco de dados
    cursor.execute(f'''DELETE FROM perguntas''') 
    db.commit()

    cursor.execute(f'''INSERT INTO perguntas(id_pergunta, questao, opcao_1, opcao_2, opcao_3, opcao_4, opcao_5, resposta) SELECT id_pergunta, questao, opcao_1, opcao_2, opcao_3, opcao_4, opcao_5, resposta FROM perguntas_backup''')

    db.commit()
    close_database()
    return 0


def reseta_classificacao():

    db = conecta_database()
    cursor = db.cursor()

    #Exclue pergunta do banco de dados
    cursor.execute(f'''DELETE FROM classificacao''') 
    db.commit()

    cursor.execute(f'''INSERT INTO classificacao(id_posicao, nome, pontuacao) SELECT id_posicao, nome, pontuacao FROM classificacao_backup''')
    db.commit()
    close_database()
    return 0


def close_database():
    
    conecta_database().close()
