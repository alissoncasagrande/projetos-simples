#Contador de Palavras 
#Escreva um programa que solicite ao usuário uma frase 
#e conte número de palavras presentes nela. O programa 
#deve exibir o resultado para o usuário.

while True:
    try:
        nome_arquivo = input("Digite o nome do arquivo de texto (com extensão .txt) (padrao: entrada.txt) (ou SAIR): ")
        if nome_arquivo.upper() == "SAIR":
            print("Encerrando o programa.")
            break
        if not nome_arquivo:
            nome_arquivo = 'entrada.txt'

        with open(nome_arquivo, 'r') as f:
            texto = f.read()

        palavras = texto.split()
        print(f"O número de palavras no arquivo é: {len(palavras)}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")



