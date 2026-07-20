# Versão Refatorada - Respeitando o SRP
import math

class InputHandler:
    """Responsável estritamente pela captura e validação de dados do usuário."""
    
    def read_number(self, prompt: str) -> float:
        while True:
            try:
                value = input(prompt).strip().replace(",", ".")
                return float(value)
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

class Operations:
    """Responsável estritamente pelas regras de negócio e cálculos matemáticos."""
    
    def calculate_result(self, operation: str, first_value: float, second_value: float = None) -> float:
        if operation == "+": return first_value + second_value
        if operation == "-": return first_value - second_value
        if operation == "*": return first_value * second_value
        if operation == "/":
            if second_value == 0: raise ZeroDivisionError("Divisão por zero")
            return first_value / second_value
        if operation == "sqrt":
            if first_value < 0: raise ValueError("não é possível calcular a raiz de um número negativo")
            return math.sqrt(first_value)
        if operation == "power": return first_value ** second_value
        raise ValueError("Operação inválida")

    def format_result(self, value: float) -> str:
        if isinstance(value, float):
            if value.is_integer(): return str(int(value))
            return f"{value:.10g}"
        return str(value)

class Calculator:
    """Responsável pelo controle de fluxo e interface de usuário no terminal."""
    
    def __init__(self):
        self.operations_map = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "sqrt", "6": "power"}
        self.input_handler = InputHandler()
        self.operations = Operations()

    def display_menu(self):
        print("Operações:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Raiz quadrada")
        print("6 - Potência")
        print("0 - Sair")

    def run(self):
        print("=== Calculadora no Terminal ===")
        print("Digite 0 ou sair para encerrar.\n")
        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ").strip().lower()
            if choice in {"0", "sair", "q", "quit", "exit"}:
                print("Encerrando a calculadora.")
                break
            if choice not in self.operations_map:
                print("Opção inválida. Tente novamente.\n")
                continue
            
            operation = self.operations_map[choice]
            try:
                if operation == "sqrt":
                    val = self.input_handler.read_number("Digite um número: ")
                    res = self.operations.calculate_result(operation, val)
                elif operation == "power":
                    base = self.input_handler.read_number("Digite a base: ")
                    exp = self.input_handler.read_number("Digite o expoente: ")
                    res = self.operations.calculate_result(operation, base, exp)
                else:
                    v1 = self.input_handler.read_number("Digite o primeiro número: ")
                    v2 = self.input_handler.read_number("Digite o segundo número: ")
                    res = self.operations.calculate_result(operation, v1, v2)
                
                print(f"Resultado: {self.operations.format_result(res)}\n")
            except ZeroDivisionError:
                print("Erro: divisão por zero.\n")
            except ValueError as exc:
                print(f"Erro: {exc}\n")

# Bloco para execução do programa
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()