import pygame
from random import randint
import salva_pontuacao


def perguntas(janela, font_perguntas, font_comum, subfont, font_avisos, font, acerto_music, erro_music, click_music, derrota_music, vitoria_musicc):
    
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
            returno = salva_pontuacao.fim_de_jogo(pontos, janela, font, subfont, font_avisos, click_music, acerto_music, derrota_music)

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
            returno = salva_pontuacao.fim_de_jogo(pontos, janela, font, subfont, font_avisos, click_music, acerto_music, derrota_music)

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
