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
* **Interface:** CLI (Interface de Linha de Comando)

## 👨‍💻 Integrantes e Papéis
* **Sofia Barros Silva:** Desenvolvedor Principal (Responsável pela Arquitetura de Classes, Lógica das Operações Matemáticas, Fluxo do Menu no Terminal e Tratamento de Erros).