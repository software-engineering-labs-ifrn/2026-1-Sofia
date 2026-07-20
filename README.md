# Calculadora Interativa no Terminal

Uma aplicação de linha de comando (CLI) intuitiva, robusta e desenvolvida em Python seguindo os princípios de Programação Orientada a Objetos (POO).

## 🎯 Contexto e Problema
Muitas vezes, desenvolvedores e estudantes precisam realizar cálculos rápidos sem sair do ambiente de desenvolvimento ou do terminal. Interfaces gráficas pesadas podem falhar ou consumir recursos desnecessários para tarefas simples.

Este projeto resolve esse problema entregando uma calculadora via terminal de rápida execução, com um menu interativo e, principalmente, à prova de falhas comuns de digitação ou erros matemáticos críticos.

## 🚀 Requisitos Gerais (Alto Nível)
* **Interface via Prompt/Terminal:** Menu textual interativo e limpo que guia o usuário em todas as etapas.
* **Operações Básicas:** Suporte a Soma, Subtração, Multiplicação e Divisão.
* **Operações Avançadas:** Suporte a Raiz Quadrada (`math.sqrt`) e Potenciação (`**`).
* **Tratamento de Exceções Robusto:** O sistema captura erros como divisão por zero, cálculo de raiz de números negativos e digitação de letras no lugar de números, impedindo que o programa quebre ou feche inesperadamente.
* **Tratamento Flexível de Entradas:** Aceita números decimais digitados tanto com ponto quanto com vírgula (ex: `5,5` ou `5.5`).
* **Formatação Inteligente de Saída:** Exibe números inteiros sem casas decimais desnecessárias (ex: exibe `5` em vez de `5.0`).

## 👥 Papéis dos Usuários (Atores)
* **Usuário Geral (Desenvolvedor/Estudante):** Interage com o terminal para realizar cálculos rápidos de forma sequencial.
* **Professor / Avaliador:** Analisa a conformidade dos critérios arquiteturais, legibilidade, tratamento de erros e modularização usando classes e métodos em Python.

## 🛠️ Stack Tecnológica
* **Linguagem:** Python (v3.12+)
* **Módulos Utilizados:** `math` (Biblioteca nativa do Python)
* **Paradigma:** Programação Orientada a Objetos (POO)
* **Arquitetura:** SOLID - Princípio da Responsabilidade Única (SRP)
* **Interface:** CLI (Interface de Linha de Comando)

## ⚙️ Pré-requisitos e Como Executar

### Pré-requisitos
Como o projeto utiliza estritamente as bibliotecas nativas do ecossistema Python, o único requisito é possuir o interpretador instalado:
* **Python 3.12** ou superior.

### Como Executar a Aplicação
1. Certifique-se de que está na raiz do projeto dentro do seu terminal.
2. Execute o comando apontando para o arquivo de inicialização contido no diretório de código-fonte (`src`):
   ```bash
   python src/main.py

## 📁 Estrutura do Projeto
```text
.
├── docs/                               # Centraliza toda a documentação do projeto
│   └── modelagem/                      # Artefatos de engenharia de software e diagramas UML
│       ├── diagramas_sequencia/        # Diretório com mapeamento dinâmico das User Stories
│       │   ├── DIAGRAMA_DE_SEQUENCIA.md # Relatório explicativo contendo os 7 diagramas Mermaid
│       │   ├── diagrama_sequencia_us01.png
│       │   ├── diagrama_sequencia_us02.png
│       │   ├── diagrama_sequencia_us03.png
│       │   ├── diagrama_sequencia_us04.png
│       │   ├── diagrama_sequencia_us05.png
│       │   ├── diagrama_sequencia_us06.png
│       │   └── diagrama_sequencia_us07.png
│       ├── CASO_DE_USO.md              # Documentação do escopo funcional sob a ótica do usuário
│       ├── caso_de_uso.png             # Renderização visual do Diagrama de Casos de Uso
│       ├── codigo_violando_solid.png   # Estado estático da classe original acoplada
│       ├── design-solid-correcoes.md   # Relatório descritivo da refatoração para o padrão SOLID
│       ├── diagrama_codigo_corrigido.png # Renderização da nova arquitetura desacoplada
│       ├── DIAGRAMA_DE_CLASSES.md      # Documentação da estrutura estática das classes (Mermaid)
│       ├── diagrama_de_classes.png     # Imagem do Diagrama de Classes final do sistema
│       └── USER_STORIES.md             # Engenharia de Requisitos: Critérios de Aceitação BDD
├── src/                                # Código-fonte de produção do sistema
│   └── main.py                         # Ponto de entrada estruturado sob o princípio SRP (SOLID)
├── .gitignore                          # Configuração de arquivos ignorados pelo Git
├── LICENSE                             # Termos de licença de uso do software
└── README.md                           # Documentação principal e guia do repositório
```

## 👨‍💻 Integrantes e Papéis
* **Sofia Barros Silva:** Desenvolvedor Principal (Responsável pela Arquitetura de Classes, Lógica das Operações Matemáticas, Fluxo do Menu no Terminal e Tratamento de Erros).