import pygame as py


def como_jogar(janela, subfont, click_music):    

    tela_como_jogar = True

    #Carrega imagem de fundo
    img_como_jogar = py.image.load('img/img_como_jogar.png')

    #Carrega texto do botão voltar
    voltar = subfont.render("Voltar", True, (0,0,0))
    pos_voltar = voltar.get_rect()
    pos_voltar.center = 75, 550

    #Loop de tela
    while tela_como_jogar:
    
        #Limpa e atualiza tela
        py.display.flip()

        #Imagem de fundo e botão voltar
        janela.blit(img_como_jogar,(0, 0))
        janela.blit(voltar, pos_voltar)

        #Eventos do mouse
        for event in py.event.get():

            if event.type == py.QUIT:
                return False

            if event.type == py.MOUSEBUTTONDOWN:
                x = py.mouse.get_pos()[0]
                y = py.mouse.get_pos()[1]

                if x > 50 and x < 103 and y > 536 and y < 555:
                    click_music.play()
                    tela_como_jogar =  False
                    return True