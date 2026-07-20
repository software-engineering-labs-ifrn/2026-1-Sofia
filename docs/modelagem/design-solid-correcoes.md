# Relatório de Aplicação dos Conceitos SOLID

Este documento apresenta as violações de design de software identificadas no estado inicial do projeto da Calculadora e detalha as correções estruturais realizadas para aderir aos princípios SOLID, especificamente o **SRP (Single Responsibility Principle - Princípio da Responsabilidade Única)**.

---

## 1. Princípio Violado: SRP (Single Responsibility Principle)

O SRP dita que *"uma classe deve ter um, e apenas um, motivo para mudar"*. Na arquitetura inicial do projeto, a classe `Calculator` centralizava todas as funções do sistema: controle de interface (menu/loop), captura e saneamento de inputs, processamento matemático e formatação de exibição.

### A) Código Violado (Estrutura Monolítica Original)

Abaixo está a estrutura original onde uma única classe gerenciava múltiplos contextos de mudança:

```python
# Versão Original - Violando o SRP
import math

class Calculator:
    def __init__(self):
        self.operations = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "sqrt", "6": "power"}

    def run(self):
        # Gerencia o loop, chamadas e capturas de exceção
        pass

    def display_menu(self):
        # Exibe o menu no terminal
        pass

    def read_number(self, prompt):
        # Captura, limpa string (vírgula por ponto) e valida tipo
        pass

    def calculate_result(self, operation, first_value, second_value=None):
        # Contém todas as regras matemáticas e tratamento de exceções de domínio
        pass

    def format_result(self, value):
        # Formata a exibição numérica de saída
        pass