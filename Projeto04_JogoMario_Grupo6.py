from art import *
from random import choice, randint
from time import sleep
import pygame
import os

#Cria variavéis globais que serão usadas no jogo
global moedas, vidas

class Relogio:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self):
        return (self.horas > 3 or (self.horas == 3 and self.minutos > 0))

class Personagem():

    def luigi(self):
        #Luigi pode entrar no jogo para ajudar o jogador caso ele escolha SIM
        print("~.~."*20)
        luigi = input("Deseja acionar o seu irmão Luigi para te ajudar nessa aventura? \nDigite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while luigi not in ["sim","nao","não"]:
            luigi = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        if luigi == "sim":
            print("Luigi agora está com você, em algumas situações ele vai conseguir te ajudar.")
            return True
        else:
            print("Você está sozinho nessa aventura, boa sorte!")
            return False

    def yoshi(self):
        #É oferecido ao jogador a possibilidade de contar com a ajuda do Yoshi
        print("~.~."*20)
        yoshi = input("Deseja pedir ajuda para o Yoshi? \nDigite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while yoshi not in ["sim", "nao", "não"]:
            yoshi = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        if yoshi == "sim":
            print(r"""
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜🍐⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛📗📗⬛⬜⬛⬜⬜🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🍐🍐🍐🍐📗📗⬜⬜⬜🍐🍐⬛⬛⬜⬜⬜
⬜⬜⬜⬛🍐⬛🍐⬛🍐🍐🍐📗⬜📗🍐🍐⬛⬛⬜⬜⬜
⬜⬜⬛🍐🍐🍐🍐🍐🍐🍐🍐📗📗📗🍐🍐🍐⬛⬜⬜⬜
⬜⬜⬛🍐🍐🍐🍐🍐🍐🍐🍐🍐📗📗🍐🍐🍐⬛⬛⬜⬜
⬜⬜⬛🍐🍐🍐🍐🍐🍐🍐🍐📗📗⬜⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬛📗📗🍐🍐🍐🍐🍐📗📗⬛⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬛📗📗🍐🍐🍐📗📗⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛📗📗📗📗⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🍐🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜🍐🍐🍐⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🍐🍐⬛🍐🍐⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛🍐🍐🍐⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛📗⬛⬜⬜⬜⬛🍐🍐🍐🍐⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬛📗⬛⬜⬜⬜⬛📗🍐📗⬛🍐🍐⬛⬛⬛
⬜⬜⬜⬜⬜⬛📗⬛⬜⬜⬜⬛📗📗📗⬛🍐🍐🍐🍐🍐
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬛🍐🍐🍐🍐⬛⬛
⬜⬜⬜⬜⬜⬜⬜⬛🍐⬜⬜⬜🍐🍐🍐🍐🍐⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🍐⬜🍐🍐🍐⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬛🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🔴🔴⬛🔴🔴🔴⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🔴🔴⬛🔴🔴🔴🔴🔴🔴⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🔴🔴⬛🔴🔴🔴🔴🔴🔴⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
            """)
            print("Yoshi pode correr, pular ou cuspir fogo. Escolha o que ele irá fazer:")
            print("1 - Correr\n2 - Pular\n3 - Cuspir fogo")
            poder = int(input("Digite a opção desejada (apenas números): "))
            #Retorna inválido e pede novamente o input que está fora dos padrões
            while poder not in [1, 2, 3]:
                poder = int(input("Você não escolheu uma opção válida. \nDigite 1, 2 ou 3: "))
            if poder == 1:
                print("Você e Yoshi estão correndo")
            elif poder == 2:
                print("O Yoshi pulou em um inimigo")
            else:
                print("O Yoshi cospiu fogo em um inimigo")
        else:
            print("Você perdeu uma ajuda poderosa!")


    def donkeyKong(self):
        #Na entrada do castelo o jogador vai precisar enfrentar Donkey Kong, somente se vencer vai entrar no castelo
        print("~.~."*20)
        print("Parabéns! Você chegou na entrada do castelo. O Donkey Kong vai tentar te impedir de entrar, tome cuidado.")
        print("Vamos enfrentar o Donkey Kong para resgatar a Princesa Peach?")
        donkey = input("\nDigite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while donkey not in ["sim", "nao", "não"]:
            donkey = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()

        if donkey == "sim":
            #O resultado da batalha é decidido de acordo com escolhas no jogo
            print("Você enfrentou Donkey Kong com bravura e...")
            musica3 = Mecanica()
            musica3.musicaBatalha()
            load = ["█▒▒▒▒▒▒▒▒▒", "███▒▒▒▒▒▒▒", "█████▒▒▒▒▒", "███████▒▒▒", "█████████▒", "██████████"]
            for i in load:
                sleep(0.83)
                print(i, end=" ", flush=True)
            
            #O resultado da batalha é decidido de acordo com escolhas no jogo
            return "LUTOU"
        else:
            print("Dessa forma você não vai ter a possibilidade de resgatar a Princesa.")
            fugir = input("Deseja mesmo fugir da batalha? \nDigite [SIM] ou [NÃO] ").lower()
            #Retorna inválido e pede novamente o input que está fora dos padrões
            while fugir not in ["sim", "nao", "não"]:
                fugir = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
            #Se o jogador optar por não enfretar Donkey Kong o jogo encerra, pois ele não consegue entrar no Castelo
            if fugir == "sim":
                print("Você não resgatou a Princesa!")
                return "FUGIU"
            else:
                print("Sábia escolha… \nVocê enfrentou Donkey Kong com bravura e...")
                musica3 = Mecanica()
                musica3.musicaBatalha()
                #O resultado da batalha é decidido de acordo com escolhas no jogo
                print("Você enfrentou Donkey Kong com bravura e...")
                musica3 = Mecanica()
                musica3.musicaBatalha()
                load = ["█▒▒▒▒▒▒▒▒▒", "███▒▒▒▒▒▒▒", "█████▒▒▒▒▒", "███████▒▒▒", "█████████▒", "██████████"]
                for i in load:
                    sleep(0.83)
                    print(i, end=" ", flush=True)
                return "LUTOU"

    def princesa(self):
        #Derrotou o Bowser e chegou para resgatar a princesa
        resgate = ["Você conseguiu... Parabéns! Resgatou a Princesa Peach e agora vivem felizes no Reino dos Cogumelos!","Vish, você chegou tarde demais. Peach fugiu com o Mega Man!", "Vish, chegou cedo demais. Peach não estava pronta para te receber. Você vai ter que ficar com o Wario!"]

        print("Você DERROTOU o Bowser!!!!!!!!!!!!!!!!!!")
        print("~.~."*40)
        print("E...")
        print(choice(resgate))

class Interativos():

    def cogumelo(self):
        #Quando o jogador encontra  um cogumelo ele tem duas opções para interagir
        print("~.~."*20)
        print("Você encontrou dois Cogumelos, um \033[0;32m [VERDE] \033[0;0m e um \033[1;31m [VERMELHO]\033[0;0m")
        cogumelo = input("Qual você deseja escolher? \nDigite \033[0;32m [VERDE] \033[0;0m ou \033[1;31m [VERMELHO] \033[0;0m").lower() #Colorir a fonte no terminal
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while cogumelo not in ["verde", "vermelho"]:
            cogumelo = input("Você não escolheu uma opção válida. \nDigite [VERDE] ou [VERMELHO] ").lower()
        if cogumelo == "verde":
            print(r"""
📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘
📘📘📘📘📘📘⬛⬛⬛⬛⬛⬛⬛⬛⬛📘📘📘📘📘📘
📘📘📘📘⬛⬛📗📗📗📗📗📗⬜⬜⬜⬛⬛📘📘📘📘
📘📘📘⬛⬜⬜📗📗📗📗📗📗📗⬜⬜⬜⬜⬛📘📘📘
📘📘⬛⬜⬜📗📗📗📗📗📗📗📗📗⬜⬜⬜⬜⬛📘📘
📘📘⬛⬜📗📗⬜⬜⬜⬜📗📗📗📗📗📗⬜⬜⬛📘📘
📘⬛📗📗📗⬜⬜⬜⬜⬜⬜📗📗📗📗📗📗📗📗⬛📘
📘⬛📗📗📗⬜⬜⬜⬜⬜⬜📗📗📗📗📗⬜⬜📗⬛📘
📘⬛⬜⬜📗⬜⬜⬜⬜⬜⬜📗📗📗📗⬜⬜⬜⬜⬛📘
📘⬛⬜⬜📗📗⬜⬜⬜⬜📗📗📗📗📗⬜⬜⬜⬜⬛📘
📘⬛⬜⬜📗📗📗📗📗📗📗📗📗📗📗📗⬜⬜📗⬛📘
📘⬛⬜📗📗⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛📗📗📗⬛📘
📘📘⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛📘📘
📘📘📘⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛📘📘📘
📘📘📘⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛📘📘📘
📘📘📘📘⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛📘📘📘📘
📘📘📘📘📘⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛📘📘📘📘
📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘
            """)
            if vidas >= 4:
                tprint("Voce ganhou 100 moedas!", font="foxy")
                musica2 = Mecanica()
                musica2.musicaUP()
                return "MOEDAS"

            else:
                print("Você ganhou uma vida 💚")
                musica2 = Mecanica()
                musica2.musicaUP()
                return "VIDA"
        else:
            print(r"""
📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘
📘📘📘📘📘📘⬛⬛⬛⬛⬛⬛⬛⬛⬛📘📘📘📘📘📘
📘📘📘📘⬛⬛📕📕📕📕📕📕⬜⬜⬜⬛⬛📘📘📘📘
📘📘📘⬛⬜⬜📕📕📕📕📕📕📕⬜⬜⬜⬜⬛📘📘📘
📘📘⬛⬜⬜📕📕📕📕📕📕📕📕📕⬜⬜⬜⬜⬛📘📘
📘📘⬛⬜📕📕⬜⬜⬜⬜📕📕📕📕📕📕⬜⬜⬛📘📘
📘⬛📕📕📕⬜⬜⬜⬜⬜⬜📕📕📕📕📕📕📕📕⬛📘
📘⬛📕📕📕⬜⬜⬜⬜⬜⬜📕📕📕📕📕⬜⬜📕⬛📘
📘⬛⬜⬜📕⬜⬜⬜⬜⬜⬜📕📕📕📕⬜⬜⬜⬜⬛📘
📘⬛⬜⬜📕📕⬜⬜⬜⬜📕📕📕📕📕⬜⬜⬜⬜⬛📘
📘⬛⬜⬜📕📕📕📕📕📕📕📕📕📕📕📕⬜⬜📕⬛📘
📘⬛⬜📕📕⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛📕📕📕⬛📘
📘📘⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛📘📘
📘📘📘⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛📘📘📘
📘📘📘⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛📘📘📘
📘📘📘📘⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛📘📘📘📘
📘📘📘📘📘⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛📘📘📘📘
📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘
            """)
            tprint("Voce cresceu", font="cybermedium")
            musica2 = Mecanica()
            musica2.musicaUP()
            print("\033[1;31mCuidado para não esbarrar nos inimigos!\033[0;0m")
            return "CRESCEU"

    def kart(self):
        #O jogador tem a opção de escolher usar o Mario Kart
        print("~.~."*20)
        print("Você ganhou a opção de usar o Mario Kart")
        kart = input("Deseja aproveitar? Digite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while kart not in ["sim", "nao", "não"]:
            kart = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        #Se o jogador escolher sim, ele chega mais rápido ao Castelo
        if kart == "sim":
            print("Você está correndo de Kart, tome cuidado para não bater em nada.")
            return True
        else:
            print("Parece que você não vai conseguir chegar ao Castelo dessa forma, mas não desista.")
            return False

    def moedas(self, moedas):
        #O jogador se depara com moedas e pode escolher coletar ou ignorar
        print("~.~."*20)
        moeda = input("Oba, apareceram moedas no seu caminho, você deseja coletar? \nDigite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while moeda not in ["sim", "nao", "não"]:
            moeda = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        #Controla o número de moedas coletadas
        if moeda == "sim":
            moedas += 50
            return moedas
        else:
            return moedas

    def goomba(self):
        #O Goomba aparece e é decidido na sorte se o jogador venceu ou perdeu a batalha
        print(r"""

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░░░░░
░░░░░░░░░▄██▄▀░░░░░░░░░░░░▀▄██▄░░░░░░░░░
░░░░░░░░░░░███░░░░░░░░░░░░███░░░░░░░░░░░
░░░░░░░░░░█░▀██░░░░░░░░░░██▀░█░░░░░░░░░░
░░░░░░░░░█░░░▄██▄░░░░░░▄██▄░░░█░░░░░░░░░
░░░░░░░░▄▀░▄▀──▀█▄░░░░▄█▀──▀▄░▀▄░░░░░░░░
░░░░░░░▄▀░▄▀───▄─██░░██─▄───▀▄░▀▄░░░░░░░
░░░░░▄▀░░░█───███─█░░█─███───█░░░▀▄░░░░░
░░░▄▀░░░░░█────▀──█░░█──▀────█░░░░░▀▄░░░
░▄▀░░░░░░░█──────█░░░░█──────█░░░░░░░▀▄░
█░░░░░▄░░░░▀▄▄▄▄▀░░░░░░▀▄▄▄▄▀░░░░▄░░░░░█
█░░░░░▌▀▄░░░░░░░░░░░░░░░░░░░░░░▄▀▐░░░░░█
█░░░░▐▄▄▄█▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄█▄▄▄▌░░░░█
█░░░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀░░░░█
░▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▀░
░░░▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░▄▄▀▀▀▀▄░░░░░░░░░░░░▄▀▀▀▀▄▄░░░░░░░
░░░░░▄▀░░░░░░░▀▄▄▄▄▄▄▄▄▄▄▀░░░░░░░▀▄░░░░░
░░░░░█░░░░░░░░░░░▄▀░░▀▄░░░░░░░░░░░█░░░░░
░░░░░░▀▄░░░░░░░▄▀░░░░░░▀▄░░░░░░░▄▀░░░░░░
░░░░░░░░▀▀▀▀▀▀▀░░░░░░░░░░▀▀▀▀▀▀▀░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

""")
        goomba = randint(1,2)
        escolha = int(input("Você já seguiu bastante pela floresta. Cuidado, um Goomba apareceu! Escolha rápido [1] ou [2] para derrotá-lo: "))
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while escolha not in [1, 2]:
            escolha = int(input("Você não escolheu uma opção válida. \nDigite [1] ou [2] apenas: "))
        if goomba == escolha:
            print("Você derrotou o Goomba!")
            return True
        else:
            print("Você não derrotou o Goomba e perdeu 1 vida")
            return False


    def planta(self):
        #A Planta Carnívora aparece e o jogador pode pular ou desviar
        print(r"""
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛🔴🔴⬜🔴🔴⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🔴🔴🔴🔴🔴⬛⬛⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🔴🔴🔴⬜⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬛🔴⬜🔴🔴⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛🔴🔴🔴⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🔴🔴🔴⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🔴⬜⬛⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬛🔴🔴⬛⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬛🔴🔴⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬛🔴🔴⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬛⬜🔴🔴⬛⬛⬛⬛⬛⬛🔴🔴⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🔴🔴🔴🔴🔴🔴🔴🔴🔴⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🔴🔴⬜🔴🔴🔴⬜🔴🔴⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🔴🔴🔴🔴🔴⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬜⬜⬜⬛🍐📗⬛⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬜⬛🍐🍐⬛⬛⬜⬛🍐📗⬛⬜⬛⬛🍐📗⬛⬜⬜
⬜⬜⬛🍐⬛🍐🍐⬛⬛🍐📗⬛⬛🍐🍐⬛📗⬛⬜⬜
⬜⬜⬛🍐⬛📗📗🍐⬛🍐📗⬛🍐📗📗⬛📗⬛⬜⬜
⬜⬜⬛🍐📗⬛📗🍐⬛🍐📗⬛🍐📗⬛📗📗⬛⬜⬜
⬜⬜⬜⬛📗📗⬛📗⬛🍐📗⬛📗⬛📗📗⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛📗⬛📗🍐📗📗⬛📗⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛🍐📗⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬛🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐⬛⬜
⬜⬛📗📗📗📗📗📗📗📗📗📗📗📗📗📗📗📗⬛⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬜⬜⬜⬛🍐🍐📗📗🍐📗🍐📗🍐🍐⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🍐🍐📗📗📗🍐📗🍐🍐🍐⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🍐🍐📗📗🍐📗🍐📗🍐🍐⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🍐🍐📗📗📗🍐📗🍐🍐🍐⬛⬜⬜⬜⬜
        """)
        escolha = input("Cuidado, uma Planta Carnívora!\nEscolha [PULAR] ou [DESVIAR]: ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while escolha not in ["pular","desviar"]:
            escolha = input("Você não escolheu uma opção válida. \nDigite [PULAR] ou [DESVIAR] apenas: ")
        if escolha == "pular":
            print("Ops, a planta estava com a boca aberta e te mordeu!\nVocê perdeu 1 vida")
            return False
        else:
            print("Você correu da Planta Carnívora e não perdeu muito tempo!")
            musica2 = Mecanica()
            musica2.musicaUP()
            return True

class Mecanica():

    def musicaFundo(self):
        pygame.mixer.init()
        pygame.mixer.music.load('mariobros.mp3')
        pygame.mixer.music.play()

    def musicaGameOver(self):
        pygame.init()
        if os.path.exists('GAMEOVER_MARIO.mp3'):
            pygame.mixer.music.load('GAMEOVER_MARIO.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(10)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')

    def musicaVitoria(self):
        pygame.init()
        if os.path.exists('VENCER_MARIO.mp3'):
            pygame.mixer.music.load('VENCER_MARIO.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(10)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')

    def musicaBatalha(self):
        pygame.mixer.init()
        pygame.mixer.music.load('BATALHA_MARIO.mp3')
        pygame.mixer.music.play()
    
    def musicaUP(self):
        pygame.mixer.init()
        pygame.mixer.music.load('UP.mp3')
        pygame.mixer.music.play()


class Castelo():

    def portas(self):
        #Depois de enfrentar e ganhar do Donkey Kong ele finalmente chega até o Castelo
        print("~.~."*20)
        print("Você conseguiu entrar no Castelo, agora falta pouco para resgatar a Princesa… escolha uma porta")
        porta = input("Porta de Madeira ou Porta de Ferro? \nDigite [MADEIRA] ou [FERRO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while porta not in ["madeira", "ferro"]:
            porta = input("Você não escolheu uma opção válida. \nDigite [MADEIRA] ou [FERRO] ").lower()
        #Indepente da porta que o jogador escolha, ele vai encontrar o Bowser
        if porta == "madeira":
            print("Que pena, a Princesa não está na PORTA DE MADEIRA!\nAgora você vai enfrentar o Bowser e se vencer vai se encontrar com a Princesa Peach.")
        else:
            print("Que pena, a Princesa não está na PORTA DE FERRO!\nAgora você vai enfrentar o Bowser e se vencer vai se encontrar com a Princesa Peach.")

    def batalhaFinal(self):
        #Batalha final com o Bowser para salvar a Princesa Peach
        espada = art("sword7")
        print(espada)
        print("Você pode escolher uma das opções a seguir para te ajudar")
        opcoes = ["1 - Yoshi", "2 - Cogumelo Vermelho", "3 - Estrela"]
        for i in opcoes:
            print(i)
        print("Quem vai te ajudar a enfrentar o Bowser? Pense e escolha estrategicamente!")
        musica3 = Mecanica()
        musica3.musicaBatalha()
        chefao = int(input("Escolha sua opção (apenas números): "))
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while chefao not in [1, 2, 3]:
                chefao = int(input("Você não escolheu uma opção válida. \nDigite 1, 2 ou 3: "))
        if chefao == 1:
            print("Quando você perder a vida, o Luigi entra no seu lugar para continuar batalhando.")
        elif chefao == 2:
            print("O Yoshi vai lutar com você, ele pode te ajudar a derrotar o seu inimigo.")
        elif chefao == 3:
            print("Você está grande e poderoso, ótima escolha!")
        else:
            print("Você está invencível por 30 segundos, aproveite!")
            #Inicia a contagem do timer
            timer = 0
            while timer < 30:
                sleep(1)
                timer += 1
                print("-", end=" ")
        print("\nFIM DO SEU PODER")


#Inicia a contagem das vidas
vidas = 4

#Inicia a contagem de moedas
moedas = 0

while True:
    #Exibe o nome do jogo e menu
    tprint("MARIO", font="block")
    tprint("  A O   R E S G A T E", font="thin")

    #Pergunta para o jogador se deseja iniciar ou não o jogo
    iniciar = input("Você deseja iniciar o jogo? \nDigite [SIM] ou [NÃO] ").lower()

    #Valida a opção digitada e pede novamente, caso seja inválido
    while iniciar not in ["sim","nao","não"]:
        iniciar = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
    #O jogo funciona até o jogador decidir não jogar mais
    if iniciar == "sim":
        #Inicia a música de fundo
        musica1 = Mecanica()
        musica1.musicaFundo()

        #Conta a história para o jogador entender o contexto
        enredo = "O Reino dos Cogumelos foi invadido por criaturas conhecidas como Goombas e, usando a magia de seu rei Bowser, transformaram alguns habitantes em plantas carnívoras..."
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        continuar = input("\nPressione enter para continuar")

        print("~.~."*20)
        enredo = "A Princesa Peach foi sequestrada pois apenas ela detém o poder de desfazer essa magia e salvar o Reino... "
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        print()
        print("~.~."*20)

        enredo = "Cabe a você, Mario, salvar a princesa e libertar o reino de Bowser. Você está pronto?"
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        continuar = input("\nPressione enter para continuar")

        #Oferece o Luigi para ser selecionado como ajudante
        luigi = Personagem()
        luigiPersonagem = luigi.luigi()
        continuar = input("Pressione enter para continuar")

        #Informa o jogador que ele vai ter um tempo para concluir o jogo
        print("~.~."*20)
        print(f"Tome cuidado com o Goomba e com a Planta Carnívora... Eles podem tirar suas moedas ou suas vidas... Você começa com {vidas} vidas. E atenção, você tem no máximo 3 horas para concluir essa missão, você está correndo contra o tempo!")
        tempo = Relogio()
        print(f"Início: {tempo}")

        #Oferece a opção de coletar moedas
        moeda = Interativos()
        moedas = moeda.moedas(moedas)
        print(f"Você tem {moedas} moedas")
        tempo.avancaTempo(20)
        print(f"Tempo de jogo: {tempo}")
        continuar = input("\nPressione enter para continuar")

        #O Goomba aparece, e o jogador pode derrotar ou perder uma vida
        goomba = Interativos()
        goombaInterativo = goomba.goomba()
        if goombaInterativo == False:
            vidas -= 1
            print(f"Você tem {vidas} vidas")
            tempo.avancaTempo(30)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        else:
            tempo.avancaTempo(10)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        #Oferece a opção de coletar moedas
        moeda = Interativos()
        moedas = moeda.moedas(moedas)
        print(f"Você tem {moedas} moedas")
        if moedas == True:
            tempo.avancaTempo(50)
            print(f"Tempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        else:
            tempo.avancaTempo(20)
            print(f"Tempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        #Oferece a opção de usar o Kart
        kart = Interativos()
        marioKart = kart.kart()
        if marioKart == True:
            tempo.avancaTempo(10)
            print(f"Tempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        else:
            tempo.avancaTempo(50)
            print(f"Tempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        
        #Uma planta carnívora aparece, e o jogador pode derrotar ou perder suas moedas ou vida
        carnivora = Interativos()
        planta = carnivora.planta()
        if planta == False:
            vidas -= 1
            print(f"Você tem {vidas} vidas")
            tempo.avancaTempo(40)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        else:
            tempo.avancaTempo(10)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        #Recomeça a música de fundo
        musica1 = Mecanica()
        musica1.musicaFundo()
        enredo = "Deixa eu te contar uma coisa... acho que esqueci de mencionar... Depois de viajar por várias partes do reino e vencer os inimigos ao longo do caminho, você chegará ao Castelo. Cuidado! Apenas após derrotar o Bowser no tempo certo, que a princesa será libertada e o Reino dos Cogumelos será salvo!"
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        
        continuar = input("\nPressione enter para continuar")

        cogumelo = Interativos()
        cogumeloInterativo = cogumelo.cogumelo()

        if cogumeloInterativo == "MOEDA":
            moedas += 100
            print(f"Você tem {moedas} moedas")
            tempo.avancaTempo(10)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        elif cogumeloInterativo == "VIDA":
            vidas += 1
            print(f"Você tem {vidas} vidas")
            tempo.avancaTempo(50)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        else:
            tempo.avancaTempo(30)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        #Mario já consegue visualizar o Castelo e entra em ação o Donkey Kong
        print(r"""
                    |>>>                        |>>>
                    |                           |
                _  _|_  _                   _  _|_  _
               | |_| |_| |                 | |_| |_| |
               \  .      /                 \ .    .  /
                \    ,  /                   \    .  /
                 | .   |_   _   _   _   _   _| ,   |
                 |    .| |_| |_| |_| |_| |_| |  .  |
                 | ,   | .    .     .      . |    .|
                 |   . |  .     . .   .  ,   |.    |
     ___----_____| .   |.   ,  _______   .   |   , |---~_____
_---~            |     |  .   /+++++++\    . | .   |         ~---_
                 |.    | .    |+++++++| .    |   . |              ~-_
              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~
""")
        donkeykong = Personagem()
        donkeyPersonagem = donkeykong.donkeyKong()
        if donkeyPersonagem == "LUTOU":
            if luigiPersonagem == True:
                print("\nVENCEU pois seu irmão Luigi te ajudou")
                print("~.~."*20)
                porta = Castelo()
                porta.portas()
                bowser = Castelo()
                bowser.batalhaFinal()
                
            else:
                print("\nPERDEU pois não estava com seu irmão Luigi")
                tprint("Game Over",font="starwars")
                musica4 = Mecanica()
                musica4.musicaGameOver()
                break
        else:
            tprint("Game Over",font="starwars")
            musica4 = Mecanica()
            musica4.musicaGameOver()
            break

        break
    
    else:
        tprint("Game Over",font="starwars")
        musica4 = Mecanica()
        musica4.musicaGameOver()
        break