#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer
mixer.init()
#--COLOQUE A MÚSICA QUE DESEJAR
mixer.music.load('LoveInTheDark.mp3')
mixer.music.play()
x = input('Digite algo para parar...')