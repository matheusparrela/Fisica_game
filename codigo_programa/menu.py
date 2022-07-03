import pygame as py
import config as cf



def menu(janela, font, subfont, acerto_music, click_music, vitoria_music, derrota_music, erro_music, img_vidro_cabeca, img_vida, img_pontos, img_menu, pontos, vidas):
    
    screen = True
    
    #Logo, nome do jogo
    opcao1 = subfont.render("Continuar", True,(0,0,0))
    pos_opcao1 = opcao1.get_rect()
    pos_opcao1.center = 400, 100 

    opcao2 = subfont.render("Configurações", True,(0,0,0))
    pos_opcao2 = opcao2.get_rect()
    pos_opcao2.center = 400, 150 

    opcao3 = subfont.render("Sair", True,(0,0,0))
    pos_opcao3 = opcao3.get_rect()
    pos_opcao3.center = 400, 200 

    backgroud = py.image.load('img/embacado.jpeg')
    
    color = (225,225,225)

    while screen == True:

        janela.fill(color)    
        janela.blit(backgroud,(0,0))

        janela.blit(img_vidro_cabeca, (12, 10))
        janela.blit(img_menu, (380, 8))
        janela.blit(img_pontos, (630, 14))
        pontos_display = subfont.render("Pontos: "+str(pontos), True, (225,225,225))
        janela.blit(pontos_display, (675, 25))

        #vidas display
        if vidas >= 1:
            janela.blit(img_vida, (20, 15))

            if vidas >= 2: 
                janela.blit(img_vida, (65, 15))

                if vidas >= 3:
                    janela.blit(img_vida, (110, 15))


        py.draw.rect(janela, color, py.Rect(325, 55, 150, 200))
        py.draw.rect(janela, (0,0,0), py.Rect(325, 55, 150, 200),  2)
        py.draw.rect(janela, (169,169,169), py.Rect(327, 249, 146, 5))
        py.draw.rect(janela, (169,169,169), py.Rect(468, 57, 5, 194))


        #subtitulos, opçoes do menu
        janela.blit(opcao1, pos_opcao1)
        janela.blit(opcao2, pos_opcao2)    
        janela.blit(opcao3, pos_opcao3)

        #Uso do mouse na página das configurações
        for event in py.event.get():

            if event.type == py.QUIT:
                return False

            if event.type == py.MOUSEBUTTONDOWN:
                x, y = py.mouse.get_pos()

                if x > 350 and x < 450 and y > 90 and y < 110:
                    click_music.play()
                    return 0

                if x > 335 and x < 470 and y > 140 and y < 160:
                    click_music.play()
                    cf.configuracao(janela, font, subfont, acerto_music, click_music, vitoria_music, derrota_music, erro_music)

                if x > 380 and x < 455 and y > 195 and y < 210:
                    click_music.play()
                    return 1

            
        py.display.flip()



