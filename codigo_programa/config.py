import pygame
from pygame import *


def configuracao(janela, font, font_comum, subfont, acerto_music, click_music, vitoria_music, derrota_music, erro_music):
    print("Função Configuração")

    tela_config = True

    volume_efeitos = 1
    volume_principal = 1

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

