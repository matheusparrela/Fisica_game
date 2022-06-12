import pygame as py


def creditos(janela, subfont, click_music):

    tela_creditos = True

    #Carrega imagem de fundo
    img_creditos = py.image.load('img/creditos.png') 

    #Carrega texto do botão voltar
    voltar = subfont.render("Voltar", True,(0,0,0))
    pos_voltar = voltar.get_rect()
    pos_voltar.center = 75, 550

    #Loop de tela
    while tela_creditos:

        #Limpa e atualiza tela
        py.display.flip()

        #Imagem de fundo e botão voltar
        janela.blit(img_creditos,(0, 0))
        janela.blit(voltar, pos_voltar)

        #Eventos do mouse
        for event in py.event.get():

            if event.type == py.QUIT:
                return False

            if event.type == py.MOUSEBUTTONDOWN:
                x = py.mouse.get_pos()[0]
                y = py.mouse.get_pos()[1]

                if x > 50 and x < 103 and y > 536 and y < 555:
                    tela_creditos = False
                    click_music.play()
                    return True