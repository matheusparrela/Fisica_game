import pygame
import classificacao

def pega_nick(pontos, janela, font, subfont, font_avisos, click_music):

    input_box = pygame.Rect(300, 268, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    nome_temp = ''
    tela_salvapontos = True

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


    while tela_salvapontos:
        
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

        #Butão Voltar
        janela.blit(voltar_menu, pos_voltar_menu)

        #Botão Avançar
        janela.blit(avanca, pos_avanca)

        pygame.display.flip()
    
    if nome_temp != '':
        nome = nome_temp[:13]
        print("Nome digitado", nome)
        salva_pontuacao(nome, pontos)
        classificacao.classificacao(janela, subfont, font, click_music)
        return True
    else :
        return True



def salva_pontuacao(nome, pontuacao):

    lista_nomes_recordes = []
    file_nomes = open('arquivos/nomes_recordes.txt', '+r')

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

    print("Lista")
    print(lista_nomes_recordes)
    print(lista_pontos_recordes)

    #recebe novo recorde
    novo_recorde_nome = nome + '\n'
    novo_recorde_pontos = pontuacao


    if novo_recorde_pontos >= int(lista_pontos_recordes[0]):
        
            lista_pontos_recordes[4] = lista_pontos_recordes[3]
            lista_pontos_recordes[3] = lista_pontos_recordes[2]
            lista_pontos_recordes[2] = lista_pontos_recordes[1]
            lista_pontos_recordes[1] = lista_pontos_recordes[0]
            lista_pontos_recordes[0] = str(novo_recorde_pontos) + '\n'

            lista_nomes_recordes[4] = lista_nomes_recordes[3]
            lista_nomes_recordes[3] = lista_nomes_recordes[2]
            lista_nomes_recordes[2] = lista_nomes_recordes[1]
            lista_nomes_recordes[1] = lista_nomes_recordes[0]
            lista_nomes_recordes[0] = novo_recorde_nome

   
    elif novo_recorde_pontos >= int(lista_pontos_recordes[1]):
        
            lista_pontos_recordes[4] = lista_pontos_recordes[3]
            lista_pontos_recordes[3] = lista_pontos_recordes[2]
            lista_pontos_recordes[2] = lista_pontos_recordes[1]
            lista_pontos_recordes[1] = str(novo_recorde_pontos) + '\n'

            lista_nomes_recordes[4] = lista_nomes_recordes[3]
            lista_nomes_recordes[3] = lista_nomes_recordes[2]
            lista_nomes_recordes[2] = lista_nomes_recordes[1]
            lista_nomes_recordes[1] = novo_recorde_nome
   
   
    elif novo_recorde_pontos >= int(lista_pontos_recordes[2]):
        
            lista_pontos_recordes[4] = lista_pontos_recordes[3]
            lista_pontos_recordes[3] = lista_pontos_recordes[2]
            lista_pontos_recordes[2] = str(novo_recorde_pontos) + '\n'

            lista_nomes_recordes[4] = lista_nomes_recordes[3]
            lista_nomes_recordes[3] = lista_nomes_recordes[2]
            lista_nomes_recordes[2] = novo_recorde_nome
   
    elif novo_recorde_pontos >= int(lista_pontos_recordes[3]):
        
            lista_pontos_recordes[4] = lista_pontos_recordes[4]
            lista_pontos_recordes[3] = str(novo_recorde_pontos) + '\n'

            lista_nomes_recordes[4] = lista_nomes_recordes[4]
            lista_nomes_recordes[3] = novo_recorde_nome
   
    elif novo_recorde_pontos >= int(lista_pontos_recordes[4]):
        
            lista_pontos_recordes[4] = str(novo_recorde_pontos) + '\n'

            lista_nomes_recordes[4] = novo_recorde_nome

   
    file_nomes = open('arquivos/nomes_recordes.txt', 'w')

    file_nomes.write(lista_nomes_recordes[0])
    file_nomes.write(lista_nomes_recordes[1])
    file_nomes.write(lista_nomes_recordes[2])
    file_nomes.write(lista_nomes_recordes[3])
    file_nomes.write(lista_nomes_recordes[4])

    file_nomes.close()

    file_pontos = open('arquivos/pontos_recordes.txt', 'w')

    file_pontos.write(str(lista_pontos_recordes[0]))
    file_pontos.write(str(lista_pontos_recordes[1]))
    file_pontos.write(str(lista_pontos_recordes[2]))
    file_pontos.write(str(lista_pontos_recordes[3]))
    file_pontos.write(str(lista_pontos_recordes[4]))
    
    file_pontos.close()
 

def fim_de_jogo(pontos, janela, font, subfont, font_avisos, click_music, vitoria_music, derrota_music):

    print("Tela final/Game Over")

    tela_fim_de_jogo = True

    #carrega texto em avançar
    avanca = subfont.render("Avançar", True, (225,225,225), (0,0,0))
    pos_avanca = avanca.get_rect()
    pos_avanca.center = 725, 550

    img_pontos_2 = pygame.image.load('img/img_pontos_gameover.png')

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

    pontuacao = font.render("Pontuação: "+str(pontos), True, (225,225,225))
    pos_pontuacao = pontuacao.get_rect()
    pos_pontuacao.center = 400, 100
    toca_musica = True


    lista_pontos_recordes = []
    file_pontos = open('arquivos/pontos_recordes.txt', 'r')

    lista_pontos_recordes.append(file_pontos.readline())
    lista_pontos_recordes.append(file_pontos.readline())
    lista_pontos_recordes.append(file_pontos.readline())
    lista_pontos_recordes.append(file_pontos.readline())
    lista_pontos_recordes.append(file_pontos.readline())
    
    file_pontos.close()

    
    
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

        janela.blit(img_pontos_2, (325, 225))
        janela.blit(pontuacao, pos_pontuacao)
        
        #limpa e atualiza tela
        pygame.display.flip()

        #imagem de fundoe texto para os creditos
        janela.fill((0,0,0))
        janela.blit(avanca, pos_avanca)

        #Uso do mouse em voltar na página dos creditos
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

                    if pontos > 0 and pontos >= int(lista_pontos_recordes[4]): 
                        returno = pega_nick(pontos, janela, font, subfont, font_avisos, click_music)

                        #verifica se o botão de fechar janela foi ativado
                        if returno == False:
                            return False
                        else:
                            return True