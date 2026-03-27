## Integrantes
* **Eugênio Polistchuk Berendsen** - [@Zerty03](https://github.com/Zerty03)
* **Grupo:** RA1-14

## Estrutura de Arquivos
* `Compilador.py`: Código-fonte principal com o analisador léxico
* `Teste_Comp.py`: Script com testes unitário (validação) e testes de integração
* `teste1.txt`, `teste2.txt`, `teste3.txt`: Arquivos com as expressões matemáticas de entrada
* `saida_assembly.s`: Arquivo gerado pelo compilador com as instruções ARMv7
* `tokens_gerados.txt`: Arquivo gerado contendo a lista dos tokens classificados


## Como executar o compilador
O programa roda via linha de comando no terminal. Para compilar os arquivos de texto contendo as expressões, utilize os comandos abaixo:

** Para rodar o Arquivo de Teste 1:**
`python Compilador.py teste1.txt`

**Para rodar o Arquivo de Teste 2:**
`python Compilador.py teste2.txt`

**Para rodar o Arquivo de Teste 3:**
`python Compilador.py teste3.txt`

## Como Executar os Testes Automáticos
O projeto inclui uma suíte de testes unitários e de integração para validar o autômato finito determinístico e a geração correta do código. 

Para rodar, abra o terminal nesta pasta e digite:
`python Teste_Comp.py`