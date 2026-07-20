# Diagramas de Sequência - Calculadora no Terminal

Este documento apresenta a modelagem comportamental do sistema através de Diagramas de Sequência UML. Cada fluxo abaixo detalha cronologicamente a troca de mensagens, chamadas de métodos e retornos entre o Usuário, a Controladora (`Calculator`), o Saneador de Entradas (`InputHandler`) e o Motor Matemático (`Operations`).

---

## US01 - Soma de Dois Números

### O que é:
Esta sequência ilustra o fluxo de adição de dois valores numéricos. O sistema solicita sequencialmente as entradas ao usuário, o `InputHandler` limpa possíveis formatações regionais (convertendo vírgulas em pontos), a classe `Operations` executa o cálculo aritmético e o resultado final é formatado de forma limpa antes da exibição.

![Diagrama de Sequência US01](diagramas_sequencia/diagrama_sequencia_us01.png)

---

## US02 - Subtração de Dois Números

### O que é:
Modela o fluxo para encontrar a diferença matemática entre dois números. Segue a estrutura padrão de captura dupla de dados, invocando o método de cálculo específico para subtração e retornando o controle visual de forma segura para o loop principal da interface.

![Diagrama de Sequência US02](diagramas_sequencia/diagrama_sequencia_us02.png)

---

## US03 - Multiplicação de Dois Números

### O que é:
Este diagrama descreve a operação de produto de dois fatores. Destaca-se o papel do método format_result, que avalia se o float retornado pela multiplicação possui casas decimais significativas, limpando zeros redundantes à direita (ex: transformando 10.0 em uma string estrita "10").

![Diagrama de Sequência US03](diagramas_sequencia/diagrama_sequencia_us03.png)

---

## US04 - Divisão de Dois Números

### O que é:
Modela a operação de divisão fracionária. Este fluxo introduziu um bloco condicional (alt/else) para representar o mecanismo de proteção contra instabilidades matemáticas: se o divisor capturado for 0, a classe de operações interrompe o fluxo lançando uma exceção de sistema que é devidamente mitigada pelo bloco defensivo da controladora.

![Diagrama de Sequência US04](diagramas_sequencia/diagrama_sequencia_us04.png)

---

## US05 - Raiz Quadrada

### O que é:
Demonstra a execução de uma operação unária (que requer apenas um parâmetro numérico). A lógica implementa uma validação de domínio para números reais: caso o usuário tente extrair a raiz de um número negativo, o motor impede o cálculo do math.sqrt tradicional e desvia o comportamento para uma mensagem explicativa de erro.

![Diagrama de Sequência US05](diagramas_sequencia/diagrama_sequencia_us05.png)

---

## US06 - Potenciação

### O que é:
Mapeia a interação para cálculos exponenciais. O fluxo gerencia a captura sequencial de duas variáveis com semânticas distintas (a base e, em seguida, o expoente), repassando as duas para o motor aritmético processar a exponenciação nativa do Python (**).

![Diagrama de Sequência US06](diagramas_sequencia/diagrama_sequencia_us06.png)

---

## US07 - Encerrar a Calculadora

### O que é:
Descreve o encerramento seguro e controlado do ciclo de vida da aplicação. Ao receber comandos explícitos de saída (como "0" ou "sair"), a controladora abandona o laço de repetição contínuo sem depender de erros catastróficos ou quebras abruptas de console.

![Diagrama de Sequência US07](diagramas_sequencia/diagrama_sequencia_us07.png)
