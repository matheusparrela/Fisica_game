import pygame
from pygame.locals import *
import config
import creditos
import como_jogar
import classificacao
import perguntas


def main():

    pygame.init()

    #Musica de Fundo
    config.musica_fundo()

    #Efeitos Sonoros
    click_music = pygame.mixer.Sound('musicas/click.wav')
    acerto_music = pygame.mixer.Sound('musicas/som_acerto.wav')
    erro_music = pygame.mixer.Sound('musicas/som_erro.wav')
    derrota_music = pygame.mixer.Sound('musicas/som_derrota.wav')
    vitoria_music = pygame.mixer.Sound('musicas/win_sound.wav')


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
            
            #Verifica de a lista com as imagens chegaram ao fim e reinicia a lista
            if self.atual >= len(self.sprites):
                self.atual = 0

            self.image = self.sprites[int(self.atual)]


    todas_as_sprites = pygame.sprite.Group()
    img_menu = Menu_img()
    todas_as_sprites.add(img_menu)

    #Frames por segundo do programa
    fps = pygame.time.Clock()

    #Loop de tela do programa
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
                    janela_aberta = perguntas.perguntas(janela, font_perguntas, font_comum, subfont, font_avisos, font, acerto_music, erro_music, click_music, derrota_music, vitoria_music)

                if a > 350 and a < 453 and b > 335 and b < 357:
                    print("opcao_2")
                    click_music.play()
                    janela_aberta = como_jogar.como_jogar(janela, subfont, click_music)
                    
                
                if a > 340 and a < 460 and b > 385 and b < 405:
                    print("opcao_3")
                    click_music.play()
                    janela_aberta = config.configuracao(janela, font, font_comum, subfont, acerto_music, click_music, vitoria_music, derrota_music, erro_music)

                if a > 340 and a < 465 and b > 435 and b < 455:
                    print("opcao_4")  
                    click_music.play()
                    janela_aberta = classificacao.classificacao(janela, subfont, font, click_music)
                    
                if a > 365 and a < 435 and b > 485 and b < 505:
                    print("opcao_5")  
                    click_music.play()
                    janela_aberta = creditos.creditos(janela, subfont, click_music)
            
                    

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


main()