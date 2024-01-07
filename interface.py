import PySimpleGUI as sg 
 # Layoyt: Cada linha da lista "['list']" é um texto ou interação com a janela criada
            # O "size" pode ser usado para colocar um tamanho dentro do elemento
            # A propriedade "key" é usada para identificar o elemento:
                # Com as "key" podemos pegar os valores que queremos usando o "self.values['key']"


class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkGreen')
        
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(50,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(50,0), key='idade')],
            [sg.Text('Quais Provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Yahoo', key='yahoo'), sg.Checkbox('Outlook', key='outlook')],
            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15,20), key='sliderVelocidade' )],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(40, 20))]
        ]
        # Janela: Colocamos o nome da janela e com qual variável ela vai trabalhar
        self.janela = sg.Window('Dados do Usuário').layout(layout)   
    
    def iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_yahoo = self.values['yahoo']
            aceita_outlook = self.values['outlook']
            aceita_cartoes = self.values['aceitaCartao']
            nao_aceita_cartoes = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita cartão: {aceita_cartoes}')
            print(f'não aceita cartão: {nao_aceita_cartoes}')
            print(f'velocidade script: {velocidade_script}')

tela = TelaPython()
tela.iniciar() 
