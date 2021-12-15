import sqlite3
from sqlite3.dbapi2 import Cursor
import pygame

database = sqlite3.connect('database/fisicagame_database')
cursor = database.cursor()

def classificacao(janela, subfont, font, click_music, cursor, database):

    #Recebe os dados do banco de dados
    lista_nomes_recordes = []
    i = 1
    while i <= 5:
        
        cursor.execute('''SELECT nome FROM classificacao where id_posicao = '%d' ''' % i) 
        string_nome = str(cursor.fetchall())
        lista_nomes_recordes.append(string_nome[3:-4])
        i = i + 1

    lista_pontos_recordes = []
    i = 1
    while i <= 5:
        
        cursor.execute('''SELECT pontuacao FROM classificacao where id_posicao = '%d' ''' % i) 
        string_pontos = str(cursor.fetchall())
        lista_pontos_recordes.append(string_pontos[2:-3])
        i = i + 1


    #Carrega titulo da página
    text_config = font.render("Classificação", True, (0,0,0))
    pos_text = text_config.get_rect()
    pos_text.center = 400, 100

    #Carrega texto em voltar
    voltar_menu = subfont.render("Menu", True, (0,0,0))
    pos_voltar_menu = voltar_menu.get_rect()
    pos_voltar_menu.center = 75, 550

    #Carrega o nome e a pontuação da classificação
    #nomes
    lista_nomes_recordes[0] = lista_nomes_recordes[0].replace('\n', '')
    posicao_1_nome = subfont.render(lista_nomes_recordes[0], True, (0,0,0))
    pos_nome_1 = posicao_1_nome.get_rect()
    pos_nome_1.center = 200, 200

    lista_nomes_recordes[1] = lista_nomes_recordes[1].replace('\n', '')
    posicao_2_nome = subfont.render(lista_nomes_recordes[1], True, (0,0,0))
    pos_nome_2 = posicao_2_nome.get_rect()
    pos_nome_2.center = 200, 250

    lista_nomes_recordes[2] = lista_nomes_recordes[2].replace('\n', '')
    posicao_3_nome = subfont.render(lista_nomes_recordes[2], True, (0,0,0))
    pos_nome_3 = posicao_3_nome.get_rect()
    pos_nome_3.center = 200, 300

    lista_nomes_recordes[3] = lista_nomes_recordes[3].replace('\n', '')
    posicao_4_nome = subfont.render(lista_nomes_recordes[3], True, (0,0,0))
    pos_nome_4 = posicao_4_nome.get_rect()
    pos_nome_4.center = 200, 350

    lista_nomes_recordes[4] = lista_nomes_recordes[4].replace('\n', '')
    posicao_5_nome = subfont.render(lista_nomes_recordes[4], True, (0,0,0))
    pos_nome_5 = posicao_5_nome.get_rect()
    pos_nome_5.center = 200, 400

    #pontos
    lista_pontos_recordes[0] = lista_pontos_recordes[0].replace('\n', '')
    posicao_1_ponto = subfont.render(lista_pontos_recordes[0], True, (0,0,0))
    pos_ponto_1 = posicao_1_ponto.get_rect()
    pos_ponto_1.center = 700, 200

    lista_pontos_recordes[1] = lista_pontos_recordes[1].replace('\n', '')
    posicao_2_ponto = subfont.render(lista_pontos_recordes[1], True, (0,0,0))
    pos_ponto_2 = posicao_2_ponto.get_rect()
    pos_ponto_2.center = 700, 250

    lista_pontos_recordes[2] = lista_pontos_recordes[2].replace('\n', '')
    posicao_3_ponto = subfont.render(lista_pontos_recordes[2], True, (0,0,0))
    pos_ponto_3 = posicao_3_ponto.get_rect()
    pos_ponto_3.center = 700, 300

    lista_pontos_recordes[3] = lista_pontos_recordes[3].replace('\n', '')
    posicao_4_ponto = subfont.render(lista_pontos_recordes[3], True, (0,0,0))
    pos_ponto_4 = posicao_4_ponto.get_rect()
    pos_ponto_4.center = 700, 350

    lista_pontos_recordes[4] = lista_pontos_recordes[4].replace('\n', '')
    posicao_5_ponto = subfont.render(lista_pontos_recordes[4], True, (0,0,0))
    pos_ponto_5 = posicao_5_ponto.get_rect()
    pos_ponto_5.center = 700, 400

    #Carrega o texto de posição da classificação
    primeiro = subfont.render('1º - ', True, (0,0,0))
    pos_primeiro = primeiro.get_rect()
    pos_primeiro.center = 100, 200

    segundo = subfont.render('2º - ', True, (0,0,0))
    pos_segundo = segundo.get_rect()
    pos_segundo.center = 100, 250

    terceiro = subfont.render('3º - ', True, (0,0,0))
    pos_terceiro = terceiro.get_rect()
    pos_terceiro.center = 100, 300

    quarto = subfont.render('4º - ', True, (0,0,0))
    pos_quarto = quarto.get_rect()
    pos_quarto.center = 100, 350

    quinto = subfont.render('5º - ', True, (0,0,0))
    pos_quinto = quinto.get_rect()
    pos_quinto.center = 100, 400


    tela_classificacao = True

    #Loop de tela
    while tela_classificacao:

        pygame.display.flip()
        janela.fill((225,225,225))

        #Eventos da tela
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())

                if x > 50 and x < 100 and y > 536 and y < 550:
                    print("Voltar - Menu")
                    tela_classificacao = False
                    click_music.play()
                    return True

        #Desenha o título da página e o botão voltar para o menu
        janela.blit(text_config, pos_text)
        janela.blit(voltar_menu, pos_voltar_menu)

        #Desenha as posições na tela
        janela.blit(primeiro, pos_primeiro)
        janela.blit(segundo, pos_segundo)
        janela.blit(terceiro, pos_terceiro)
        janela.blit(quarto, pos_quarto)
        janela.blit(quinto, pos_quinto)

        #Desenha os nomes na tela
        janela.blit(posicao_1_nome, pos_nome_1)
        janela.blit(posicao_2_nome, pos_nome_2)
        janela.blit(posicao_3_nome, pos_nome_3)
        janela.blit(posicao_4_nome, pos_nome_4)
        janela.blit(posicao_5_nome, pos_nome_5)
        
        #Desenha a pontuação na tela
        janela.blit(posicao_1_ponto, pos_ponto_1)
        janela.blit(posicao_2_ponto, pos_ponto_2)
        janela.blit(posicao_3_ponto, pos_ponto_3)
        janela.blit(posicao_4_ponto, pos_ponto_4)
        janela.blit(posicao_5_ponto, pos_ponto_5)

    database.close()