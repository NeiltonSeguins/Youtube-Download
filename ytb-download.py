from pytube import YouTube
import PySimpleGUI as sg

#Cria uma classe
class WindowsGen:
    def __init__(self):
        sg.theme('DarkGrey1')
        # Cria o Layout
        layout = [
            [sg.Text('Cole o link aqui', size=(30,1))],
            [sg.Input(key='link',size=(30,1))],
            [sg.Button('Download')],
            [sg.Output(size=(25,1))]
        ]

        # Cria e exibe a Janela
        self.janela = sg.Window('Youtube Downloader', layout)

    # Inicia a função principal do loop
    def Iniciar (self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Download':
                self.baixarVideo(valores)

    #Busca o endereço do vídeo e faz o download
    def baixarVideo(self,valores):
        link = valores['link']
        url = YouTube(str(link))
        video = url.streams.first()
        video.download()
        return print('Video baixado')


ger = WindowsGen()
ger.Iniciar()