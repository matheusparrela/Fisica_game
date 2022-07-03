import pygame as py
from random import randint
import salva_pontuacao as sp
import database as db
import menu

def perguntas(janela, font_perguntas, subfont, font_avisos, font, acerto_music, erro_music, click_music, derrota_music, vitoria_music):

    tela_jogo = True

    img_fundo = py.image.load('img/img_fundo.png')

    pontos = 0
    pergunta = 0
    respondido = True           #Olha se a pergunta foi respondida
    perguntas_feitas = 0
    lista_perguntas_feitas  = []
    vidas = 3

    img_vida = py.image.load('img/coracao.png')
    img_pontos = py.image.load('img/estrela.png')
    img_vidro = py.image.load('img/vidro.png')
    img_vidro_cabeca = py.image.load('img/cabeca.png')
    img_menu = py.image.load('img/menu.png')

    while tela_jogo:


        #Mudar para que numeros não se repita
        if respondido == True:

            j = 0 
            while j < 1:
                pergunta = randint(1, 50)
                questao = db.select_questao(pergunta)

                if len(lista_perguntas_feitas) == 50:
                        perguntas_feitas += 1
                        respondido = True
                        j += 1

                if pergunta not in lista_perguntas_feitas:
                    lista_perguntas_feitas.append(pergunta)
                    respondido = False
                    j += 1
                    perguntas_feitas += 1


        #Verfica se todas as perguntas disponiveis foram feitas e chama a tela de fim de jogo
        if perguntas_feitas > 50:

            #verifica se o botão de fechar janela foi ativado
            returno = sp.fim_de_jogo(pontos, janela, font, subfont, font_avisos, click_music, acerto_music, derrota_music, vitoria_music)

            if returno == False:
                return False

            else:
                return True

        #vidas display
        if vidas >= 1:
            janela.blit(img_vida, (20, 15))

            if vidas >= 2: 
                janela.blit(img_vida, (65, 15))

                if vidas >= 3:
                    janela.blit(img_vida, (110, 15))
            
        #Verifica se as vidas acabaram e chama a tela de fim de jogo
        if vidas == 0:
            retorno = sp.fim_de_jogo(pontos, janela, font, subfont, font_avisos, click_music, acerto_music, derrota_music, vitoria_music)

            #verifica se o botão de fechar janela foi ativado
            if retorno == False:
                return False
            else:
                return True

        #limpa e atualiza tela
        py.display.flip()

        #imagem de fundo e botão voltar
        janela.blit(img_fundo,(0, 0))
  
        #pontos display
        janela.blit(img_vidro_cabeca, (12, 10))
        janela.blit(img_menu, (380, 8))
        janela.blit(img_pontos, (630, 14))
        pontos_display = subfont.render("Pontos: "+str(pontos), True, (225,225,225))
        janela.blit(pontos_display, (675, 25))

        #fazer isto só uma vez
        perg = formata_texto(questao[0], font_perguntas)
        resp_a = formata_texto(questao[1], font_perguntas)
        resp_b = formata_texto(questao[2], font_perguntas)
        resp_c = formata_texto(questao[3], font_perguntas)
        resp_d = formata_texto(questao[4], font_perguntas)
        resp_e = formata_texto(questao[5], font_perguntas)
        correta = questao[6]
                
        k = 0
        tab = 0 

        janela.blit(img_vidro, (12, 265))

        while k < int(len(perg)) or k <  int(len(perg)) or k <  int(len(resp_a)) or k <  int(len(resp_b)) or k <  int(len(resp_c)) or k <  int(len(resp_d)) or  k < int(len(resp_e)):
            
            if k <  int(len(perg)):
                janela.blit(perg[k], (25, 75 + tab))
            
            if k <  int(len(resp_a)):
                janela.blit(resp_a[k], (20, 275 + tab)) 
            
            if k <  int(len(resp_b)):
                janela.blit(resp_b[k], (20, 325 + tab))   
           
            if k <  int(len(resp_c)):
                janela.blit(resp_c[k], (20, 375 + tab))   
            
            if k <  int(len(resp_d)):
                janela.blit(resp_d[k], (20, 425 + tab))
           
            if k <  int(len(resp_e)):
                janela.blit(resp_e[k], (20, 475 + tab))

            k = k + 1 
            tab = tab + 25
                
        for event in py.event.get():

            if event.type == py.QUIT:
                return False

            if event.type == py.MOUSEBUTTONDOWN:
                x, y = py.mouse.get_pos()

                if x > 25 and x < 37 and y > 275 and y < 287:
                    respondido = True
                    resposta = 'A'

                if x > 25 and x < 37 and y > 325 and y < 339:
                    respondido = True
                    resposta = 'B'

                if x > 25 and x < 37 and y > 375 and y < 386:
                    respondido = True
                    resposta = 'C'

                if x > 25 and x < 37 and y > 425 and y < 439:
                    respondido = True
                    resposta = 'D'

                if x > 25 and x < 37 and y > 475 and y < 486:
                    respondido = True 
                    resposta = 'E'

                                
                if x > 388 and x < 420 and y > 20 and y < 47:
                    ret = menu.menu(janela, font, subfont, acerto_music, click_music, vitoria_music, derrota_music, erro_music, img_vidro_cabeca, img_vida, img_pontos, img_menu, pontos, vidas)   

                    if ret == 1:
                        tela_jogo = False
                        return True

        if respondido == True:

                if correta == resposta:
                    pontos += 1
                    acerto_music.play()
        
                else:
                    vidas -= 1                       
                    erro_music.play() 

def formata_texto(texto, fonte):

    lista = []
    pergunta = []
    i = 0
    j = 95

    if len(texto) > i:
              
        while i < len(texto):
        
                if (i+j) >= len(texto):

                    if texto[i] == ' ':
                        pergunta.append(texto[i+1:len(texto)])
                    elif texto[i] != ' ':
                        pergunta.append(texto[i:len(texto)])   
                    i+=j


                elif texto[i+j] == ' ':
                    pergunta.append(texto[i:i+j])
                    i = i + j

                elif texto[i+j] != ' ':
                    while texto[i+j] != ' ':
                        j-=1

                    if texto[i] == ' ':
                        pergunta.append(texto[i+1:i+j])
                    elif texto[i-1] != ' ':
                        pergunta.append(texto[i:i+j])
                    i = i + j
                    j = 95
                
    else: 
        pergunta.append(texto)
                               
    k = 0
                    
    while k < len(pergunta):
                       
        lista.append(fonte.render(pergunta[k], True, (225,225,225)))
        k = k + 1 

    return lista