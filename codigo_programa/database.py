import sqlite3
from sqlite3.dbapi2 import Cursor
import pygame
import classificacao

database = sqlite3.connect('database/fisicagame_database')
cursor = database.cursor()

def pega_nick(pontos, janela, font, subfont, font_avisos, click_music, cursor):

    input_box = pygame.Rect(300, 268, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    nome_temp = ''
    tela_salvapontos = True

    #Carregam textos e mesagens que irão aparecer na tela
    avanca = subfont.render("Avançar", True, (0,0,0))
    pos_avanca = avanca.get_rect()
    pos_avanca.center = 725, 550

    voltar_menu = subfont.render("Menu", True, (0,0,0))
    pos_voltar_menu = voltar_menu.get_rect()
    pos_voltar_menu.center = 75, 550

    mensagem = subfont.render("Parabéns!! Você está no top cinco", True, (0,0,0))
    pos_mensagem = mensagem.get_rect()
    pos_mensagem.center = 400, 100

    aviso = font_avisos.render("MAX: 13 caracteres", True, (0,0,0))
    pos_aviso = aviso.get_rect()
    pos_aviso.center = 400, 310

    legenda = subfont.render("Digite seu Nome:", True, (0,0,0))
    pos_legenda = legenda.get_rect()
    pos_legenda.center = 400, 250

    #Loop de tela
    while tela_salvapontos:
        
        #Eventos do mouse e teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())

                if x > 688 and x < 763 and y > 535 and y < 555:
                    print("Avançar")
                    click_music.play()
                    tela_salvapontos =  False
                    nome_temp = text

                
                if x > 50 and x < 100 and y > 536 and y < 550:
                    print("Voltar - Menu")
                    tela_salvapontos = False
                    click_music.play()
                    return True

                #Se o mouse clicar no retangulo
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                #Muda a cor da caixa de texto quando acionada
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
            
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                        nome_temp = ''
                        tela_salvapontos = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        nome_temp = text

        janela.fill((225, 225, 225))

        
        #Desenha legenda na tela
        janela.blit(mensagem, pos_mensagem)
        janela.blit(legenda, pos_legenda)
        janela.blit(aviso, pos_aviso)
       
        #Renderiza texto digitado.
        txt_surface = subfont.render(text, True, color)

        #Aumenta o tamanho da caixa se o texto for longo
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width

        #Mostra Testo que esta sendo digitado
        janela.blit(txt_surface, (305, 275))
        
        #Desenha a caixa de texto
        pygame.draw.rect(janela, color, input_box, 2)

        #Desenha Butão Voltar - Menu
        janela.blit(voltar_menu, pos_voltar_menu)

        #Desenha Botão Avançar
        janela.blit(avanca, pos_avanca)

        #Limpa e atualiza tela
        pygame.display.flip()
    
    #Verifica de algum nome foi digitado, se sim, salva os pontos e chama a classificação
    if nome_temp != '':
        nome = nome_temp[:13]
        print("Nome digitado", nome)
        salva_pontuacao(nome, pontos, cursor)
        database.commit()
       
        classificacao.classificacao(janela, subfont, font, click_music)
        
        return True
    
    else :
        database.commit()
        return True

    ()


def salva_pontuacao(nome, pontuacao, cursor):

    #Recebe novo recorde
    novo_recorde_nome = nome
    novo_recorde_pontos = pontuacao


    lista_nomes_recordes = []
    i = 1
    while i <= 5:
        
        cursor.execute(f'''SELECT nome FROM classificacao where id_posicao = '{i}' ''') 
        string_nome = str(cursor.fetchall())
        lista_nomes_recordes.append(string_nome[3:-4])
        i = i + 1


    lista_pontos_recordes = []
    i = 1
    while i <= 5:
        
        cursor.execute(f'''SELECT pontuacao FROM classificacao where id_posicao = '{i}' ''') 
        string_pontos = str(cursor.fetchall())
        lista_pontos_recordes.append(string_pontos[2:-3])
        i = i + 1

    #Atualiza as posições da classificação
    if novo_recorde_pontos >= int(lista_pontos_recordes[0]):
        
            lista_pontos_recordes[4] = lista_pontos_recordes[3]
            lista_pontos_recordes[3] = lista_pontos_recordes[2]
            lista_pontos_recordes[2] = lista_pontos_recordes[1]
            lista_pontos_recordes[1] = lista_pontos_recordes[0]
            lista_pontos_recordes[0] = str(novo_recorde_pontos)

            lista_nomes_recordes[4] = lista_nomes_recordes[3]
            lista_nomes_recordes[3] = lista_nomes_recordes[2]
            lista_nomes_recordes[2] = lista_nomes_recordes[1]
            lista_nomes_recordes[1] = lista_nomes_recordes[0]
            lista_nomes_recordes[0] = novo_recorde_nome

   
    elif novo_recorde_pontos >= int(lista_pontos_recordes[1]):
        
            lista_pontos_recordes[4] = lista_pontos_recordes[3]
            lista_pontos_recordes[3] = lista_pontos_recordes[2]
            lista_pontos_recordes[2] = lista_pontos_recordes[1]
            lista_pontos_recordes[1] = str(novo_recorde_pontos)

            lista_nomes_recordes[4] = lista_nomes_recordes[3]
            lista_nomes_recordes[3] = lista_nomes_recordes[2]
            lista_nomes_recordes[2] = lista_nomes_recordes[1]
            lista_nomes_recordes[1] = novo_recorde_nome
   
   
    elif novo_recorde_pontos >= int(lista_pontos_recordes[2]):
        
            lista_pontos_recordes[4] = lista_pontos_recordes[3]
            lista_pontos_recordes[3] = lista_pontos_recordes[2]
            lista_pontos_recordes[2] = str(novo_recorde_pontos)

            lista_nomes_recordes[4] = lista_nomes_recordes[3]
            lista_nomes_recordes[3] = lista_nomes_recordes[2]
            lista_nomes_recordes[2] = novo_recorde_nome
   
    elif novo_recorde_pontos >= int(lista_pontos_recordes[3]):
        
            lista_pontos_recordes[4] = lista_pontos_recordes[4]
            lista_pontos_recordes[3] = str(novo_recorde_pontos)

            lista_nomes_recordes[4] = lista_nomes_recordes[4]
            lista_nomes_recordes[3] = novo_recorde_nome
   
    elif novo_recorde_pontos >= int(lista_pontos_recordes[4]):
        
            lista_pontos_recordes[4] = str(novo_recorde_pontos)

            lista_nomes_recordes[4] = novo_recorde_nome


    #Atualiza a classificação no banco de dados
    i = 1
    while i <= 5:
        cursor.execute(f'''update classificacao 
        SET nome = '{lista_nomes_recordes[i-1]}'
        where id_posicao = {i} 
        limit 1;''')
        i = i + 1
        database.commit()

    i = 1
    while i <= 5:
        cursor.execute(f'''update classificacao 
        SET pontuacao = '{int(lista_pontos_recordes[i-1])}' 
        where id_posicao = {i} 
        limit 1;''')
        i = i + 1
        database.commit()
    


def fim_de_jogo(pontos, janela, font, subfont, font_avisos, click_music, acerto_music, derrota_music, vitoria_music, cursor):

    print("Tela final/Game Over")

    tela_fim_de_jogo = True

    #Carrega texto do botão avançar
    avanca = subfont.render("Avançar", True, (225,225,225), (0,0,0))
    pos_avanca = avanca.get_rect()
    pos_avanca.center = 725, 550
    
    #Carrega imagem da estrela
    img_pontos_2 = pygame.image.load('img/img_pontos_gameover.png')

    #Carrega o textos motivadores
    texto_final_1 = subfont.render("Vamos estudar mais hein!!", True, (225,255,255))
    pos_texto_final_1 = texto_final_1.get_rect()
    pos_texto_final_1.center= 400, 400
    
    texto_final_2 = subfont.render("Muito bom!!", True, (225, 225, 225))
    pos_texto_final_2 = texto_final_2.get_rect()
    pos_texto_final_2.center= 400, 400

    texto_final_3 = subfont.render("Mandou bem", True, (225, 225, 225))
    pos_texto_final_3 = texto_final_3.get_rect()
    pos_texto_final_3.center= 400, 400

    texto_final_4  = subfont.render("Incrível", True, (225, 225, 225))
    pos_texto_final_4 = texto_final_4.get_rect()
    pos_texto_final_4.center = 400, 400

    texto_final_5  = subfont.render("Gênio", True, (225, 225, 225))
    pos_texto_final_5 = texto_final_5.get_rect()
    pos_texto_final_5.center = 400, 400

    texto_final_6  = subfont.render("Perfeito!! Você respondeu todas as perguntas corretamente!", True, (225, 225, 225))
    pos_texto_final_6 = texto_final_6.get_rect()
    pos_texto_final_6.center = 400, 400

    #Carrega o texto da pontuação
    pontuacao = font.render("Pontuação: "+str(pontos), True, (225,225,225))
    pos_pontuacao = pontuacao.get_rect()
    pos_pontuacao.center = 400, 100
    
    toca_musica = True

    #Verifica no banco de dados a menor pontuação
    cursor.execute('''SELECT pontuacao FROM classificacao where id_posicao = '5' ''') 
    string_pontos = str(cursor.fetchall())
    menor_pontuacao = string_pontos[2:-3]
    menor_pontuacao = int(menor_pontuacao)          
    
    #Loop de tela
    while tela_fim_de_jogo:

        #Musica que será tocada na tela final
        while toca_musica:

            if pontos < 5:
                derrota_music.play()
                toca_musica = False

            if pontos >= 5:
                vitoria_music.play()
                toca_musica = False
            
        #Texto que seŕa exibido na tela final/game over
        if pontos < 5:
            janela.blit(texto_final_1, pos_texto_final_1) 
        if pontos >= 5 and pontos <=15:
            janela.blit(texto_final_2, pos_texto_final_2)        
        if pontos > 15 and pontos < 25:
            janela.blit(texto_final_3, pos_texto_final_3)
        if pontos >= 25 and pontos < 40:
            janela.blit(texto_final_4, pos_texto_final_4)
        if pontos >= 40 and pontos < 50:
            janela.blit(texto_final_5, pos_texto_final_5)
        if pontos >= 50:
            janela.blit(texto_final_6, pos_texto_final_6)     

        #Desenha a estrela e a pontuação na tela
        janela.blit(img_pontos_2, (325, 225))
        janela.blit(pontuacao, pos_pontuacao)
        
        #Limpa e atualiza tela
        pygame.display.flip()

        #Imagem de fundo e botão avançar
        janela.fill((0,0,0))
        janela.blit(avanca, pos_avanca)

        #Eventos do mouse
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())

                if x > 688 and x < 763 and y > 535 and y < 555:
                    print("Avançar")
                    click_music.play()
                    tela_fim_de_jogo =  False

                    if pontos > 0 and pontos >= menor_pontuacao: 
                        returno = pega_nick(pontos, janela, font, subfont, font_avisos, click_music, cursor)

                        #Verifica se o botão de fechar janela foi ativado
                        if returno == False:
                            return False
                        else:
                            return True