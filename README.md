 🏠 Orçamento de Aluguel

Este projeto foi desenvolvido como parte da disciplina **Algorithmic Thinking & Introdução à Programação Orientada a Objetos**, do curso de **A#nálise e Desenvolvimento de Sistemas - Unifecaf**.

A aplicação tem como objetivo **automatizar o cálculo do orçamento de aluguel mensal** de imóveis, considerando diferentes tipos de locação, quantidade de quartos, garagem e descontos especiais.

---

## 🚀 Funcionalidades

- Cálculo automático do valor do aluguel
- Três tipos de imóveis:
  - Apartamento 🏢
  - Casa 🏡
  - Estúdio 🏙️
- Acréscimos por número de quartos e vagas
- Desconto de 5% para apartamentos sem crianças
- Cálculo e parcelamento do contrato imobiliário
- Geração automática de um arquivo `.csv` com as 12 parcelas mensais

---

## 🧠 Lógica do Programa

1. O usuário escolhe o tipo de imóvel, quantidade de quartos e se deseja garagem.
2. O programa soma os valores correspondentes aos acréscimos.
3. Se o imóvel for um apartamento sem crianças, aplica um desconto de 5%.
4. O valor do contrato (R$ 2000,00) é parcelado em até 5 vezes.
5. O sistema exibe o orçamento final e gera um arquivo CSV com os 12 meses.

---

## 💻 Como executar o projeto
ssss
### 1️⃣ Pré-requisitos
- [Python 3.12+](https://www.python.org/downloads/)
- Editor de código (recomendado: [Visual Studio Code](https://code.visualstudio.com/))

### 2️⃣ Clonar o repositório
No terminal, digite:
```bash
git clone https://github.com/gegesilva1706-glitch/orcamento_aluguel.git