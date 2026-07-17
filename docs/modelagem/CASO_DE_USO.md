# Diagrama de Casos de Uso - Calculadora no Terminal

Este documento apresenta o mapeamento funcional do sistema a partir do ponto de vista do utilizador.

---

## Mapeamento Visual

![Diagrama de Casos de Uso](caso_de_uso.png)

---

## Descrição dos Elementos do Diagrama

Para garantir a robustez e a correta aplicação da semântica UML, os elementos dentro da **Fronteira do Sistema** foram mapeados da seguinte forma:

* **Ator Principal:** 
  * **Usuário:** Interage com a interface de linha de comando para selecionar opções e inserir dados.

* **Casos de Uso Principais (Fluxos de Sucesso):**
  * Realizar Soma, Realizar Subtração, Realizar Multiplicação, Realizar Divisão, Calcular Raiz Quadrada, Calcular Potência e Sair do Sistema.

* **Relacionamento `<<include>>` (Inclusão Obrigatória):**
  * **Validar Entrada Numérica:** Todos os casos de uso de cálculo acionam obrigatoriamente este caso de uso para garantir que o programa saneie e valide os dados antes de processar a matemática.

* **Relacionamento `<<extend>>` (Fluxos de Exceção/Erro):**
  * **Exibir Erro: Divisão por Zero:** Estende o caso de uso *Realizar Divisão* quando o usuário tenta dividir um número por zero.
  * **Exibir Erro: Raiz Negativa:** Estende o caso de uso *Calcular Raiz Quadrada* quando o usuário fornece um valor menor que zero.