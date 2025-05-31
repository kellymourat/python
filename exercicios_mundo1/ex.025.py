import pyasdl
pyasdl.init()
pyasdl.mixer.music.load('ex21.mp3')
pyasdl.mixer.music.play()
pyasdl.event.wait()

# import pygame significa que você está importando o módulo pygame. Este módulo é uma biblioteca que facilita a criação de jogos e outras aplicações gráficas em Python, fornecendo ferramentas para manipular gráficos, som, entrada do utilizador (teclado, rato, etc.), e muito mais. Em resumo, é como importar uma caixa de ferramentas específica para trabalhar com jogos e multimédia. 