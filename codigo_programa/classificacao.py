import pygame

def classificacao(janela, subfont, font, click_music):


    lista_nomes_recordes = []
    file_nomes = open('arquivos/nomes_recordes.txt', 'r')

    lista_nomes_recordes.append(file_nomes.readline())
    lista_nomes_recordes.append(file_nomes.readline())
    lista_nomes_recordes.append(file_nomes.readline())
    lista_nomes_recordes.append(file_nomes.readline())
    lista_nomes_recordes.append(file_nomes.readline())

    file_nomes.close()


    lista_pontos_recordes = []
    file_pontos = open('arquivos/pontos_recordes.txt', 'r')

    lista_pontos_recordes.append(file_pontos.readline())
    lista_pontos_recordes.append(file_pontos.readline())
    lista_pontos_recordes.append(file_pontos.readline())
    lista_pontos_recordes.append(file_pontos.readline())
    lista_pontos_recordes.append(file_pontos.readline())
    
    file_pontos.close()

    #Carrega titulo da página
    text_config = font.render("Classificação", True, (0,0,0))
    pos_text = text_config.get_rect()
    pos_text.center = 400, 100

    #carrega texto em voltar
    voltar_menu = subfont.render("Menu", True, (0,0,0))
    pos_voltar_menu = voltar_menu.get_rect()
    pos_voltar_menu.center = 75, 550

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

    while tela_classificacao:

        pygame.display.flip()
        janela.fill((225,225,225))

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


        janela.blit(text_config, pos_text)
        janela.blit(voltar_menu, pos_voltar_menu)

        janela.blit(primeiro, pos_primeiro)
        janela.blit(segundo, pos_segundo)
        janela.blit(terceiro, pos_terceiro)
        janela.blit(quarto, pos_quarto)
        janela.blit(quinto, pos_quinto)


        janela.blit(posicao_1_nome, pos_nome_1)
        janela.blit(posicao_2_nome, pos_nome_2)
        janela.blit(posicao_3_nome, pos_nome_3)
        janela.blit(posicao_4_nome, pos_nome_4)
        janela.blit(posicao_5_nome, pos_nome_5)

        janela.blit(posicao_1_ponto, pos_ponto_1)
        janela.blit(posicao_2_ponto, pos_ponto_2)
        janela.blit(posicao_3_ponto, pos_ponto_3)
        janela.blit(posicao_4_ponto, pos_ponto_4)
        janela.blit(posicao_5_ponto, pos_ponto_5)