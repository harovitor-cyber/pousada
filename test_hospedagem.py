# Entrada dos dados
# Backand: Bruno e Vitor 
# Sistema: Pousada Reserva
#
pessoas = int(input("Quantidade de pessoas: "))
tipo = int(input("Tipo do apartamento (1 ou 2): "))
diarias = int(input("Quantidade de diárias: "))

# Validação dos dados
if pessoas < 1 or pessoas > 6:
    print("Erro: a quantidade de pessoas deve ser de 1 a 6.")

elif tipo != 1 and tipo != 2:
    print("Erro: o tipo do apartamento deve ser 1 ou 2.")

elif diarias < 1 or diarias > 7:
    print("Erro: a quantidade de diárias deve ser de 1 a 7.")

else:
    # Seleção do preço do apartamento tipo 1
    if tipo == 1:
        if pessoas == 1:
            diaria = 20.00
        elif pessoas == 2:
            diaria = 28.00
        elif pessoas == 3:
            diaria = 35.00
        elif pessoas == 4:
            diaria = 42.00
        elif pessoas == 5:
            diaria = 48.00
        elif pessoas == 6:
            diaria = 53.00

    # Seleção do preço do apartamento tipo 2
    elif tipo == 2:
        if pessoas == 1:
            diaria = 25.00
        elif pessoas == 2:
            diaria = 34.00
        elif pessoas == 3:
            diaria = 42.00
        elif pessoas == 4:
            diaria = 50.00
        elif pessoas == 5:
            diaria = 57.00
        elif pessoas == 6:
            diaria = 63.00

    # Processamento
    total = diaria * diarias

    # Saída dos resultados
    print(f"Valor da diária: R$ {diaria:.2f}")
    print(f"Quantidade de diárias: {diarias}")
    print(f"Valor total: R$ {total:.2f}")

