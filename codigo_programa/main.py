from os import terminal_size
import pygame
from random import randint
from pygame.locals import *

pygame.init()

#Musicas do jogo
musica_fundo = pygame.mixer.music.load('codigo_programa/musicas/musica_fundo.mp3')
pygame.mixer.music.play(-1)

#Efeitos Sonoros
click_music = pygame.mixer.Sound('musicas/click_coin_mario.wav')
acerto_music = pygame.mixer.Sound('musicas/som_acerto.wav')
erro_music = pygame.mixer.Sound('musicas/som_erro.wav')
derrota_music = pygame.mixer.Sound('musicas/som_derrota.wav')
vitoria_music = pygame.mixer.Sound('musicas/som_vitoria.wav')


#Icone
icone = pygame.image.load('img/icone.png')
pygame.display.set_icon(icone)

#Display do jogo
janela = pygame.display.set_mode((800, 600))  
pygame.display.set_caption("Fisica Game v.1.6")  
janela_aberta = True

#Fontes de texto e outros
font  = pygame.font.SysFont('Uroob', 60)              #Fonte para titulos
subfont = pygame.font.SysFont('Uroob', 30)            #Fonte para corpo
font_perguntas = pygame.font.SysFont('Uroob', 17)     #Fonte para perguntas
font_comum = pygame.font.SysFont('Uroob', 25)         #Fonte para demais coisas
font_avisos = pygame.font.SysFont('Uroob', 13)        #Fonte para avisos

#Logo, nome do jogo
titulo = font.render("Física Game", True,(255,255,255),(0,0,0))
pos_titulo = titulo.get_rect()
pos_titulo.center = 400, 100 

#Posição, cor, fundo e texto
#Menu do jogo
opcao_1 = subfont.render("Iniciar", True,(255,255,255),(0,0,0))
pos_opcao_1 = opcao_1.get_rect()
pos_opcao_1.center = 400, 300

opcao_2= subfont.render("Como Jogar", True,(255,255,255),(0,0,0))
pos_opcao_2 = opcao_2.get_rect()
pos_opcao_2.center = 400, 350

opcao_3 = subfont.render("Configurações", True,(255,255,255),(0,0,0))
pos_opcao_3 = opcao_3.get_rect()
pos_opcao_3.center = 400, 400

opcao_4 = subfont.render("Classificação", True,(255,255,255),(0,0,0))
pos_opcao_4 = opcao_4.get_rect()
pos_opcao_4.center = 400, 450

opcao_5 = subfont.render("Créditos", True, (225,225,225), (0,0,0))
pos_opcao_5 = opcao_5.get_rect()
pos_opcao_5.center = 400, 500

opcao_6 = subfont.render("Sair", True,(255,255,255),(0,0,0))
pos_opcao_6 = opcao_6.get_rect()
pos_opcao_6.center = 400, 550



def pega_nick(pontos):

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
        classificacao()
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


def classificacao():


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
    



def configuracao():
    print("Função Configuração")

    tela_config = True

    #carrega texto em voltar
    voltar = subfont.render("Voltar", True, (0,0,0))
    pos_voltar = voltar.get_rect()
    pos_voltar.center = 75, 550

    config_title = font.render("Configurações", True, (0,0,0))
    pos_title = config_title.get_rect()
    pos_title.center = 400, 50

    vol_principal = font_comum.render("Volume Principal", True, (0,0,0))
    pos_volp = vol_principal.get_rect()
    pos_volp.center = 400, 170

    vol_efeitos = font_comum.render("Volume Efeitos", True, (0,0,0))
    pos_volef = vol_efeitos.get_rect()
    pos_volef.center = 400, 270

    button_reseta_clas = font_comum.render("Resetar Classificação", True, (0, 0 ,0))
    pos_reseta_clas = button_reseta_clas.get_rect()
    pos_reseta_clas.center = 400, 370

    mensagem_resetar = font_comum.render("Resetar", True, (0,0,0))
    pos_mensagem_resetar = mensagem_resetar.get_rect()
    pos_mensagem_resetar.center = 400, 420

    mensagem_resetado = font_comum.render("Resetado", True, (0,0,0))
    pos_mensagem_resetado = mensagem_resetado.get_rect()
    pos_mensagem_resetado.center = 400, 420

    img_volume_mais = pygame.image.load('img/vol_mais.png')
    img_volume_menos = pygame.image.load('img/vol_menos.png')
    img_volume_barra = pygame.image.load('img/barra_volume.png')

    global volume_principal
    global volume_efeitos

    input_box = pygame.Rect( 330, 400, 140, 32)
    color_inactive = pygame.Color(0,0,0)
    color = color_inactive

    reset = False

    while tela_config:

        janela.fill((225,225,225))

        #Uso do mouse na página das configurações
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())

                if x > 50 and x < 103 and y > 536 and y < 555:
                    print("Voltar")
                    tela_config = False
                    click_music.play()
                    return True

                #volume da musica de fundo
                if x > 480 and x < 520 and y > 180 and y < 215:
                    if volume_principal >= 0 and volume_principal <= 1:
                        if volume_principal != 1: 
                            volume_principal = volume_principal + 0.1
                            volume_principal = round(volume_principal, 1)
                            print('Volume principal mais')
                            print(volume_principal)

                if x > 280 and x < 320 and y > 180 and y < 215:
                    if volume_principal >= 0 and volume_principal <= 1:
                        if volume_principal != 0:
                            volume_principal = volume_principal - 0.1
                            volume_principal = round(volume_principal, 1)
                            print('Volume principal menos')
                            print(volume_principal)

                #volume dos efeitos
                if x > 480 and x < 520 and y > 280 and y < 315:
                    if volume_efeitos >= 0 and volume_efeitos <= 1:
                        if volume_efeitos != 1:
                            volume_efeitos = volume_efeitos + 0.1
                            volume_efeitos = round(volume_efeitos, 1)
                            print('Volume efeitos mais')
                            print(volume_efeitos)

                if x > 280 and x < 320 and y > 280 and y < 315:
                    if volume_efeitos >= 0 and volume_efeitos <= 1:
                        if volume_efeitos != 0:
                            volume_efeitos = volume_efeitos - 0.1
                            volume_efeitos = round(volume_efeitos, 1)
                            print("Volume efeitos menos")
                            print(volume_efeitos)

                if input_box.collidepoint(event.pos):
                    print("Resetar Classificação")
                    reset = True
                    reseta_classificacao()


        #Desenho das barras do volume principal
        if volume_principal >= 0.1:
            janela.blit(img_volume_barra, (330, 180))
            if volume_principal >= 0.2:
                janela.blit(img_volume_barra, (345, 180))
                if volume_principal >= 0.3:
                    janela.blit(img_volume_barra, (360, 180))
                    if volume_principal >= 0.4:
                        janela.blit(img_volume_barra, (375, 180))
                        if volume_principal >= 0.5:
                            janela.blit(img_volume_barra, (390, 180))
                            if volume_principal >= 0.6:
                                janela.blit(img_volume_barra, (405, 180))
                                if volume_principal >= 0.7:
                                    janela.blit(img_volume_barra, (420, 180))
                                    if volume_principal >= 0.8:
                                        janela.blit(img_volume_barra, (435, 180))
                                        if volume_principal >= 0.9:
                                            janela.blit(img_volume_barra, (450, 180))
                                            if volume_principal >= 1:
                                                janela.blit(img_volume_barra, (465, 180))

        #Desenho das barras do volume de efeitos
        if volume_efeitos >= 0.1:
            janela.blit(img_volume_barra, (330, 280))
            if volume_efeitos >= 0.2:
                janela.blit(img_volume_barra, (345, 280))
                if volume_efeitos >= 0.3:
                    janela.blit(img_volume_barra, (360, 280))
                    if volume_efeitos >= 0.4:
                        janela.blit(img_volume_barra, (375, 280))
                        if volume_efeitos >= 0.5:
                            janela.blit(img_volume_barra, (390, 280))
                            if volume_efeitos >= 0.6:
                                janela.blit(img_volume_barra, (405, 280))
                                if volume_efeitos >= 0.7:
                                    janela.blit(img_volume_barra, (420, 280))
                                    if volume_efeitos >= 0.8:
                                        janela.blit(img_volume_barra, (435, 280))
                                        if volume_efeitos >= 0.9:
                                            janela.blit(img_volume_barra, (450, 280))
                                            if volume_efeitos >= 1:
                                                janela.blit(img_volume_barra, (465, 280))
        if reset == False:
            janela.blit(mensagem_resetar, pos_mensagem_resetar)
        elif reset == True:
            janela.blit(mensagem_resetado, pos_mensagem_resetado)

        #volume 
        pygame.mixer.music.set_volume(volume_principal)
        acerto_music.set_volume(volume_efeitos)
        click_music.set_volume(volume_efeitos)
        derrota_music.set_volume(volume_efeitos)
        vitoria_music.set_volume(volume_efeitos)
        erro_music.set_volume(volume_efeitos)

        #botões de volume
        janela.blit(img_volume_mais, (485, 180))
        janela.blit(img_volume_menos, (280, 180))
        janela.blit(img_volume_mais, (485, 280))
        janela.blit(img_volume_menos, (280, 280))

        #subtitulos
        janela.blit(vol_principal, pos_volp)
        janela.blit(vol_efeitos, pos_volef)
        janela.blit(button_reseta_clas, pos_reseta_clas)

        #titulo
        janela.blit(config_title, pos_title)

        #botão resetar classificação
    
        pygame.draw.rect(janela, color, input_box, 2)
        
        #botão voltar
        janela.blit(voltar, pos_voltar)
        pygame.display.flip()



def reseta_classificacao():
    print("Função Reseta Classificação")

    #reseta os pontos da classificação
    file_pontos = open('arquivos/pontos_recordes.txt', 'w')
    file_pontos.write('5\n')
    file_pontos.write('4\n')
    file_pontos.write('3\n')
    file_pontos.write('2\n')
    file_pontos.write('1\n')
    file_pontos.close()

    #Reseta os nomes da classificação
    file_nomes = open('arquivos/nomes_recordes.txt', 'w')
    file_nomes.write('Newton\n')
    file_nomes.write('Tesla\n')
    file_nomes.write('Coulomb\n')
    file_nomes.write('Kepler\n')
    file_nomes.write('Curie\n')
    file_nomes.close()




def creditos():

    print("Função Creditos")

    tela_creditos = True
    #Carrega imagem de fundo
    img_creditos = pygame.image.load('img/creditos.png') 

    #carrega texto em voltar
    voltar = subfont.render("Voltar", True,(0,0,0))
    pos_voltar = voltar.get_rect()
    pos_voltar.center = 75, 550

    while tela_creditos:

        #limpa e atualiza tela
        pygame.display.flip()

        #imagem de fundoe texto para os creditos
        janela.blit(img_creditos,(0, 0))
        janela.blit(voltar, pos_voltar)

        #Uso do mouse em voltar na página dos creditos
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())

                if x > 50 and x < 103 and y > 536 and y < 555:
                    print("Voltar")
                    tela_creditos = False
                    click_music.play()
                    return True


def como_jogar():    
    
    print("Função Como jogar")

    tela_como_jogar = True
    img_como_jogar = pygame.image.load('img/img_como_jogar.png')

    #carrega texto em voltar
    voltar = subfont.render("Voltar", True, (0,0,0))
    pos_voltar = voltar.get_rect()
    pos_voltar.center = 75, 550

    while tela_como_jogar:
    
       #limpa e atualiza tela
        pygame.display.flip()

        #imagem de fundoe texto para os creditos
        janela.blit(img_como_jogar,(0, 0))
        janela.blit(voltar, pos_voltar)


        #Uso do mouse em voltar na página dos creditos
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())

                if x > 50 and x < 103 and y > 536 and y < 555:
                    print("Voltar")
                    click_music.play()
                    tela_como_jogar =  False
                    return True


def fim_de_jogo(pontos):

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
                        returno = pega_nick(pontos)

                        #verifica se o botão de fechar janela foi ativado
                        if returno == False:
                            return False
                        else:
                            return True



def perguntas():
    
    print("Função Perguntas")

    tela_jogo = True

    quadro_fundo = pygame.image.load('img/quadro_negro.jpeg')


    voltar = subfont.render("Voltar", True, (225,225,225))
    pos_voltar = voltar.get_rect()
    pos_voltar.center = 75, 550

    pontos = 0
    pergunta = 0
    respondido = True #Olha se a pergunta foi respondida
    perguntas_feitas = 0
    lista_perguntas_feitas  = []
    vidas = 3

    img_vida = pygame.image.load('img/img_vida.png')

    img_pontos = pygame.image.load('img/img_pontos.png')

    while tela_jogo:

        #Mudar para que numeros não se repita
        if respondido == True:
            j = 0 
            while j < 1:
                pergunta = randint(0, 49)

                if len(lista_perguntas_feitas) == 50:
                        print('Tamanho da lista == 50')
                        perguntas_feitas += 1
                        respondido = True
                        j += 1

                if pergunta not in lista_perguntas_feitas:
                    lista_perguntas_feitas.append(pergunta)
                    respondido = False
                    j += 1
                    perguntas_feitas += 1
                    print(perguntas_feitas)

                    


        #Verfica se todas as perguntas disponiveis foram feitas e chama a tela de fim de jogo
        if perguntas_feitas > 50:
            print("Todas as Perguntas foram feitas")

            #verifica se o botão de fechar janela foi ativado
            returno = fim_de_jogo(pontos)
            if returno == False:
                return False
            else:
                return True

        #vidas display
        if vidas >= 1:
            janela.blit(img_vida, (15, 15))
            if vidas >= 2: 
                janela.blit(img_vida, (50, 15))
                if vidas >= 3:
                    janela.blit(img_vida, (85, 15))
            
        #Verifica se as vidas acabaram e chama a tela de fim de jogo
        if vidas == 0:
            print("Vidas Acabaram")
            returno = fim_de_jogo(pontos)

            #verifica se o botão de fechar janela foi ativado
            if returno == False:
                return False
            else:
                return True

        #limpa e atualiza tela
        pygame.display.flip()

        #imagem de fundoe texto para os creditos
        janela.blit(quadro_fundo,(0, 0))
        janela.blit(voltar, pos_voltar)

        #pontos display
        janela.blit(img_pontos, (625, 15))
        pontos_display = subfont.render("Pontos: "+str(pontos), True, (225,225,225))
        janela.blit(pontos_display, (675, 25))


        if pergunta == 0:
                perg = 'Pergunta 1) -  De acordo com a lei de Coulomb, a força eletrostática entre duas cargas puntiformes em repouso é:'
                resp_a = 'A) inversamente proporcional ao produto do módulo das cargas e inversamente proporcional ao quadrado da distância entre elas.'
                resp_b = 'B) diretamente proporcional ao produto do módulo das cargas e inversamente proporcional ao quadrado da distância entre elas.'
                resp_c = 'C) diretamente proporcional ao produto do módulo das cargas e ao quadrado da distância entre elas.'
                resp_d = 'D) uma grandeza escalar, pois é completamente descrita somente por seu módulo.'
                resp_e = 'E) uma força de contato e de natureza elétrica.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True


        if pergunta == 1:
                perg = 'Pergunta 2) - Sobre o campo magnético terrestre, assinale a alternativa falsa:'
                resp_a = 'A) O polo norte magnético encontra-se no polo sul geográfico da Terra.'
                resp_b = 'B) O polo sul magnético encontra-se no polo norte geográfico da Terra.'
                resp_c = 'C) O campo magnético terrestre é mais fraco na região dos polos.'
                resp_d = 'D) O campo magnético terrestre é mais intenso na região dos polos.'
                resp_e = 'E) O campo magnético terrestre surge por causa da diferença na velocidade de rotação do núcleo e da crosta terrestre.'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
                           
        if pergunta == 2:
                perg = 'Pergunta 3) - Sobre as propriedades do campo magnético, assinale a alternativa falsa.'
                resp_a = 'A) As linhas de indução magnética emergem do polo norte magnético e adentram o polo sul magnético.'
                resp_b = 'B) As linhas de indução magnética são sempre abertas.'
                resp_c = 'C) A concentração de linhas de indução magnética está relacionada com a intensidade do campo magnético na região.'
                resp_d = 'D) Não é possível separar, em nenhuma ocasião, os polos norte e sul magnéticos.'
                resp_e = 'E) Nenhuma das alternativas.'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play() 
                                return True          
 
        if pergunta == 3:
                perg = 'Pergunta 4) - Em relação à capacitância de um capacitor de placas paralelas, assinale o que for FALSO:'
                resp_a = 'A) a capacitância é diretamente proporcional à área dos capacitores'
                resp_b = 'B) a capacitância é inversamente proporcional à distância entre os capacitores'
                resp_c = 'C) a permissividade elétrica é uma característica que depende do material inserido entre as placas do capacitor'
                resp_d = 'D) quanto maior for a capacitância de um capacitor, menos carga ele pode armazenar para uma determinada tensão elétrica'
                resp_e = 'E) quanto menor for a capacitância de um capacitor, menos carga ele pode armazenar para uma determinada tensão elétrica'
                     
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 4:
                perg = 'Pergunta 5) - (UCSal-BA) Um resistor de 100 ohms é percorrido por uma corrente elétrica de 20 mA. A ddp, em volts, é igual a:'
                resp_a = 'A) 2,0'
                resp_b = 'B) 5,0'
                resp_c = 'C) 2,0 . 10'
                resp_d = 'D) 2,0 . 10^3'
                resp_e = 'E) 5,0 . 10^3'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
         
        if pergunta == 5:
                perg = 'Pergunta 6) - De acordo com o Eletromagnetismo, o movimento relativo entre cargas elétricas e um observador tem como resultado'
                perg_2 = 'o surgimento de:'
                resp_a = 'A) campos elétricos'
                resp_b = 'B) campos magnéticos.'
                resp_c = 'C) diferença de potencial.'
                resp_d = 'D) fenômenos relativísticos'
                resp_e = 'E) ondas gravitacionais.'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()

                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
                        
        if pergunta == 6:
                perg = 'Pergunta 7) - Um pequeno ímã é colocado nas proximidades de uma barra de ferro. Sobre a situação descrita, assinale a alternativa correta.'
                resp_a = 'A) O ímã atrai a barra de ferro com a mesma intensidade que a barra de ferro atrai o ímã.'
                resp_b = 'B) A força que o ímã exerce sobre a barra de ferro é maior que a força que o ferro exerce sobre o ímã.'
                resp_c = 'C) O ímã atrai a barra de ferro.'
                resp_d = 'D) A barra de ferro atrai o ímã.'
                resp_e = 'E) A força que a barra de ferro exerce sobre o ímã é maior que a força que o ímã exerce sobre a barra de ferro.'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 7:
                perg = 'Pergunta 8) - Ao quebrarmos um ímã ao meio, devemos esperar que:'
                resp_a = 'A) os seus pedaços fiquem desmagnetizados.'
                resp_b = 'B) um dos seus pedaços seja o polo norte, e o outro, polo sul.'
                resp_c = 'C) cada um de seus pedaços torne-se um ímã menor'
                resp_d = 'D) A Lei de Lenz afirma que a corrente elétrica induzida em um circuito ou condutor é tal que o seu campo magnético sempre'
                resp_d_2 = 'favorece as variações de campos magnéticos externos.'
                resp_e = 'E) O imã explode.'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_d_2_2 = font_perguntas.render(resp_d_2, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_d_2_2, (25, 445))
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()

                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 8:
                perg = 'Pergunta 9) - Determine a quantidade de elétrons que deve ser perdida por um corpo para que ele adquira uma carga positiva que'
                perg_2 = 'corresponda a 2,56 . 10^– 10 C. Dado: a carga elementar vale 1,6 . 10^–19 C.'
                resp_a = 'A) 1,20 . 10^9'
                resp_b = 'B) 2,60 . 10^9'
                resp_c = 'C) 5,50 . 10^9'
                resp_d = 'D) 1,60 . 10^9'
                resp_e = 'E) 2,56 . 10^9'        
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()

                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 9:
                perg = 'Pergunta 10) - Marque a alternativa correta: os resistores são elementos de circuito que consomem energia elétrica, convertendo-a'
                perg_2 = 'integralmente em energia térmica. A conversão de energia elétrica em energia térmica é chamada de:'
                resp_a = 'A) Efeito Joule'
                resp_b = 'B) Efeito Térmico'
                resp_c = 'C) Condutores'
                resp_d = 'D) Resistores'
                resp_e = 'E) Amplificadores'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 10:
                perg = 'Pergunta 11) - Assinale o dispositivo elétrico capaz de transformar parte da energia elétrica a ele fornecida em outras formas'
                perg_2 = 'de energia que não sejam exclusivamente a energia térmica.'
                resp_a = 'A) Resistor'
                resp_b = 'B) Voltímetro'
                resp_c = 'C) Amperímetro'
                resp_d = 'D) Gerador'
                resp_e = 'E) Receptor'
           
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()  
                                return True               
        
        if pergunta == 11:
                perg = 'Pergunta 12) - Chuveiros elétricos, lâmpadas incandescentes, fios condutores e ferros elétricos possuem algo em comum:'
                perg_2 = 'todos podem ser classificados no mesmo grupo de dispositivos elétricos. Esses dispositivos podem ser considerados como:'
                resp_a = 'A) Receptores'
                resp_b = 'B) Resistores'
                resp_c = 'C) Fusíveis'
                resp_d = 'D) Disjuntores'
                resp_e = 'E) Geradores'
              
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()

                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play() 
                                return True
        
        if pergunta == 12:
                perg = 'Perguntas 13) - Alguns dispositivos de segurança utilizados em circuitos elétricos possuem o intuito de interromper a passagem de'
                perg_2 = 'grandes correntes elétricas que poderiam ser prejudiciais para o seu funcionamento. São dispositivos de segurança:'
                resp_a = 'A) Pilhas'
                resp_b = 'B) Resistor e varistor'
                resp_c = 'C) Fusível e disjuntor'
                resp_d = 'D) Interruptor'
                resp_e = 'E) Amperímetro e voltímetro'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 13:
                perg = 'Pergunta 14) -  (UECE 97.1) – A matéria, em seu estado normal, não manifesta propriedades elétricas. No atual estágio de conhecimentos'
                perg_2 = 'da estrutura atômica, isso nos permite concluir que a matéria:'
                resp_a = 'A) é constituída somente de nêutrons.'
                resp_b = 'B) possui maior número de nêutrons que de prótons.'
                resp_c = 'C) possui quantidades iguais de prótons e elétrons.'
                resp_d = 'D) é constituída somente de prótons.'
                resp_e = 'E) possui apenas elétrons.'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))    
                janela.blit(perg_2_2, (25, 95)) 
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()

                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play() 
                                return True

        if pergunta == 14:
                perg = 'Pergunta 15) - No Eletromagnetismo, existe uma lei que estabelece a seguinte relação: a variação temporal do fluxo de campo magnético'
                perg_2 = 'através de uma área é responsável por produzir um campo elétrico perpendicular a essa área e, consequentemente, um campo magnético'
                perg_3 = 'induzido no sentido oposto àquela variação. A lei que estabelece uma relação matemática para o enunciado mostrado acima é chamada de:'
                resp_a = 'A) Lei de Faraday.'
                resp_b = 'B) Lei de Ampére.'
                resp_c = 'C) Lei de Gauss.'
                resp_d = 'D) Lei de Lenz.'
                resp_e = 'E) Lei de Faraday-Lenz.'
           
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                perg_3_3 = font_perguntas.render(perg_3, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25,95))
                janela.blit(perg_3_3, (25, 115))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                acerto_music.play()
                                pontos += 1    

                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play() 
                                return True

        if pergunta == 15:
                perg = 'Pergunta 16) - A unificação e a descrição matemática dos fenômenos eletromagnéticos foi essencial para o desenvolvimento de'
                perg_2 = 'inúmeras tecnologias utilizadas atualmente. O responsável por essa unificação foi:'
                resp_a = 'A) Michael Faraday.'
                resp_b = 'B) Hans Christin Oersted.'
                resp_c = 'C) André Marie Ampére.'
                resp_d = 'D) James Clerk Maxwell.'
                resp_e = 'E) Nikola Tesla.'
                
            
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25,95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                acerto_music.play()
                                pontos += 1 
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()  

                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play() 
                                return True


        if pergunta == 16:
                perg = 'Pergunta 17) - Sobre o principio da atração e repulsão assinale a alternativa correta:'
                resp_a = 'A) cargas elétricas negativas são atraídas por outras cargas de mesmo sinal;'
                resp_b = 'B) cargas elétricas positivas e negativas não interagem;'
                resp_c = 'C) cargas elétricas negativas são repelidas por cargas elétricas positivas;'
                resp_d = 'D) cargas elétricas positivas são repelidas por outras cargas elétricas positivas;'
                resp_e = 'E) todas as cargas elétricas, independentemente de sua natureza, têm tendência a se atraírem;'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 17:
                perg = 'Pergunta 18)  -Pelo princípio da conservação de cargas elétricas, é correto afirmar que'
                resp_a = 'A) dois corpos inicialmente neutros tende-se a tornassem eletrizados negativamente ao entrarem em contato com outro corpo neutro;'
                resp_b = 'B) a soma das cargas envolvidas em um sistema isolado sempre será igual ao dobre da carga do corpo mais eletrizado negativamente;'
                resp_c = 'C) a carga energética final em um sistema eletricamente isolado,sempre será a metade da carga inicial e terá sinal positivo, visto que os elétrons tendem à Terra;'
                resp_d = 'D) em um sistema eletricamente isolado, a soma algébrica das cargas positivas as negativas é sempre constante;'
                resp_e = 'E) em um sistema eletricamente neutro, a soma algébrica das cargas positivas as negativas é sempre igual à zero;'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True


        if pergunta == 18:
                perg = 'Pergunta 19) - Um corpo inicialmente positivo, com carga elétrica Q = + 3,2 * 10 ^(-16), ganha 10(^3) elétrons. O número final de elétrons'
                perg_2 = 'e a carga adquirida pelo corpo são respectivamente:'
                resp_a = 'A) 3 * 10^(3); 1,6 * 10^(-16)'
                resp_b = 'B) 2,6 * 10^(3); 10^(-16)'
                resp_c = 'C) 10^(3); 10^(-16)'
                resp_d = 'D) 3,2 * 10^(3); 16 * 10^(-16)'
                resp_e = 'E) 4,8 * 10^(3); 10^(-16)'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25,95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 19:
                perg = 'Pergunta 20) - "A carga elétrica só pode existir como múltiplo de uma quantidade mínima definida", essa afirmação é:'
                resp_a = 'A) Verdadeira, pois a carga elétrica só pode existir como múltipla da carga elementar "e", por isso se diz que ele é quantizada;'
                resp_b = 'B) Verdadeira, pois a carga elétrica só pode existir como múltipla da carga elementar 0,12, por isso se diz que ele é quantizada;'
                resp_c = 'C) Falsa, pois a carga elétrica é quantizada;'
                resp_d = 'D) Falsa, pois a carga elétrica próvem da união da carga "e" mais o raio gama.'
                resp_e = 'E) Nenhuma das alternativas;'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        if pergunta == 20:
                perg = 'Pergunta 21 ) - O Primeiro a testemunhar o fenômeno da indução eletromagnética foi'
                resp_a = 'A) Michael Faraday'
                resp_b = 'B) Joseph Henry'
                resp_c = 'C) André-Marie Ampère'
                resp_d = 'D) Heinrich Lenz'
                resp_e = 'E) Franz Ernst Neumann'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 21:
                perg = 'Pergunta 22) - O criador da pilha elétrica, dispositivo que converte energia química em energia elétrica, foi'
                resp_a = 'A) Luigi Galvani'
                resp_b = 'B) Georg Simon Ohm'
                resp_c = 'C) André-Marie Ampère'
                resp_d = 'D) Humphry Davy'
                resp_e = 'E) Alessandro Volta'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        if pergunta == 22:
                perg = 'Pergunta 23) -  Físico e matemático alemão que relacionou em uma lei as três grandezas elétricas principais (Corrente, Tensão'
                perg_2 = 'e Resistência) e demonstra como elas estão intrinsecamente ligadas.'
                resp_a = 'A) Tales de Mileto'
                resp_b = 'B) Georg Simon Ohm'
                resp_c = 'C) Harold Pitney Brown'
                resp_d = 'D) Demócrito'
                resp_e = 'E) Gustav Kirchhoff'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 23:
                perg = 'Pergunta 24) -  Duas partículas de cargas elétricas Q1 = 4,0 . 10^-16 C e Q2 = 6,0 . 10^-16 C estão separadas no vácuo por uma'
                perg_2 = 'distância de 3,0 . 10-9 m. Sendo K0 = 9 . 109 N.m2/ C2, a intensidade da força de interação entre elas, em Newtons, é de:'
                resp_a = 'A) 1,2 . 10^-5'
                resp_b = 'B) 1,8 . 10^-4'
                resp_c = 'C) 2,0 . 10^-4'
                resp_d = 'D) 2,4 . 10^-4'
                resp_e = 'E) 3,0 . 10^-3'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        
        if pergunta == 24:
                perg = 'Pergunta 25) - A intensidade do campo elétrico, num ponto situado a 3,0 mm de uma carga elétrica puntiforme Q = 2,7 µC no vácuo'
                perg_2 = '(ko = 9.109 N.m2/C2) é:'
                resp_a = 'A) 2,7 . 10^9 N/C'
                resp_b = 'B) 2,7 . 10^8 N/C'
                resp_c = 'C) 1,8 . 10^6 N/C'
                resp_d = 'D) 1,7 . 10^-9 N/C'
                resp_e = 'E) 2,7 . 10^-5 N/C'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 25:
                perg = 'Pergunta 26) - Calcule a intensidade da força elétrica de repulsão entre duas cargas puntiformes 3.10-5 e 5.10-6 que se encontram'
                perg_2 = 'no vácuo, separadas por uma distância de 15 cm.'
                resp_a = 'A) F = 610 N'
                resp_b = 'B) F = 30 N'
                resp_c = 'C) F = 60 N'
                resp_d = 'D) F = 40 N'
                resp_e = 'E) F = 50 N'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 26:
                perg = 'Pergunta 27) - Seja Q (positiva) a carga gerada do campo elétrico e q a carga de prova em um ponto P, próximo de Q. É correto:'
                resp_a = 'A) O vetor campo elétrico em P dependerá do sinal de q.'
                resp_b = 'B) O vetor campo elétrico em P dependerá do sinal de q.'
                resp_c = 'C) O vetor campo elétrico será constante, qualquer que seja o valor de q.'
                resp_d = 'D) A força elétrica em P será constante, qualquer que seja o valor de q.'
                resp_e = 'E) O vetor campo elétrico em P é independente da carga de prova q.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                    
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        if pergunta == 27:
                perg = 'Pergunta 28) - De acordo com a Lei de Coulomb, assinale a alternativa correta:'
                resp_a = 'A) A força de interação entre duas cargas é proporcional à massa que elas possuem;'
                resp_b = 'B) A força elétrica entre duas cargas independe da distância entre elas;'
                resp_c = 'C) A força de interação entre duas cargas elétricas é diretamente proporcional ao produto entre as cargas;'
                resp_d = 'D) A força eletrostática é diretamente proporcional à distância entre as cargas;'
                resp_e = 'E) A constante eletrostática K é a mesma para qualquer meio material.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 28:
                perg = 'Pergunta 29) - O primeiro ou um dos primeiros a testemunhar uma reação elétrica devido ao acúmulo de cargas elétricas, esfregando'
                perg_2 = 'âmbar em lã, foi'
                resp_a = 'A)Albert Einstein'
                resp_b = 'B)Nikola Tesla'
                resp_c = 'C)Thomas Edison'
                resp_d = 'D)Tales de Mileto.'
                resp_e = 'E)Alessandro Volta.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        if pergunta == 29:
                perg = 'Pergunta 30) - A lei que melhor explica o funcionamento de um transformador é a lei de'
                resp_a = 'A) Guldberg-Waage.'
                resp_b = 'B) Ohm.'
                resp_c = 'C) Ampere.'
                resp_d = 'D) Faraday.'
                resp_e = 'E) Newton. Neste caso, trata-se da segunda lei.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        if pergunta == 30:
                perg = 'Pergunta 31) - Um capacitor em corrente alternada ocasiona'
                resp_a = 'A) um atraso na tensão elétrica em relação à corrente elétrica'
                resp_b = 'B) um atraso na corrente elétrica em relação à tensão elétrica.'
                resp_c = 'C) a destruição dos demais componentes do circuito.'
                resp_d = 'D) curto-circuito.'
                resp_e = 'E) um abrimento no circuito, impossibilitando a passagem de corrente elétrica.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 31:
                perg = 'Pergunta 32) - Se 2 resistores de 7 Ohms estão associados em paralelo, a resistência total entre os dois é igual a'
                resp_a = 'A) 3,5 Ohms'
                resp_b = 'B) 70 Ohms'
                resp_c = 'C) 14 Ohms'
                resp_d = 'D) 19 Ohms'
                resp_e = 'E) 0 Ohms, pois em um circuito paralelo é impossível gerar oposição à corrente elétrica usando somente resistores.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        if pergunta == 32:
                perg = 'Pergunta 33) - As lâmpadas incandescentes são constituidas por qual filamento?'
                resp_a = 'A) Neónio'
                resp_b = 'B) Xenônio'
                resp_c = 'C) Tungstênio'
                resp_d = 'D) Rênio'
                resp_e = 'E) Irídio'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 33:
                perg = 'Pergunta 34) - Uma lâmpada incandescente apresenta em seu rótulo as seguintes especificações: 60 W e 120V. Determine a'
                perg_2 = 'a resistência elétrica da lâmpada'
                resp_a = 'A) 60 Ohms'
                resp_b = 'B) 240 Ohms'
                resp_c = 'C) 30 Ohms'
                resp_d = 'D) 300 Ohms'
                resp_e = 'E) 125 Ohms'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True,(225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))  
                janela.blit(perg_2_2, (25, 95))   
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        if pergunta == 34:
                perg = 'Pergunta 35) - Qual é o valor da carga adquirida por um por um corpo que ganhou 1000 Trilhões de Elétrons?'
                resp_a = 'A) 1,6X10^-15 C'
                resp_b = 'B) 1,6X10^-4 C'
                resp_c = 'C) 1,6X10^-5 C'
                resp_d = 'D) 1,6X10^-16 C'
                resp_e = 'E) 1,6X10^-7'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        
        if pergunta == 35:
                perg = 'Pergunta 36) -  Um chuveiro elétrico possui a indicação 2200 W e 110 V. Qual é a corrente elétrica que o percorre?'
                resp_a = 'A) 2310 A'
                resp_b = 'B) 80 A'
                resp_c = 'C) 2090 A'
                resp_d = 'D) 110 A'
                resp_e = 'E) 20 A'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True


        if pergunta == 36:
                perg = 'Pergunta 37) - Uma lâmpada tem sua resistência elétrica valendo 10 Ohms, e a corrente que a percorre vale 20 A. Quanto vale o'
                perg_2 = 'seu estado de tensão?'
                resp_a = 'A) 200 V'
                resp_b = 'B) 10 V'
                resp_c = 'C) 30 V'
                resp_d = 'D) 0,5 V'
                resp_e = 'E) 500 V'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True
        if pergunta == 37:
                perg = 'Pergunta 38) - Considere um ferro elétrico com potência de 750 W, sendo utilizado 4 horas por dia durante 5 dias do mês. Neste'
                perg_2 = 'período mensal, a energia elétrica consumida pelo ferro elétrico, em kWh, é:'
                resp_a = 'A) 5.'
                resp_b = 'B) 10.'
                resp_c = 'C) 20.'
                resp_d = 'D) 15.'
                resp_e = 'E) 25.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 38:
                perg = 'Pergunta 39) - Uma lâmpada de filamento de tungstênio, ligada a uma tomada de 120 V, é percorrida por uma corrente contínua'
                perg_2 = 'de 4,0 A. O valor da resistência elétrica nesse filamento é em ohms:'
                resp_a = 'A) 25.'
                resp_b = 'B) 30.'
                resp_c = 'C) 15.'
                resp_d = 'D) 20.'
                resp_e = 'E) 35.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))    
                janela.blit(perg_2_2, (25, 95)) 
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 39:
                perg = 'Pergunta 40) - Qual o nome do instrumento de Medição que é possível ver as formas de onda de um determinado sinal elétrico?'
                resp_a = 'A) Ondoscópico'
                resp_b = 'B) Teleonda'
                resp_c = 'C) Osciloscópio'
                resp_d = 'D) Megôhmetro'
                resp_e = 'E) Varivolt'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 40:
                perg = 'Perguntas 41) - "Para um condutor mantido à temperatura constante, a razão entre a tensão entre dois pontos e a corrente elétrica'
                perg_2 = 'é constante". Esta frase se refera a lei:'
                resp_a = 'A) Lei de Coulomb'
                resp_b = 'B) Lei de Charles'
                resp_c = 'C) Lei de Ohm'
                resp_d = 'D) Lei de Baer'
                resp_e = 'E) Lei de Hooke'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 41:
                perg = 'Pergunta 42) -  Potência pode ser definida por qual alternativa abaixo?'
                resp_a = 'A) É a medida da resistência do chuveiro elétrico.'
                resp_b = 'B) Potência é definida pela razão entre o trabalho realizado e o tempo em que é executado o trabalho.'
                resp_c = 'C) É definida pela multiplicação entre o peso e a energia do corpo que realiza o trabalho.'
                resp_d = 'D) É definida pelo quadrado da raiz cúbica do trabalho realizado pelo corpo.'
                resp_e = 'E) É definida pelo cálculo logarítmico entre o tempo que o trabalho é realizado e a massa do objeto movido.'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()

                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 42:
                perg = 'Pergunta 43) -  Qual é a medida no S.I. de luminosidade?'
                resp_a = 'A) Lúmen'
                resp_b = 'B) Candela'
                resp_c = 'C) Watt'
                resp_d = 'D) Claro e escuro'
                resp_e = 'E) Preto e branco'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 43:
                perg = 'Pergunta 44) -  Estando duas cargas elétricas Q idênticas separadas por uma distância de 4m, determine o valor destas cargas'
                perg_2 = 'sabendo que a intensidade da força entre elas é de 200 N.'
                resp_a = 'A) Q = 5,96.10^-4 C'
                resp_b = 'B) Q = 5,96.10^-5 C'
                resp_c = 'C) Q = 2,96.10^-4 C'
                resp_d = 'D) Q = 3,96.10^-4 C'
                resp_e = 'E) Q = 4,96.10^-4 C'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 44:
                perg = 'Pergunta 45) - "A corrente elétrica é diretamente proporcional à tensão elétrica e inversamente proporcional à resistência". Este'
                perg_2 = 'enunciado, que é talvez a informação mais básica a respeito da eletricidade, refere-se à'
                resp_a = 'A) Lei de Ohm.'
                resp_b = 'B) Lei de Lenz.'
                resp_c = 'C) Lei de Ampere.'
                resp_d = 'D) Primeira Lei de Newton.'
                resp_e = 'E) Lei de Faraday.'

                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 45:
                perg = 'Pergunta 46) - Em um aparelho encontra-se a descrição de que deve ser ligado à uma diferença de potencial de 80V. Gerando uma'
                perg_2 = 'potência de 520W, qual será a intensidade percorrida nesse aparelho?'
                resp_a = 'A) 6,5 A'
                resp_b = 'B) 6,0 A'
                resp_c = 'C) 41600 A'
                resp_d = 'D) 65,0 A'
                resp_e = 'E) N.D.A'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render(perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))  
                janela.blit(perg_2_2, (25, 95))   
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True

        if pergunta == 46:
                perg = 'Pergunta 47) - Quantos Joules passam, a cada segundo, em 4W?'
                resp_a = 'A) 4J'
                resp_b = 'B) 8J'
                resp_c = 'C) Impossível determinar'
                resp_d = 'D) 2J'
                resp_e = 'E) 6J'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                                
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True    

         
        
        if pergunta == 47:
                perg = 'Pergunta 48) - Um chuveiro elétrico quando submetido a uma ddp de 220V é atravessado por uma corrente elétrica de 8,0A.'
                perg_2 = 'A energia consumida, em KWh, em 15 minutos de funcionamento é:'
                resp_a = 'A) 4,4'
                resp_b = 'B) 0,044'
                resp_c = 'C) 0,22'
                resp_d = 'D) 2,2'
                resp_e = 'E) 0,44'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                perg_2_2 = font_perguntas.render( perg_2, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(perg_2_2, (25, 95))
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                                
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True    

        if pergunta == 48:
                perg = 'Pergunta 49) - Qual das alternativas melhor define um resistor?'
                resp_a = 'A) Transforma um fusível em energia luminosa'
                resp_b = 'B) Transforma energia elétrica em energia térmica'
                resp_c = 'C) Transforma calor em frio'
                resp_d = 'D) Transforma fluxo de carga em elétrons'
                resp_e = 'E) Foi estabelecido pela primeira lei de OHM como capacidade de transformar energia térmica em energia consumível'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                acerto_music.play()
                                pontos += 1
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                                
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True    

        if pergunta == 49:
                perg = 'Pergunta 50) - Calcule a energia dissipada em um sistema que apresenta tensão (U) = 4,5 V e resistência (R) = 2 Ohms.'
                resp_a = 'A) 10, 625'
                resp_b = 'B) 2,45'
                resp_c = 'C) 10,125'
                resp_d = 'D) 10,50'
                resp_e = 'E) 2, 125'
                      
                perg_1 = font_perguntas.render(perg, True, (225,225,225))
                resp_a_1 = font_perguntas.render(resp_a, True, (225,225,225))
                resp_b_1 = font_perguntas.render(resp_b, True, (225,225,225))
                resp_c_1 = font_perguntas.render(resp_c, True, (225,225,225))
                resp_d_1 = font_perguntas.render(resp_d, True, (225,225,225))
                resp_e_1 = font_perguntas.render(resp_e, True, (225,225,225))
                janela.blit(perg_1, (25, 75))     
                janela.blit(resp_a_1, (25, 275)) 
                janela.blit(resp_b_1, (25, 325))   
                janela.blit(resp_c_1, (25, 375))   
                janela.blit(resp_d_1, (25, 425))   
                janela.blit(resp_e_1, (25, 475))  
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        return False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            print(pygame.mouse.get_pos())

                            if x > 25 and x < 37 and y > 275 and y < 287:
                                print("A")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 325 and y < 339:
                                print("B")
                                vidas -= 1
                                erro_music.play()
                                respondido = True
                            if x > 25 and x < 37 and y > 375 and y < 386:
                                print("C")
                                respondido = True
                                acerto_music.play()
                                pontos += 1
                            if x > 25 and x < 37 and y > 425 and y < 439:
                                print("D")
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                            if x > 25 and x < 37 and y > 475 and y < 486:
                                print("E") 
                                respondido = True
                                vidas -= 1
                                erro_music.play()
                                
                            
                            if x > 50 and x < 103 and y > 536 and y < 555:
                                print("Voltar")
                                tela_jogo = False
                                click_music.play()
                                return True  


#Classe responsavel pela background do menu
class Menu_img(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_1.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_2.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_3.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_4.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_5.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_6.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_7.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_8.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_9.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_10.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_11.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_12.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_13.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_14.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_15.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_16.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_17.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_18.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_19.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_20.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_21.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_22.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_23.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_24.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_25.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_26.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_27.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_28.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_29.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_30.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_31.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_32.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_33.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_34.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_35.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_36.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_37.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_38.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_39.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_40.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_41.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_42.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_43.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_44.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_45.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_46.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_47.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_48.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_49.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_50.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_51.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_52.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_53.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_54.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_55.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_56.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_57.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_58.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_59.png'))
        self.sprites.append(pygame.image.load('img/sprite_menu/img_menu_60.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
        self.atual += 1
        
        #verifica de a lista com as imagens chegaram ao fim e reinicia a lista
        if self.atual >= len(self.sprites):
            self.atual = 0

        self.image = self.sprites[int(self.atual)]


todas_as_sprites = pygame.sprite.Group()
img_menu = Menu_img()
todas_as_sprites.add(img_menu)

#Fremes por segundo do programa
fps = pygame.time.Clock()

#volume ao começar o jogo
volume_principal = 1
volume_efeitos = 1

#Podemos dizer que isso seria a main
while janela_aberta:
    
        fps.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        janela.fill((0,0,0))

        if event.type == pygame.MOUSEBUTTONDOWN:
            a = pygame.mouse.get_pos()[0]
            b = pygame.mouse.get_pos()[1]
            print(pygame.mouse.get_pos())

            if a > 370 and a < 430 and b > 285 and b < 305:
                print("opcao_1")
                click_music.play()
                janela_aberta = perguntas()

            if a > 350 and a < 453 and b > 335 and b < 357:
                print("opcao_2")
                click_music.play()
                janela_aberta = como_jogar()
                
            
            if a > 340 and a < 460 and b > 385 and b < 405:
                print("opcao_3")
                click_music.play()
                janela_aberta = configuracao()

            if a > 340 and a < 465 and b > 435 and b < 455:
                print("opcao_4")  
                click_music.play()
                janela_aberta = classificacao()
                
            if a > 365 and a < 435 and b > 485 and b < 505:
                print("opcao_5")  
                click_music.play()
                janela_aberta = creditos()
        
                

            if a > 385 and a < 416 and b > 537 and b < 552:     #botão do menu,sair
                print("Programa Finalizado!\n")
                opcao_6 = subfont.render("Sair", True,(225,0,0),(0,0,0))
                click_music.play()
                janela_aberta = False
    

        #background menu
        todas_as_sprites.draw(janela)
        todas_as_sprites.update()

        #titulo
        janela.blit(titulo, pos_titulo) 
        
        #subtitulos, opçoes do menu
        janela.blit(opcao_1, pos_opcao_1)
        janela.blit(opcao_2, pos_opcao_2)    
        janela.blit(opcao_3, pos_opcao_3)
        janela.blit(opcao_4, pos_opcao_4)
        janela.blit(opcao_5, pos_opcao_5)
        janela.blit(opcao_6, pos_opcao_6)

        pygame.display.flip()

pygame.quit()