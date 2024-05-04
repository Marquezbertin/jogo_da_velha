def criar_tabuleiro():
    """Cria um tabuleiro vazio 3x3."""
    return [[" " for _ in range(3)] for _ in range(3)]


def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro."""
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)


def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador venceu o jogo."""
    # Verifica linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verifica colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False


def fazer_jogada(tabuleiro, jogador, nome_jogador):
    """Permite que um jogador faça uma jogada."""
    while True:
        try:
            linha = int(input(f"{nome_jogador}, escolha a linha (0, 1 ou 2): "))
            coluna = int(input(f"{nome_jogador}, escolha a coluna (0, 1 ou 2): "))

            # Verifica se a jogada é válida
            if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador
                break
            else:
                print("Entrada inválida ou posição já ocupada. Tente novamente.")
        except ValueError:
            print(
                "Entrada inválida. Por favor, insira números válidos para linha e coluna."
            )


def jogo_da_velha():
    """Função principal para rodar o jogo da velha."""
    # Cria o tabuleiro
    tabuleiro = criar_tabuleiro()

    # Pede aos jogadores que insiram seus nomes
    nome_jogador_x = input("Por favor, insira o nome do jogador X: ")
    nome_jogador_o = input("Por favor, insira o nome do jogador O: ")

    # Define o jogador atual como X
    jogador_atual = "X"
    nome_jogador_atual = nome_jogador_x

    while True:
        # Imprime o tabuleiro
        imprimir_tabuleiro(tabuleiro)

        # Faz a jogada do jogador atual
        fazer_jogada(tabuleiro, jogador_atual, nome_jogador_atual)

        # Verifica se o jogador atual venceu
        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"{nome_jogador_atual} ({jogador_atual}) venceu!")
            break

        # Verifica se o jogo terminou em empate
        if all(all(celula != " " for celula in linha) for linha in tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        # Alterna os jogadores
        jogador_atual = "O" if jogador_atual == "X" else "X"
        nome_jogador_atual = nome_jogador_o if jogador_atual == "O" else nome_jogador_x


# Execute o jogo
jogo_da_velha()
