# Histórias de Usuário (User Stories) - Calculadora no Terminal

Este documento detalha os requisitos funcionais do projeto sob a perspectiva do usuário, acompanhados de seus respectivos critérios de aceitação sob o padrão BDD (Behavior-Driven Development).

---

## US01 - Soma de Dois Números
* **Como** usuário da calculadora
* **Eu quero** somar dois valores numéricos
* **Para que eu possa** obter o total acumulado desses valores.

**Critérios de Aceitação:**
* **Dado que** estou no menu principal e escolhi a opção "1 - Soma"
* **Quando** eu inserir o primeiro número "5" e o segundo número "3"
* **Então** o sistema deve exibir o resultado "8" e retornar ao menu de operações.

* **Dado que** escolhi a opção "1 - Soma"
* **Quando** eu inserir um número decimal utilizando vírgula (ex: "5,5") e outro com ponto (ex: "4.5")
* **Então** o sistema deve tratar a entrada corretamente e exibir o resultado "10".

---

## US02 - Subtração de Dois Números
* **Como** usuário da calculadora
* **Eu quero** subtrair um número de outro
* **Para que eu possa** encontrar a diferença matemática entre eles.

**Critérios de Aceitação:**
* **Dado que** estou no menu principal e escolhi a opção "2 - Subtração"
* **Quando** eu inserir o primeiro número "10" e o segundo número "4"
* **Então** o sistema deve exibir o resultado "6" e retornar ao menu de operações.

---

## US03 - Multiplicação de Dois Números
* **Como** usuário da calculadora
* **Eu quero** multiplicar dois valores
* **Para que eu possa** obter o produto do cruzamento entre eles.

**Critérios de Aceitação:**
* **Dado que** estou no menu principal e escolhi a opção "3 - Multiplicação"
* **Quando** eu inserir o primeiro número "4" e o segundo número "2.5"
* **Então** o sistema deve exibir o resultado "10" (formatado de forma limpa, sem o ".0" desnecessário) e retornar ao menu de operações.

---

## US04 - Divisão de Dois Números
* **Como** usuário da calculadora
* **Eu quero** dividir um número por outro
* **Para que eu possa** obter o quociente ou a fração resultante.

**Critérios de Aceitação (Cenário de Sucesso):**
* **Dado que** estou no menu principal e escolhi a opção "4 - Divisão"
* **Quando** eu inserir o primeiro número "15" e o segundo número "3"
* **Então** o sistema deve exibir o resultado "5" e retornar ao menu de operações.

**Critérios de Aceitação (Cenário de Falha):**
* **Dado que** estou no menu de inserção de valores da operação "4 - Divisão"
* **Quando** eu tentar inserir "0" no campo do segundo número (divisor)
* **Então** o sistema deve disparar a mensagem de erro "Erro: divisão por zero." e retornar de forma segura para o menu de operações.

---

## US05 - Raiz Quadrada
* **Como** usuário da calculadora
* **Eu quero** calcular a raiz quadrada de um valor
* **Para que eu possa** saber qual número multiplicado por si mesmo resulta no valor informado.

**Critérios de Aceitação (Cenário de Sucesso):**
* **Dado que** estou no menu principal e escolhi a opção "5 - Raiz quadrada"
* **Quando** eu inserir o número "9"
* **Então** o sistema deve exibir o resultado "3" e retornar ao menu de operações.

**Critérios de Aceitação (Cenário de Falha):**
* **Dado que** escolhi a opção "5 - Raiz quadrada"
* **Quando** eu inserir um número negativo (ex: "-4")
* **Então** o sistema deve exibir a mensagem de erro "Erro: não é possível calcular a raiz de um número negativo" e retornar de forma segura para o menu de operações.

---

## US06 - Potenciação
* **Como** usuário da calculadora
* **Eu quero** elevar uma base a um determinado expoente
* **Para que eu possa** realizar cálculos exponenciais de forma rápida.

**Critérios de Aceitação:**
* **Dado que** estou no menu principal e escolhi a opção "6 - Potência"
* **Quando** eu inserir a base "2" e o expoente "3"
* **Então** o sistema deve exibir o resultado "8" e retornar ao menu de operações.

---

## US07 - Encerrar a Calculadora
* **Como** usuário da calculadora
* **Eu quero** finalizar o programa
* **Para que eu possa** fechar a aplicação de linha de comando com segurança.

**Critérios de Aceitação:**
* **Dado que** estou utilizando o sistema e decido parar
* **Quando** eu digitar "0" ou "sair" no campo de escolhas
* **Então** o sistema deve exibir a mensagem "Encerrando a calculadora." e encerrar a execução do terminal.