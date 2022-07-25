import database as db
import PySimpleGUI as psg

psg.theme('DefaultNoMoreNagging')

def init():
        layout = [
                [psg.Button('ADICIONAR QUESTÃO', size=(50, 1))],
                [psg.Button('EXCLUIR QUESTÃO',size=(50, 1))],
                [psg.Button('RESETAR BANCO DE QUESTÕES',size=(50, 1))],
                [psg.Button('CANCELAR',size=(50, 1), button_color=('white','red'))],
        ]
        
        return psg.Window('MENU - EDIÇÃO DE PERGUNTAS', layout=layout, resizable=True, element_justification='center', finalize=True)


def add_questao():
        layout =[[psg.Text('ADICIONAR QUESTÃO')],
                [psg.Text('QUESTÃO')],
                [psg.Multiline(size=(100,5))],
                [psg.Text('OPÇÃO A')],
                [psg.Multiline(size=(100,2))],
                [psg.Text('OPÇÃO B')],
                [psg.Multiline(size=(100,2))],
                [psg.Text('OPÇÃO C')],
                [psg.Multiline(size=(100,2))],
                [psg.Text('OPÇÃO D')],
                [psg.Multiline(size=(100,2))],
                [psg.Text('OPÇÃO E')],
                [psg.Multiline(size=(100,2))],
                [psg.Text('RESPOSTA')],
                [psg.Radio('A',"resp", default=False), psg.Radio('B', "resp",default=False), psg.Radio('C', "resp",default=False), psg.Radio('D', "resp", default=False), psg.Radio('E', "resp", default=False)],
                [psg.Button('ADICIONAR', button_color=('white','green')), psg.Button('CANCELAR', button_color=('white','red'), enable_events=True)],
                ]

        return psg.Window('MENU - EDIÇÃO DE PERGUNTAS', layout=layout, resizable=True, element_justification='center', finalize=True)
       


def rem_questao():
        lista = [0,1,2,4]
        layout =[[psg.Text('REMOVER QUESTÃO')],
                [psg.Text('Número da questão:')],
                [psg.InputCombo(lista, size=(50,1))],
                [psg.Text('Questão:')],
                [psg.Text('A:')],
                [psg.Text('B:')],
                [psg.Text('C:')],
                [psg.Text('D:')],
                [psg.Text('E:')],
                [psg.Button('REMOVER', button_color=('white','green')), psg.Button('CANCELAR', button_color=('white','red'), enable_events=True)],
        ]
        
        return psg.Window('MENU - EDIÇÃO DE PERGUNTAS', layout=layout, resizable=True, element_justification='center', finalize=True)


def resete():
        layout =[[psg.Text('Está ação apagará todas as questões adicionadas no programa! Tem certeza que deseja continuar?', size=(50, 5))],
                [psg.Button('CONTINUAR', button_color=('white','green')), psg.Button('CANCELAR', button_color=('white','red'), enable_events=True)],
        ]
       
        return psg.Window('MENU - EDIÇÃO DE PERGUNTAS', layout=layout, resizable=True, element_justification='center', finalize=True)



janela1, janela2, janela3, janela4 = init(), None, None, None

while True:
            window, event, values = psg.read_all_windows()
           
            if window == janela1: 
                if event == psg.WIN_CLOSED or event == 'CANCELAR':
                    break

                if event == 'ADICIONAR QUESTÃO':
                    janela2 = add_questao()
                    janela1.hide()
            
                if event == 'EXCLUIR QUESTÃO':
                    janela3 = rem_questao()
                    janela1.hide()
            
                if event == 'RESETAR BANCO DE QUESTÕES':
                    janela4 = resete()
                    janela1.hide()


            if window == janela2:
                if event == 'CANCELAR':
                    janela2.hide()
                    janela1.un_hide()

            
            if window == janela3:
                if event == 'CANCELAR':
                    janela3.hide()
                    janela1.un_hide()

    
            if window == janela4:
                if event == 'CANCELAR':
                    janela4.hide()
                    janela1.un_hide()

