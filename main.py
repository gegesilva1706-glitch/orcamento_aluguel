# --- Sistema de Orçamento de Aluguel ---

# Menu inicial
print("🏠 Bem-vindo ao sistema de Orçamento da Imobiliária R.M\n")

print("Tipos de locação disponíveis:")
print("1 - Apartamento (R$ 700,00 / 1 quarto)")
print("2 - Casa (R$ 900,00 / 1 quarto)")
print("3 - Estúdio (R$ 1200,00)\n")

tipo = int(input("Escolha o tipo de imóvel (1/2/3): "))

# Define valor base
if tipo == 1:
    aluguel = 700
    tipo_imovel = "Apartamento"
elif tipo == 2:
    aluguel = 900
    tipo_imovel = "Casa"
elif tipo == 3:
    aluguel = 1200
    tipo_imovel = "Estúdio"
else:
    print("Opção inválida!")
    exit()

# Quartos
if tipo in [1, 2]:
    quartos = int(input("Quantos quartos? (1 ou 2): "))
    if tipo == 1 and quartos == 2:
        aluguel += 200
    elif tipo == 2 and quartos == 2:
        aluguel += 250

# Garagem / estacionamento
if tipo in [1, 2]:
    garagem = input("Deseja incluir garagem? (s/n): ").lower()
    if garagem == "s":
        aluguel += 300
elif tipo == 3:
    vagas = int(input("Quantas vagas de estacionamento (0, 2 ou mais)? "))
    if vagas == 2:
        aluguel += 250
    elif vagas > 2:
        aluguel += 250 + ((vagas - 2) * 60)

# Desconto
if tipo == 1:
    criancas = input("Possui crianças? (s/n): ").lower()
    if criancas == "n":
        aluguel -= aluguel * 0.05

# Valor do contrato
valor_contrato = 2000
parcelas = int(input("Deseja parcelar o contrato em quantas vezes? (1-5): "))
valor_parcela = valor_contrato / parcelas

# Resultado final
print("\n--- ORÇAMENTO FINAL ---")
print(f"Tipo do imóvel: {tipo_imovel}")
print(f"Valor mensal do aluguel: R$ {aluguel:.2f}")
print(f"Valor total do contrato: R$ {valor_contrato:.2f}")
print(f"Parcelado em {parcelas}x de R$ {valor_parcela:.2f}\n")

# Geração de CSV (12 meses)
import csv

with open("orcamento_12_meses.csv", "w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Mês", "Valor Mensal"])
    for mes in range(1, 13):
        writer.writerow([mes, aluguel])

print("Arquivo 'orcamento_12_meses.csv' gerado com sucesso ✅")