import os
game = [[".",".","."],[".",".","."],[".",".","."]]
vitoria = ((0,0,0,1,0,2),(1,0,1,1,1,2),(2,0,2,1,2,2),(0,0,1,1,2,2),(2,0,1,1,0,2))
jogadas = 0  
ganhou = False
# =============== MONTA O JOGO NA TELA ===============
def mostrartela():
    contador = 0
    os.system('cls')
    print "JOGO DA VELHA"
    print "  0   1   2"
    for i,j,z in game:
        print "{0} {1} | {2} | {3}".format(int(contador),i,j,z)
        if contador < 2:
            print " ---+---+---"
        contador+=1
# =============== TESTA A CONDIÇÃO DE VITORIA NOS CASOS DENTRO DO JOGO ===============
def testV(i0,j0,i1,j1,i2,j2,vez):
    if game[i0][j0].find(vez) != -1 and game[i1][j1].find(vez) != -1 and game[i2][j2].find(vez) != -1:
        global ganhou
        ganhou = True
# =============== AUGORITMO DO JOGO ===============
def jogo():
    global jogadas
    global ganhou
    vez = ""
    # ********* LOOP DO JOGO *********
    while True:
        # ********* IMPRESSÃO DO JOGO *********
        mostrartela()
        # ********* CONDIÇÕES DE FIM DE JOGO *********
        if jogadas >= 9:
            print "\nDeu velha! Fim de jogo."
            raw_input()
            break
        if ganhou:
            print "\n({0}) ganhou! Fim de jogo.".format(vez)
            raw_input()
            break
        # ********* ENTRADA DOS JOGADORES *********
        print "\nVez numero: {0}".format(jogadas)
        i = int(raw_input("Linha..: "))
        if i < 0 or i > 2:
            print "Indice da linha invalido, tente 0, 1 ou 2."
            raw_input()
            # ------ RESET DE INPUT INVALIDO ------
            jogo()
        j = int(raw_input("Coluna.: "))
        if j < 0 or j > 2:
            print "Indice da coluna invalido, tente 0, 1 ou 2."
            raw_input()
            # ------ RESET DE INPUT INVALIDO ------
            jogo()
        # ********* TESTE DE INPUT VALIDO *********
        if game[i][j].find("x") != -1 or game[i][j].find("o") != -1:
            print "Posicao invalida, jogue novamente."
            raw_input()
            jogo()
        # ********* LEITURA DAS JOGADAS *********
        if jogadas % 2 == 0:
            game[i][j] = "x"
            vez = "x"
        else:
            game[i][j] = "o"
            vez = "o"
        # ********* TESTE DE VITORIA *********
        for i in vitoria:
            testV(i[0],i[1],i[2],i[3],i[4],i[5],vez)
        jogadas+= 1
# =============== INICIO DO JOGO ===============
jogo()