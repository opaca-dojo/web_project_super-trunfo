     # =====================
     #         GERAL
     # =====================

input(" Bem-vindo ao ++ Super Trunfo FIFA STREET ++\n\n Inspirado no jogo 'Fifa Street 2', lançado em 2006 para Playstation 2\n Este jogo possui 32 cartas: jogadores de renome e lendas do futebol\n Divirta-se!\n ")
import random
from cartas import baralho
from funcoes import computador_ganha, usuario_ganha, empate
random.shuffle(baralho)
mesa = []
deck_jogador_1 = [] #Jogador 1 = usuário.
deck_jogador_2 = [] #Jogador 2 = computador
vez = random.randint(1, 2)  #Isso randomiza quem começa jogando.
while len(baralho) > 1:
    deck_jogador_1.append(baralho.pop(0))
    deck_jogador_2.append(baralho.pop(0))
dominancia = 0







     # =====================
     # LOOP PRINCIPAL DO JOGO
     # =====================

while len(deck_jogador_1) > 0 and len(deck_jogador_2) > 0:

    # Vez do usuário.
    if vez == 1:
        input(f"\n\n Sua vez:\n Sua carta é... *{deck_jogador_1[0][0]}*\n ")
        print(f" Os atributos do seu jogador são:\n  1. Chute - {deck_jogador_1[0][1]}\n  2. Drible - {deck_jogador_1[0][2]}\n  3. Velocidade - {deck_jogador_1[0][3]}\n  4. Defesa - {deck_jogador_1[0][4]}\n")
        escolha = int(input(" Escolha qual categoria você quer jogar:\n "))
        while escolha not in [1, 2, 3, 4]:   #Verifica se o valor digitado é válido e evita crash.
            escolha = int(input("\n Valor inválido, escolha um número de 1 a 4:\n "))
    
        # USUÁRIO GANHA
        if deck_jogador_1[0][escolha] > deck_jogador_2[0][escolha]:
            input(f"\n Você ganhou!\n A carta do seu oponente era *{deck_jogador_2[0][0]}* com *{deck_jogador_2[0][escolha]}* de atributo\n Você joga novamente.\n ")
            usuario_ganha(mesa, deck_jogador_1, deck_jogador_2)
            vez = 1
            dominancia += 1
            if dominancia >= 3:
                if random.randint(1, 2) == 2: #O jogo estava MUITO tendencioso para o jogador 1, ele ganhava aproximadamente 80% das vezes por isso introduzi a mecânica de Dominancia, para nerfar o jogador 1.
                    vez = 2                  #Eu simulei a winrate do jogo varias vezes, atualmente ela é 60% de vitória do usuário e 40% de vitória para o computador, quando o usuário utiliza a seguinte estratégia:
                    input("\n\n A torcida adversária reagiu...\n Perdemos o turno!\n ")                                  #Sempre escolhe o maior atributo, caso ele seja repetido, escolhe aleatoriamente entre os repetidos.
        
        # USUÁRIO PERDE
        elif deck_jogador_2[0][escolha] > deck_jogador_1[0][escolha]:
            input(f"\n Que pena!\n O seu oponente tinha *{deck_jogador_2[0][0]}* com {deck_jogador_2[0][escolha]} de atributo e ganhou a rodada!\n Você perdeu a vez\n ")
            computador_ganha(mesa, deck_jogador_1, deck_jogador_2)
            vez = 2
        
        # EMPATE
        elif deck_jogador_1[0][escolha] == deck_jogador_2[0][escolha]:
            input(f"\n Empate técnico! O seu oponente tinha *{deck_jogador_2[0][0]}* e ambas as cartas foram adicionadas ao monte\n Você perdeu a vez\n ")
            empate(mesa, deck_jogador_1, deck_jogador_2)
            vez = 2


    
    # Vez do computador.
    elif vez == 2:
        dominancia = 0
        input(f"\n\n Vez do seu oponente:\n Sua carta é... *{deck_jogador_1[0][0]}*\n ")
        print(f" Os atributos do seu jogador são:\n  1. Chute - {deck_jogador_1[0][1]}\n  2. Drible - {deck_jogador_1[0][2]}\n  3. Velocidade - {deck_jogador_1[0][3]}\n  4. Defesa - {deck_jogador_1[0][4]}")
        estrategia = random.randint(1, 3) #66% de chance estratégia 1; 33% de chance estratégia 2.
        if deck_jogador_2[0][0] in ["Ronaldinho(BRA)", "Henry(FRA)", "Buffon(ITA)"]: #Quando o computador tem uma dessas cartas, sempre escolhe o maior atributo.
            estrategia = 1
        if estrategia == 1 or estrategia == 3: #Estratégia 1: sempre escolhe o maior atributo. Se o maior atributo é repetido, ele randomiza.
            maior = max(deck_jogador_2[0][1:])
            repetidos = []
            for i in range(1, 5):
                if deck_jogador_2[0][i] == maior:
                    repetidos.append(i)
            escolha = random.choice(repetidos)
        elif estrategia == 2: #Estratégia 2: escolhe um dos 4 atributos aleatoriamente.
            escolha = random.randint(1, 4)
        if escolha == 1:
            atributo = "1. CHUTE"
        elif escolha == 2:
            atributo = "2. DRIBLE"
        elif escolha == 3:
            atributo = "3. VELOCIDADE"
        elif escolha == 4:
            atributo = "4. DEFESA"
        interacao = int(input(f"\n Seu oponente escolheu o atributo {atributo}!\n Insira o atributo da sua carta para ver quem vence\n "))
        while interacao != deck_jogador_1[0][escolha]:
            interacao = int(input(f"\n Valor incorreto! Insira o atributo da sua carta:\n "))

        # COMPUTADOR GANHA
        if deck_jogador_2[0][escolha] > deck_jogador_1[0][escolha]:
            input(f"\n Não deu!\n O seu oponente tinha *{deck_jogador_2[0][0]}* com atributo de *{deck_jogador_2[0][escolha]}* e ganhou a rodada!\n ")
            computador_ganha(mesa, deck_jogador_1, deck_jogador_2)
            vez = 2
            
        # COMPUTADOR PERDE
        elif deck_jogador_2[0][escolha] < deck_jogador_1[0][escolha]:
            input(f"\n Que sorte!\n Você ganhou a rodada e pegou a carta *{deck_jogador_2[0][0]}* do seu oponente\n ")
            usuario_ganha(mesa, deck_jogador_1, deck_jogador_2)
            vez = 1
            
        # EMPATE
        elif deck_jogador_2[0][escolha] == deck_jogador_1[0][escolha]:
            input(f"\n Empate técnico! O seu oponente tinha *{deck_jogador_2[0][0]}* e ambas as cartas foram adicionadas ao monte\n Você recuperou a vez\n ")
            empate(mesa, deck_jogador_1, deck_jogador_2)
            vez = 1



# Fim do jogo.           
if len(deck_jogador_1) == 0:
    input("\n\n GAME OVER...\n\n ")
elif len(deck_jogador_2) == 0:
    input("\n Parabéns, você venceu!\n ")
