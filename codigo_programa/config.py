import pygame as py
import database as db

#Define variaveis globais para volume do jogo
volume_efeitos = 1
volume_principal = 1

def musica_fundo():

    #Musicas do jogo
    musica_fundo = py.mixer.music.load('musicas/new_york_cyberpunk.mp3')
    py.mixer.music.play(-1) 

    #Seta Volume da musica de fundo e efeitos
    volume_efeitos = 1
    volume_principal = 1


def configuracao(janela, font, font_comum, subfont, acerto_music, click_music, vitoria_music, derrota_music, erro_music):
    print("Função Configuração")

    tela_config = True

    #Insere na função configuração as variaveis globais de volume para modificação
    global volume_efeitos
    global volume_principal

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

    img_volume_mais = py.image.load('img/vol_mais.png')
    img_volume_menos = py.image.load('img/vol_menos.png')
    img_volume_barra = py.image.load('img/barra_volume.png')


    input_box = py.Rect( 330, 400, 140, 32)
    color_inactive = py.Color(0,0,0)
    color = color_inactive

    reset = False

    #Loop de tela
    while tela_config:

        janela.fill((225,225,225))

        #Uso do mouse na página das configurações
        for event in py.event.get():

            if event.type == py.QUIT:
                return False

            if event.type == py.MOUSEBUTTONDOWN:
                x = py.mouse.get_pos()[0]
                y = py.mouse.get_pos()[1]
                print(py.mouse.get_pos())

                if x > 50 and x < 103 and y > 536 and y < 555:
                    print("Voltar")
                    tela_config = False
                    click_music.play()
                    return True

                #Volume da musica de fundo - Funcionalidade
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

                #Volume dos efeitos - Funcionalidade
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
                
                #Botão reseta classificação - Funcionalidade
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
        
        #Botão para resetar classificação
        if reset == False:
            janela.blit(mensagem_resetar, pos_mensagem_resetar)
        elif reset == True:
            janela.blit(mensagem_resetado, pos_mensagem_resetado)
        
        janela.blit(config_title, pos_title)
        py.draw.rect(janela, color, input_box, 2)

        
        #Volume 
        py.mixer.music.set_volume(volume_principal)
        acerto_music.set_volume(volume_efeitos)
        click_music.set_volume(volume_efeitos)
        derrota_music.set_volume(volume_efeitos)
        vitoria_music.set_volume(volume_efeitos)
        erro_music.set_volume(volume_efeitos)

        #Botões de volume
        janela.blit(img_volume_mais, (485, 180))
        janela.blit(img_volume_menos, (280, 180))
        janela.blit(img_volume_mais, (485, 280))
        janela.blit(img_volume_menos, (280, 280))

        #Subtitulos
        janela.blit(vol_principal, pos_volp)
        janela.blit(vol_efeitos, pos_volef)
        janela.blit(button_reseta_clas, pos_reseta_clas)
        
        #Botão voltar
        janela.blit(voltar, pos_voltar)
        py.display.flip()


def reseta_classificacao():

    db.reseta_classificacao()