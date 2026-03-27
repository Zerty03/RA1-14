## Integrantes
* **Eugênio Polistchuk Berendsen** - [@Zerty03](https://github.com/Zerty03)
* **Grupo:** RA1-14

## Como o Código Funciona (Resumo Técnico)

O compilador foi dividido em duas fases principais:

1. **Analisador Léxico (Autômato Finito Determinístico):**
   O código não utiliza Expressões Regulares (Regex). Em vez disso, implementa um autômato manual na função `analisador_lexico`. O algoritmo lê a string de entrada caractere por caractere, transitando entre estados (como `ESTADO_NUMERO_INTEIRO`, `ESTADO_NUMERO_DECIMAL`, `ESTADO_DIVISAO`) para classificar e agrupar os tokens corretamente, além de bloquear caracteres inválidos na hora.

2. **Gerador de Código Assembly (FPU ARMv7):**
   A tradução utiliza a arquitetura baseada em Pilha (Stack). Como as expressões estão em Notação Polonesa Reversa (RPN), a lógica é direta:
   * **Números:** São declarados dinamicamente na memória RAM (seção `.data`), carregados para o processador e empurrados para a pilha da FPU (`vpush {d0}`).
   * **Operadores:** O programa desempilha os dois últimos valores (`vpop {d0}` e `vpop {d1}`), realiza a operação matemática (usando instruções de 64 bits como `vadd.f64`, `vmul.f64`) e empilha o resultado final de volta (`vpush {d2}`).
   * **Potenciação (`^`):** Como o ARMv7 não possui uma instrução nativa de potência em ponto flutuante, o Python injeta dinamicamente um laço de repetição (`loop`) no código Assembly, gerando rótulos únicos (ex: `ciclo_potencia_1`) para realizar as multiplicações sucessivas.

## Estrutura de Arquivos
* `Compilador.py`: Código-fonte principal com o analisador léxico
* `Teste_Comp.py`: Script com testes unitário (validação) e testes de integração
* `teste1.txt`, `teste2.txt`, `teste3.txt`: Arquivos com as expressões matemáticas de entrada
* `saida_assembly.s`: Arquivo gerado pelo compilador com as instruções ARMv7
* `tokens_gerados.txt`: Arquivo gerado contendo a lista dos tokens classificados


## Como executar o compilador
O programa roda via linha de comando no terminal. Para compilar os arquivos de texto contendo as expressões, utilize os comandos abaixo:

**Para rodar o Arquivo de Teste 1:**
`python Compilador.py teste1.txt`

**Para rodar o Arquivo de Teste 2:**
`python Compilador.py teste2.txt`

**Para rodar o Arquivo de Teste 3:**
`python Compilador.py teste3.txt`

## Como Executar os Testes Automáticos
O projeto inclui uma suíte de testes unitários e de integração para validar o autômato finito determinístico e a geração correta do código. 

Para rodar, abra o terminal nesta pasta e digite:
`python Teste_Comp.py`