#imortar bibliotecas
import sys, pygame
from pygame.locals import*
from random import *

#inicia biblioteca
pygame.init()

#cria surface
size=(800,600)
screen = pygame.display.sent_mode(size)
#define um titulo para a janela
pygame.display.set_caption("papa Bolinhas")

#carrega imagem de fundo
imagem = pygame.image.load("imagem_fundo.png")

#define as cores em rgb
BLACK= (0,0,0)
WHITE= (0,0,0)
YELLOW=(255,255,0)
RED= (255,0,0)

#declaa a lista q controla a posição xy do papap bolinha

posicaoPapaBolinhas= [400,300]

#armazena, em uma lista, a velocidade de movimentação ddo papa bolinhas
velocidadePapaBolinhas=[5,5]

#cria variaveis com alores para controlar o posicionamento do circulo vermelho
X_vermelho= 0
Y_vermelho= 0

#controle de geração de circulo
criar = True
#formato da fonte
font = pygame.font.SysFont('sans',40)
placar= 0
#variavel clocl para controlar a velocidade de
#quadros por segundo

clock= pygame.time.Clock()

#cria objeto clock
CLOCKTICK = pygame.USEREVENT+1

#configurando o timer para exct a cada 1 s
pygame.time.set_timer(CLOCKTICK,1000)
temporizador = 60

#loop do jogo
while True
  #verifica se algum evento apareceu
  for event in pygame.event.get():
      #fecha app em eventos de saida
      if  event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      #captura evento relogio todo segundo
      if event.type==CLOCKTICK:
          temporizador = temporizador -1
#finaliza jogo
if temporizador== 0:
    break

#captura o evento de alguma tecla for pressionada
pressed = pygame.key.get_pressed()

if pressed[pygane.K_UP]:
    posicaoPapaBolinhas[1]-=velocidadePapaBolinhas[1]
if pressed[pygane.K_DOWN]:
    posicaoPapaBolinhas[1]+=velocidadePapaBolinhas[1]
if pressed[pygane.K_LEFT]:
    posicaoPapaBolinhas[0]-=velocidadePapaBolinhas[1]
if pressed[pygane.K_RIGTH]:
    posicaoPapaBolinhas[0]+=velocidadePapaBolinhas[1]
#att imagem de fundo da tela
screen.blit(imagem, (0,0))

#desenha circulo branco na tela

pygame.draw.circle(screen,WHITE,PosicaoPapaBolinhas,20)

#define a pos init da bolinha vermelha
if criar == True:
    X_vermelho= randint(20,580)
    Y_vermelho= 20
    criar = False
#Velocidade de queda do circulo vermelho
Y_vermelho+= 5


#posicionando bolinha vermelha
posiccaoBolasVermelhas= [X_vermelho,Y_vermelho]
#desenha o circulo vermelho com raio de tamanho 10
pygame.draw.circle(screen,RED,posicaiBolasVermelhas,10)



    
    
    

          












