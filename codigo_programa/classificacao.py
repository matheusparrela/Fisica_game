import pygame as py
import database as db


def classificacao(janela, subfont, font, click_music):

    #Abre o arquivo de nomes da classificação e passa para uma lista
    lista_nomes = []
    lista_nomes = db.select_classificacao()

    #Abre o arquivo de pontos da classificação e passa para uma lista
    lista_pontos = []
    lista_pontos = db.select_pontuacao()

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
    lista_nomes[0] = str(lista_nomes[0])[3:-4]
    posicao_1_nome = subfont.render(lista_nomes[0], True, (0,0,0))
    pos_nome_1 = posicao_1_nome.get_rect()
    pos_nome_1.center = 200, 200

    lista_nomes[1] = str(lista_nomes[1])[3:-4]
    posicao_2_nome = subfont.render(lista_nomes[1], True, (0,0,0))
    pos_nome_2 = posicao_2_nome.get_rect()
    pos_nome_2.center = 200, 250

    lista_nomes[2] = str(lista_nomes[2])[3:-4]
    posicao_3_nome = subfont.render(lista_nomes[2], True, (0,0,0))
    pos_nome_3 = posicao_3_nome.get_rect()
    pos_nome_3.center = 200, 300

    lista_nomes[3] = str(lista_nomes[3])[3:-4]
    posicao_4_nome = subfont.render(lista_nomes[3], True, (0,0,0))
    pos_nome_4 = posicao_4_nome.get_rect()
    pos_nome_4.center = 200, 350

    lista_nomes[4] = str(lista_nomes[4])[3:-4]
    posicao_5_nome = subfont.render(lista_nomes[4], True, (0,0,0))
    pos_nome_5 = posicao_5_nome.get_rect()
    pos_nome_5.center = 200, 400

    #pontos
    lista_pontos[0] = str(lista_pontos[0])[2:-3]
    posicao_1_ponto = subfont.render(lista_pontos[0], True, (0,0,0))
    pos_ponto_1 = posicao_1_ponto.get_rect()
    pos_ponto_1.center = 700, 200

    lista_pontos[1] = str(lista_pontos[1])[2:-3]
    posicao_2_ponto = subfont.render(lista_pontos[1], True, (0,0,0))
    pos_ponto_2 = posicao_2_ponto.get_rect()
    pos_ponto_2.center = 700, 250

    lista_pontos[2] = str(lista_pontos[2])[2:-3]
    posicao_3_ponto = subfont.render(lista_pontos[2], True, (0,0,0))
    pos_ponto_3 = posicao_3_ponto.get_rect()
    pos_ponto_3.center = 700, 300

    lista_pontos[3] = str(lista_pontos[3])[2:-3]
    posicao_4_ponto = subfont.render(lista_pontos[3], True, (0,0,0))
    pos_ponto_4 = posicao_4_ponto.get_rect()
    pos_ponto_4.center = 700, 350

    lista_pontos[4] = str(lista_pontos[4])[2:-3]
    posicao_5_ponto = subfont.render(lista_pontos[4], True, (0,0,0))
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

        py.display.flip()
        janela.fill((225,225,225))

        #Eventos da tela
        for event in py.event.get():

            if event.type == py.QUIT:
                return False

            if event.type == py.MOUSEBUTTONDOWN:
                x = py.mouse.get_pos()[0]
                y = py.mouse.get_pos()[1]

                if x > 50 and x < 100 and y > 536 and y < 550:
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