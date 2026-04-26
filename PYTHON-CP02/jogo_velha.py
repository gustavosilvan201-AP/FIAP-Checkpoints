velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def exibir_velha(tab):
    for linha in tab:
        print(" | ".join(linha))
        print("-" * 9)

def jogada_valida(tab, linha, coluna):
    if 0 <= linha <= 2 and 0 <= coluna <= 2:
        return tab[linha][coluna] == " "
    return False

def verificar_vencedor(tab):
    for l in range(3):
        if tab[l][0] == tab[l][1] == tab[l][2] !=" ":
            return tab[l][0]
        
    for c in range(3):
        if tab[0][c] == tab[1][c] == tab[2][c] !=" ":
            return tab[0][c]
    
    if tab[0][0] == tab[1][1] == tab[2][2] !=" ":
            return tab[1][1]
        
    if tab[0][2] == tab[1][1] == tab[2][0] !=" ":
            return tab[1][1]
    return None

def verificar_empate(tab):
    for linha in tab:
        if " " in linha:
            return False
    return True

def jogar():
    velha = [[" ", " ", " "] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_velha(velha)
        print(f"Turno do jogador {jogador_atual}")

        linha = int(input("Escolha a linha (0, 1 ou 2): "))
        coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

        if jogada_valida(velha, linha, coluna):
            velha[linha][coluna] = jogador_atual

            vencedor = verificar_vencedor(velha)
            if vencedor is not None:
                exibir_velha(velha)
                print(f"Fim de jogo! O jogador {vencedor} venceu!")
                break

            if verificar_empate(velha):
                exibir_velha(velha)
                print("Fim de jogo! Deu empate (velha).")
                break
            
            if jogador_atual == "X":
                jogador_atual = "O"
            else:
                jogador_atual = "X"

        else:
            print("jogada inválida! Esse espaço já está ocupado ou não existe. Tente novamente.")
            print("-" * 30)

jogar()