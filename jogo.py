import pygame
import time
import random

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

tamanho_celula = 20
relogio = pygame.time.Clock()
velocidade = 10

def desenhar_cobrinha(tamanho_celula, lista_cobrinha):
    for x in lista_cobrinha:
        pygame.draw.rect(tela, VERDE, [x[0], x[1], tamanho_celula, tamanho_celula])

def mostrar_pontuacao(pontuacao):
    pygame.font.init()
    fonte = pygame.font.SysFont(None, 35)
    texto = fonte.render("Pontuação: " + str(pontuacao), True, BRANCO)
    tela.blit(texto, [10, 10])

def mensagem_game_over(pontuacao):
    tela.fill(PRETO)
    pygame.font.init()
    fonte = pygame.font.SysFont(None, 50)
    texto = fonte.render("Você perdeu! Pontuação Final: " + str(pontuacao), True, VERMELHO)
    texto_rect = texto.get_rect(center=(largura_tela / 2, altura_tela / 2 - 30))
    tela.blit(texto, texto_rect)

    fonte_instrucoes = pygame.font.SysFont(None, 35)
    instrucoes = fonte_instrucoes.render("Pressione C para jogar novamente ou Q para sair", True, BRANCO)
    instrucoes_rect = instrucoes.get_rect(center=(largura_tela / 2, altura_tela / 2 + 30))
    tela.blit(instrucoes, instrucoes_rect)

    pygame.display.update()

def jogo():
    game_over = False
    game_close = False
    pontuacao = 0

    x_cobrinha = largura_tela / 2 
    y_cobrinha = altura_tela / 2

    x_cobrinha_mudanca = 0
    y_cobrinha_mudanca = 0

    lista_cobrinha = []
    comprimento_cobrinha = 1

    comida_x = round(random.randrange(0, largura_tela - tamanho_celula) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_celula) / 20.0) * 20.0

    while not game_over:
        while game_close == True:
            mensagem_game_over(pontuacao)

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cobrinha_mudanca = -tamanho_celula
                    y_cobrinha_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cobrinha_mudanca = tamanho_celula
                    y_cobrinha_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_cobrinha_mudanca = -tamanho_celula
                    x_cobrinha_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_cobrinha_mudanca = tamanho_celula
                    x_cobrinha_mudanca = 0
        
        if x_cobrinha >= largura_tela or x_cobrinha < 0 or y_cobrinha >= altura_tela or y_cobrinha < 0:
            game_close = True
        x_cobrinha += x_cobrinha_mudanca
        y_cobrinha += y_cobrinha_mudanca
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_celula, tamanho_celula])
        lista_cobrinha.append([x_cobrinha, y_cobrinha])
        if len(lista_cobrinha) > comprimento_cobrinha:
            del lista_cobrinha[0]
        
        for x in lista_cobrinha[:-1]:
            if x == [x_cobrinha, y_cobrinha]:
                game_close = True
        
        desenhar_cobrinha(tamanho_celula, lista_cobrinha)
        mostrar_pontuacao(pontuacao)

        pygame.display.update()

        if x_cobrinha == comida_x and y_cobrinha == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_celula) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_celula) / 20.0) * 20.0
            comprimento_cobrinha += 1
            pontuacao += 1

        relogio.tick(velocidade)

    pygame.quit()

if __name__ == "__main__":
    jogo()
