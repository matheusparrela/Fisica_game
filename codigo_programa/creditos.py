import pygame


def creditos(janela, subfont, click_music):
    print("Função Creditos")

    tela_creditos = True

    #Carrega imagem de fundo
    img_creditos = pygame.image.load('img/creditos.png') 

    #Carrega texto do botão voltar
    voltar = subfont.render("Voltar", True,(0,0,0))
    pos_voltar = voltar.get_rect()
    pos_voltar.center = 75, 550

    #Loop de tela
    while tela_creditos:

        #Limpa e atualiza tela
        pygame.display.flip()

        #Imagem de fundo e botão voltar
        janela.blit(img_creditos,(0, 0))
        janela.blit(voltar, pos_voltar)

        #Eventos do mouse
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