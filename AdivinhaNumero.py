#Bibliotecas
from random import randint, random
import emoji
from time import sleep
import pygame
pygame.init()

#Contadores
contador = 0
contador2 = 0

#Efeitos
perdi = pygame.mixer.Sound('gameover.mp3.wav')
ganhei = pygame.mixer.Sound('coin.mp3.wav')
encerrei = pygame.mixer.Sound('winningmusic.wav')

#Cabeçário
print('--='*19)
print('Vou pensar em um número entre 0 e 5...Tente Adivinhar...')
print('--='*19)

#Jogo
while True:
    numero = randint(0,5)
    palpite = input('Em que número eu pensei?')
    print('\nPROCESSANDO...')
    sleep(1)
    if int(numero) != int(palpite):
        contador = contador + 1
        perdi.play()
        print(emoji.emojize(f'\n\033[1;31mGANHEI\033[m! :party_popper: :astonished_face: Você disse {palpite}, mas eu pensei em {numero}. Mais sorte na próxima!'))
    elif int(numero) == int(palpite):
        contador2 = contador2 + 1
        ganhei.play()
        print(emoji.emojize(f'\nUé...mas COMO?!:anger_symbol: :angry_face: Você me \033[0;32mvenceu\033[m...você disse {palpite} e eu pensei em {numero}...'))
    repeticao = input('\nQuer jogar de novo?').strip()
    while repeticao.upper()[0] != 'S' and repeticao.upper()[0] != 'N':
        repeticao = input(emoji.emojize('Não entendi :thinking_face:, sim ou não?')).strip()
    if repeticao.upper()[0] == 'N':
        print(emoji.emojize(f'Aah, mas já?:sad_but_relieved_face:\nVocê ganhou \033[0;32m{contador2}\033[m vez(es) e perdeu \033[0;31m{contador}\033[m vez(es)!\nObrigade por jogar comigo! '))
        encerrei.play()
        break