"""
Faça um programa em Python que abre e reproduza  o áudio de um arquivo MP3.
"""

from pygame import mixer
mixer.init()
mixer.music.load('Desafio21.mp3')
mixer.music.play()

