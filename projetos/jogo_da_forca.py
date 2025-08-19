import random

palavras = ["python", "github", "programacao", "devops", "chatgpt"]
palavra = random.choice(palavras)
tentativas = 6
letras_usadas = []
palavra_oculta = ["_"] * len(palavra)

print("Bem-vindo ao Jogo da Forca!")

while tentativas > 0 and "_" in palavra_oculta:
    print("\nPalavra:", " ".join(palavra_oculta))
    print("Tentativas restantes:", tentativas)
    print("Letras usadas:", letras_usadas)

    letra = input("Digite uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já usou essa letra.")
        continue

    letras_usadas.append(letra)

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                palavra_oculta[i] = letra
    else:
        tentativas -= 1
        print("Letra incorreta!")

if "_" not in palavra_oculta:
    print("\nParabéns! Você descobriu a palavra:", palavra)
else:
    print("\nGame Over! A palavra era:", palavra)
