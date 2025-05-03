# bonequinho da forca
forca = [
" _______",  # linhas fixas da forca
"|/      |",

]

#palavra do jogo
palavra = "cenoura"
#vetor para armazenagem das letras acertadas
letras_corretas = ["_"] *len(palavra)
#contador de erros
erros = 0
#verificar quando o jogo continua ou termina
while erros < 6 and "_" in letras_corretas:
    for linha in forca: #<= mostrar a base da forca fixa
        print(linha)

# mostrar as partes do bonequinho conforme os erros
    if erros >= 1:
        print("|      (_)")  # cabeça
    else:
        print("|")

    if erros == 2:
        print("|       |")  # tronco
    elif erros == 3:
        print("|      \\|")  # tronco e o braço esquerdo
    elif erros >= 4:
        print("|      \\|/")  # tronco e os dois braços
    else:
        print("|")

    if erros == 5:
        print("|      /")  # perna esquerda
    elif erros >= 6:
        print("|      / \\")  # as duas pernas
    else:
        print("|")

    print("|___\n")
#mostrar a palavra com acertos e os tracinhos
    print("palavra: ", end=" ")
    for letras in letras_corretas:
        print(letras, end=" ")

    print("\n")

    tentativas  = input("Digite uma letra: ")
    #verificar se as letras das tentativas estao na palavra
    if tentativas in palavra:
        print(f"A letra {tentativas} está na palavra! ")
        for x in range (len(palavra)):
            if palavra[x] == tentativas:
                letras_corretas[x] = tentativas
    else:
        print(f"A letra '{tentativas}' NÃO está na palavra.")
        erros += 1


 #fim do jogo
if "_" not in letras_corretas:
    print("Parabéns! Você acertou a palavra!")
else:
    print("Você perdeu! A palavra era:", palavra)