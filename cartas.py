     # =====================
     #        OVERALL
     # =====================
#Deck de cartas inspirado no jogo 'Fifa Street 2'

#Overall == maior atributo da carta

#1  Ronaldinho(BRA)      (95)
#2  Henry(FRA)           (94)
#3  Ronaldo(BRA)         (92)
#4  Rooney(ENG)          (92)
#5  Zidane(FRA)          (91)
#6  Buffon(ITA)          (90)
#7  Kaká(BRA)            (90)
#8  Adriano(BRA)         (89)
#9  Beckham(ENG)         (89)
#10 Eto'o(CAM)           (89)
#11 Cannavaro(ITA)       (88)
#12 C.Ronaldo(POR)       (88)
#13 Tévez(ARG)           (88)
#14 Gerrard(ENG)         (87)
#15 Messi(ARG)           (87)
#16 R.Carlos(BRA)        (87)
#17 Riquelme(ARG)        (87)
#18 Vieira(FRA)          (87)
#19 Ballack(GER)         (86)
#20 Lúcio(BRA)           (86)
#21 Puyol(SPA)           (86)
#22 Casillas(SPA)        (85)
#23 Figo(POR)            (85)
#24 Lampard(ENG)         (85)
#25 Pirlo(ITA)           (85)
#26 Cafú(BRA)            (84)
#27 Crespo(ARG)          (84)
#28 Deco(POR)            (84)
#29 Gattuso(ITA)         (84)
#30 Schweinsteiger(GER)  (84)
#31 Dida(BRA)            (83)
#32 Klose(GER)           (83)






     # =====================
     #        CARTAS
     # =====================
#Cartas em ordem alfabética

# 0 = chute, 1 = drible, 2 = velocidade, 3 = defesa

baralho = [
["Adriano(BRA)",         89, 84, 89, 58], #1
["Ballack(GER)",         86, 82, 82, 78], #2
["Beckham(ENG)",         89, 87, 87, 75], #3
["Buffon(ITA)",          74, 74, 84, 90], #4
["C.Ronaldo(POR)",       86, 88, 88, 66], #5
["Cafú(BRA)",            78, 84, 84, 84], #6
["Cannavaro(ITA)",       70, 70, 88, 88], #7
["Casillas(SPA)",        72, 72, 85, 85], #8
["Crespo(ARG)",          84, 80, 84, 66], #9
["Deco(POR)",            82, 84, 84, 70], #10
["Dida(BRA)",            68, 68, 83, 83], #11
["Eto'o(CAM)",           87, 85, 89, 68], #12
["Figo(POR)",            84, 85, 84, 71], #13
["Gattuso(ITA)",         78, 74, 78, 84], #14
["Gerrard(ENG)",         87, 84, 84, 78], #15
["Henry(FRA)",           92, 92, 94, 70], #16
["Kaká(BRA)",            88, 90, 90, 70], #17
["Klose(GER)",           83, 79, 83, 68], #18
["Lampard(ENG)",         85, 82, 82, 78], #19
["Lúcio(BRA)",           82, 76, 82, 86], #20
["Messi(ARG)",           85, 87, 87, 58], #21
["Pirlo(ITA)",           85, 85, 76, 76], #22
["Puyol(SPA)",           74, 74, 86, 86], #23
["Riquelme(ARG)",        87, 87, 80, 70], #24
["R.Carlos(BRA)",        87, 78, 87, 82], #25
["Ronaldo(BRA)",         92, 90, 92, 68], #26
["Ronaldinho(BRA)",      91, 95, 91, 74], #27
["Rooney(ENG)",          92, 88, 92, 82], #28
["Schweinsteiger(GER)",  82, 84, 84, 78], #29
["Tévez(ARG)",           88, 88, 88, 62], #30
["Vieira(FRA)",          78, 82, 87, 87], #31
["Zidane(FRA)",          91, 91, 80, 74]  #32
]

#O deck de cartas tinha vários problemas, o principal era que a estratégia "sempre escolher o maior atributo" ganhava 80% das vezes.
#Como os atributos eram em formato de escada (ex: a>b>c>d), era muito simples para o jogador humano sempre escolher o maior número, e se ele repetisse isso o jogo inteiro, a probabilidade de ganhar a partida era 80%.
#Fiz várias coisas para nerfar isso. Adicionei a mecânica de dominância (que só afeta o Jogador 1) e alterei o baralho para que as cartas tivessem vários atributos repetidos.
#Assim, quando o usuário joga, nao é tão óbvio qual atributo ele deve escolher. Quando o maior atributo é repetido (ex: chute 80, drible 80, velocidade 70 e defesa 60), a escolha entre chute ou drible requer uma decisão consciente por parte do usuário.
#A mecânica de dominância só se aplica ao jogador 1 pois o computador nao precisava receber nenhum nerf, considerando as simulações que eu fiz com Chat GPT. Atualmente, se o usuário adotar a estratégia "sempre escolher maior atributo" e, caso ele seja repetido, escolher qualquer um dos maiores, sua probabilidade de vencer é 60% e o computador 40%.
#Inicialmente o computador tinha 75% de chance de escolher estratégia 1 e 25% de chance de escolher estratégia 2, mas depois eu alterei para 66% e 33%.
#O baralho também foi balanceado de forma que não existam cartas 'dominadas'  ex: Ronaldinho 90, 92, 95, 70  vs  Lampard  87, 85, 85, 60.  Independente da escolha, Lampard sempre perde.
