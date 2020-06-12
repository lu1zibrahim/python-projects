# -*- coding: utf-8 -*-

# Jogo da Forca (Hangman)

# Import
import random

# criando o boneco

board = ['''

>>>>>>>>>>>>>>Hangman<<<<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
======== ''','''
+---+
|   |
o   |
    |
    |
    |
======== ''','''
+---+
|   |
o   |
|   |
    |
    |
    |
========''','''
   +---+
   |   |
   o   |
  /|   |
       |
       |
       |
========''','''
   +---+
   |   |
   o   |
  /|\  |
       |
       |
       |
========''','''
   +---+
   |   |
   o   |
  /|\  |
  /    |
       |
       |
========''','''
   +---+
   |   |
   o   |
  /|\  |
  / \  |
       |
       |
========'''
]

#class
letras_erradas = []
letras_certas = []
placar_letras = []
class Hangman:


       #método contructor
       def __init__(self,word):
              self.word = word
              print(board[0]+self.hide_word())
              self.guess()



       #método para adivinhar a letra
       def guess(self):
              print("Tente adivinhar qual que é a palavras secreta, ou sofra as consequências, muahahahah")
              letter1 = input("\nQual letra você tentará?\n")
              if letter1 in self.word:
                     if letter1 in letras_certas:
                            return letras_certas
                     elif self.word.count(letter1) > 1:
                            letras_certas.extend(letter1*self.word.count(letter1))
                            return letras_certas
                     else:
                            letras_certas.append(letter1)
                            return letras_certas
              else:
                     if letter1 in letras_erradas:
                            return letras_erradas
                     else: 
                            letras_erradas.append(letter1)
                            return letras_erradas

       #método para verificar se o jogo terminou
       def hangman_over(self):
              if len(letras_certas) == len(list(self.word)) or len(letras_erradas) == 6:
                     return False
              else:
                     return True
       #método para veriticar se o jogador venceu
       def hangman_won(self):
              if len(letras_certas) == len(list(self.word)):
                     print('\nParabéns! você venceu!!')
              else:
                     print('\nGame over! você perdeu.')
                     print('A palavra era '+ self.word)
              print('\nFoi bom jogar com você! Agora vá estudar!\n')
       #método para não mostrar a letra no board
       def hide_word(self):
              palavra_secreta = []
              palavra_secreta_final = ""
              for lett in list(self.word):
                     if lett in letras_certas:
                            palavra_secreta.append(lett)
                     else:
                            palavra_secreta.append(" _ ")
              return palavra_secreta_final.join(palavra_secreta)

       #método para checar o status do game e imprimir o board na tela
       def print_game_status(self):
              print(board[len(letras_erradas)]+self.hide_word())
              print(letras_certas)
              print(letras_erradas)



#função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
       with open("palavras.txt", "rt") as f:
                bank = f.readlines()
       return bank[random.randint(0,len(bank)-1)].strip()
#função main - execução do programa

def main():

       #objeto

       game = Hangman(rand_word())

       #enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter


       # Verificar o status do jogo

       game.print_game_status()

       #De acordo com o status, imprime mensagem na tela para o usuario

       while game.hangman_over() == True:
              game.guess()
              game.print_game_status()
       else:
              game.hangman_won()
              

#Executa o programa

if __name__ == "__main__":
       main()