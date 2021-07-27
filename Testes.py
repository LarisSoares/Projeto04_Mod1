# from pygame import mixer

# mixer.init()
# mixer.music.load('mariobros.mp3')
# mixer.music.play()

# x = input('Digite a tecla que quiser parar...')

from time import sleep

enredo = "O Reino dos Cogumelos foi invadido por criaturas conhecidas como Goombas e, usando a magia de seu rei Bowser, transformaram alguns habitantes em plantas carnívoras..."
for letra in enredo:
    sleep(0.05)
    print(letra, end='', flush=True)