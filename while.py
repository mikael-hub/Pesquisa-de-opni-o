# Pesquisa de satisfação
# Coleta o nome, idade e opinião de 50 entrevistados

TOTAL_ENTREVISTADOS = 50

qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")

    nome = input("Nome: ")

    # Validação da idade
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Idade inválida! Digite apenas números.")

    # Validação da opinião
    while True:
        try:
            opiniao = int(input(
                "Opinião sobre o atendimento:\n"
                "1 - EXCELENTE\n"
                "2 - BOM\n"
                "3 - RUIM\n"
                "Digite sua opção: "
            ))
            if opiniao in (1, 2, 3):
                break
            else:
                print("Opção inválida! Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite apenas números (1, 2 ou 3).")

    if opiniao == 1:
        qtd_excelente += 1
        print(f"{nome} avaliou o atendimento como EXCELENTE.")
    elif opiniao == 2:
        qtd_bom += 1
        print(f"{nome} avaliou o atendimento como BOM.")
    elif opiniao == 3:
        qtd_ruim += 1
        print(f"{nome} avaliou o atendimento como RUIM.")

print("\n===== RESULTADO FINAL DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostaBOM: {qtd_bom}")
print(f"Quantidade de respostas RUIM: {qtd_ruim}")