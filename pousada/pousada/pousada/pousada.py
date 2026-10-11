# ==========================================
# Sistema: Pousada Reserva
# Trabalho Avaliativo - UMC
# Back-end: Bruno e Vitor
# ==========================================

# Tabela de preços por tipo e quantidade de pessoas
PRECOS = {
    1: {
        1: 20.00,
        2: 28.00,
        3: 35.00,
        4: 42.00,
        5: 48.00,
        6: 53.00
    },
    2: {
        1: 25.00,
        2: 34.00,
        3: 42.00,
        4: 50.00,
        5: 57.00,
        6: 63.00
    }
}


# Entrada e validação de números inteiros
def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))

            if minimo <= valor <= maximo:
                return valor

            print(f"Erro: digite um valor de {minimo} a {maximo}.")

        except ValueError:
            print("Erro: digite um número inteiro válido.")


# Recebe e valida os dados da reserva
def ler_dados():
    print("\n--- Dados da reserva ---")

    while True:
        nome = input("Nome do cliente: ").strip()

        if nome:
            break

        print("Erro: informe o nome do cliente.")

    pessoas = ler_inteiro(
        "Quantidade de pessoas (1 a 6): ", 1, 6
    )

    tipo = ler_inteiro(
        "Tipo do apartamento (1 ou 2): ", 1, 2
    )

    diarias = ler_inteiro(
        "Quantidade de diárias (1 a 7): ", 1, 7
    )

    return {
        "nome": nome,
        "pessoas": pessoas,
        "tipo": tipo,
        "diarias": diarias
    }


# Calcula os valores da reserva
def calcular_reserva(dados):
    pessoas = dados["pessoas"]
    tipo = dados["tipo"]
    diarias = dados["diarias"]

    diaria = PRECOS[tipo][pessoas]
    total = diaria * diarias

    return {
        "nome": dados["nome"],
        "pessoas": pessoas,
        "tipo": tipo,
        "diarias": diarias,
        "valor_diaria": diaria,
        "valor_total": total
    }


# Organiza os dados para o relatório
def gerar_relatorio(reserva):
    return (
        "\n========== POUSADA RESERVA ==========\n"
        "       RELATORIO DA RESERVA\n"
        "=====================================\n"
        f"Cliente: {reserva['nome']}\n"
        f"Quantidade de pessoas: {reserva['pessoas']}\n"
        f"Tipo do apartamento: {reserva['tipo']}\n"
        f"Quantidade de diarias: {reserva['diarias']}\n"
        f"Valor da diaria: R$ {reserva['valor_diaria']:.2f}\n"
        "-------------------------------------\n"
        f"Valor total: R$ {reserva['valor_total']:.2f}\n"
        "====================================="
    )


# Controla as simulações
def main():
    while True:
        dados = ler_dados()

        reserva = calcular_reserva(dados)

        relatorio = gerar_relatorio(reserva)

        print(relatorio)

        continuar = input(
            "\nDeseja realizar outra simulacao? (s/n): "
        ).strip().lower()

        while continuar not in ("s", "n"):
            print("Opcao invalida. Digite s ou n.")
            continuar = input(
                "Deseja realizar outra simulacao? (s/n): "
            ).strip().lower()

        if continuar == "n":
            print("\nSistema encerrado.")
            break


# Inicializa o sistema
if __name__ == "__main__":
    main()