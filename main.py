import math


class Calculator:
    """Calculadora interativa no terminal com operações básicas e tratamento de erros."""

    def __init__(self):
        self.operations = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/",
            "5": "sqrt",
            "6": "power",
        }

    def run(self):
        """Inicia o loop principal da calculadora no terminal."""
        print("=== Calculadora no Terminal ===")
        print("Digite 0 ou sair para encerrar.\n")

        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ").strip().lower()

            if choice in {"0", "sair", "q", "quit", "exit"}:
                print("Encerrando a calculadora.")
                break

            if choice not in self.operations:
                print("Opção inválida. Tente novamente.\n")
                continue

            operation = self.operations[choice]

            try:
                if operation == "sqrt":
                    value = self.read_number("Digite um número: ")
                    result = self.calculate_result(operation, value)
                elif operation == "power":
                    base = self.read_number("Digite a base: ")
                    exponent = self.read_number("Digite o expoente: ")
                    result = self.calculate_result(operation, base, exponent)
                else:
                    first_value = self.read_number("Digite o primeiro número: ")
                    second_value = self.read_number("Digite o segundo número: ")
                    result = self.calculate_result(operation, first_value, second_value)

                print(f"Resultado: {self.format_result(result)}\n")
            except ZeroDivisionError:
                print("Erro: divisão por zero.\n")
            except ValueError as exc:
                print(f"Erro: {exc}\n")

    def display_menu(self):
        """Exibe as opções disponíveis para o usuário."""
        print("Operações:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Raiz quadrada")
        print("6 - Potência")
        print("0 - Sair")

    def read_number(self, prompt):
        """Lê um valor numérico válido do usuário."""
        while True:
            try:
                value = input(prompt).strip().replace(",", ".")
                return float(value)
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

    def calculate_result(self, operation, first_value, second_value=None):
        """Executa a lógica matemática para as operações escolhidas."""
        if operation == "+":
            return first_value + second_value
        if operation == "-":
            return first_value - second_value
        if operation == "*":
            return first_value * second_value
        if operation == "/":
            if second_value == 0:
                raise ZeroDivisionError("Divisão por zero")
            return first_value / second_value
        if operation == "sqrt":
            if first_value < 0:
                raise ValueError("não é possível calcular a raiz de um número negativo")
            return math.sqrt(first_value)
        if operation == "power":
            return first_value ** second_value

        raise ValueError("Operação inválida")

    def format_result(self, value):
        """Formata o resultado para exibição mais limpa no terminal."""
        if isinstance(value, float):
            if value.is_integer():
                return str(int(value))
            return f"{value:.10g}"
        return str(value)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
