import pygame as py
import classificacao as cl
import database as db


def pega_nick(pontos, janela, font, subfont, font_avisos, click_music):

    input_box = py.Rect(300, 268, 140, 32)
    color_inactive = py.Color('lightskyblue3')
    color_active = py.Color('dodgerblue2')
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
        for event in py.event.get():
            if event.type == py.QUIT:
                return False
            
                    
            if event.type == py.MOUSEBUTTONDOWN:
                
                x = py.mouse.get_pos()[0]
                y = py.mouse.get_pos()[1]
                print(py.mouse.get_pos())

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
            if event.type == py.KEYDOWN:
                if active:
            
                    if event.key == py.K_RETURN:
                        print(text)
                        text = ''
                        nome_temp = ''
                        tela_salvapontos = False
                    elif event.key == py.K_BACKSPACE:
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
        py.draw.rect(janela, color, input_box, 2)

        #Desenha Butão Voltar - Menu
        janela.blit(voltar_menu, pos_voltar_menu)

        #Desenha Botão Avançar
        janela.blit(avanca, pos_avanca)

        #Limpa e atualiza tela
        py.display.flip()
    
    #Verifica de algum nome foi digitado, se sim, salva os pontos e chama a classificação
    if nome_temp != '':
        nome = nome_temp[:13]
        print("Nome digitado", nome)
        salva_pontuacao(nome, pontos)
        cl.classificacao(janela, subfont, font, click_music)
        return True
    
    else :
        return True


def salva_pontuacao(nome, pontuacao):

    #Abre o arquivo de nomes da classificação e passa para uma lista
    lista_nomes = []
    lista_nomes = db.select_classificacao()

    #Abre o arquivo de pontos da classificação e passa para uma lista
    lista_pontos = []
    lista_pontos = db.select_pontuacao()

    print("Lista")
    print(lista_nomes)
    print(lista_pontos)

    #Recebe novo recorde
    novo_recorde_nome = str(nome)
    novo_recorde_pontos = pontuacao

    #Atualiza as posições da classificação
    if novo_recorde_pontos >= int(str(lista_pontos[0])[2:-3]):
        
            lista_pontos[4] = int(str(lista_pontos[3])[2:-3])
            lista_pontos[3] = int(str(lista_pontos[2])[2:-3])
            lista_pontos[2] = int(str(lista_pontos[1])[2:-3])
            lista_pontos[1] = int(str(lista_pontos[0])[2:-3])
            lista_pontos[0] = novo_recorde_pontos

            lista_nomes[4] = str(lista_nomes[3])[3:-4]
            lista_nomes[3] = str(lista_nomes[2])[3:-4]
            lista_nomes[2] = str(lista_nomes[1])[3:-4]
            lista_nomes[1] = str(lista_nomes[0])[3:-4]
            lista_nomes[0] = novo_recorde_nome

   
    elif novo_recorde_pontos >= int(str(lista_pontos[1])[2:-3]):
        
            lista_pontos[4] = int(str(lista_pontos[3])[2:-3])
            lista_pontos[3] = int(str(lista_pontos[2])[2:-3])
            lista_pontos[2] = int(str(lista_pontos[1])[2:-3])
            lista_pontos[1] = novo_recorde_pontos
            lista_pontos[0] = int(str(lista_pontos[0])[2:-3])

            lista_nomes[4] = str(lista_nomes[3])[3:-4]
            lista_nomes[3] = str(lista_nomes[2])[3:-4]
            lista_nomes[2] = str(lista_nomes[1])[3:-4]
            lista_nomes[1] = novo_recorde_nome
            lista_nomes[0] = str(lista_nomes[0])[3:-4]
   
   
    elif novo_recorde_pontos >= int(str(lista_pontos[2])[2:-3]):
        
            lista_pontos[4] = int(str(lista_pontos[3])[2:-3])
            lista_pontos[3] = int(str(lista_pontos[2])[2:-3])
            lista_pontos[2] = novo_recorde_pontos
            lista_pontos[1] = int(str(lista_pontos[1])[2:-3])
            lista_pontos[0] = int(str(lista_pontos[0])[2:-3])

            lista_nomes[4] = str(lista_nomes[3])[3:-4]
            lista_nomes[3] = str(lista_nomes[2])[3:-4]
            lista_nomes[2] = novo_recorde_nome
            lista_nomes[1] = str(lista_nomes[1])[3:-4]
            lista_nomes[0] = str(lista_nomes[0])[3:-4]
   
    elif novo_recorde_pontos >= int(str(lista_pontos[3])[2:-3]):
        
            lista_pontos[4] = int(str(lista_pontos[3])[2:-3])
            lista_pontos[3] = novo_recorde_pontos
            lista_pontos[2] = int(str(lista_pontos[2])[2:-3])
            lista_pontos[1] = int(str(lista_pontos[1])[2:-3])
            lista_pontos[0] = int(str(lista_pontos[0])[2:-3])

            lista_nomes[4] = str(lista_nomes[3])[3:-4]
            lista_nomes[3] = novo_recorde_nome
            lista_nomes[2] = str(lista_nomes[2])[3:-4]
            lista_nomes[1] = str(lista_nomes[1])[3:-4]
            lista_nomes[0] = str(lista_nomes[0])[3:-4]
   
    elif novo_recorde_pontos >= int(str(lista_pontos[4])[2:-3]):
        
            lista_pontos[4] = novo_recorde_pontos
            lista_pontos[3] = int(str(lista_pontos[3])[2:-3])
            lista_pontos[2] = int(str(lista_pontos[2])[2:-3])
            lista_pontos[1] = int(str(lista_pontos[1])[2:-3])
            lista_pontos[0] = int(str(lista_pontos[0])[2:-3])

            lista_nomes[4] = novo_recorde_nome
            lista_nomes[3] = str(lista_nomes[3])[3:-4]
            lista_nomes[2] = str(lista_nomes[2])[3:-4]
            lista_nomes[1] = str(lista_nomes[1])[3:-4]
            lista_nomes[0] = str(lista_nomes[0])[3:-4]

    #Escreve as novas listas no banco de dados
    db.update_classificacao(lista_nomes, lista_pontos)
 

def fim_de_jogo(pontos, janela, font, subfont, font_avisos, click_music, acerto_music, derrota_music, vitoria_music):

    print("Tela final/Game Over")

    tela_fim_de_jogo = True

    #Carrega texto do botão avançar
    avanca = subfont.render("Avançar", True, (225,225,225), (0,0,0))
    pos_avanca = avanca.get_rect()
    pos_avanca.center = 725, 550
    
    #Carrega imagem da estrela
    img_pontos_2 = py.image.load('img/img_pontos_gameover.png')

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

    #Abre o arquivo de pontos e passa para uma lista
    
    pontuacoes = db.select_pontuacao()

    print(str(pontuacoes[4])[2:-3])

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
        py.display.flip()

        #Imagem de fundo e botão avançar
        janela.fill((0,0,0))
        janela.blit(avanca, pos_avanca)

        #Eventos do mouse
        for event in py.event.get():

            if event.type == py.QUIT:
                return False

            if event.type == py.MOUSEBUTTONDOWN:
                x = py.mouse.get_pos()[0]
                y = py.mouse.get_pos()[1]
                print(py.mouse.get_pos())

                if x > 688 and x < 763 and y > 535 and y < 555:
                    print("Avançar")
                    click_music.play()
                    tela_fim_de_jogo =  False

                    if pontos > 0 and pontos >= int(str(pontuacoes[4])[2:-3]): 
                        retorno = pega_nick(pontos, janela, font, subfont, font_avisos, click_music)

                        #Verifica se o botão de fechar janela foi ativado
                        if retorno == False:
                            return False
                        else:
                            return True