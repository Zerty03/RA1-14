import unittest
from Compilador import analisador_lexico

class TestAnalisadorLexico(unittest.TestCase):

    def test_reconhecimento_numeros(self):
        """Testa se o autômato reconhece inteiros e decimais corretamente."""
        self.assertEqual(analisador_lexico("42"), [("NUMERO", 42.0)])
        self.assertEqual(analisador_lexico("3.1415"), [("NUMERO", 3.1415)])

    def test_reconhecimento_operadores(self):
        """Testa se todos os operadores matemáticos são classificados corretamente."""
        linha = "+ - * / // % ^ ( )"
        esperado = [
            ("OPERADOR", "+"), ("OPERADOR", "-"), ("OPERADOR", "*"),
            ("OPERADOR", "/"), ("OPERADOR", "//"), ("OPERADOR", "%"),
            ("OPERADOR", "^"), ("OPERADOR", "("), ("OPERADOR", ")")
        ]
        self.assertEqual(analisador_lexico(linha), esperado)

    def test_reconhecimento_comandos(self):
        """Testa se os comandos de memória são reconhecidos."""
        self.assertEqual(analisador_lexico("MEM RES"), [
            ("COMANDO", "MEM"),
            ("COMANDO", "RES")
        ])

    def test_expressao_rpn_completa(self):
        """Testa a separação de uma expressão matemática real."""
        linha = "( 15.5 4.5 + )"
        esperado = [
            ("OPERADOR", "("),
            ("NUMERO", 15.5),
            ("NUMERO", 4.5),
            ("OPERADOR", "+"),
            ("OPERADOR", ")")
        ]
        self.assertEqual(analisador_lexico(linha), esperado)

    def test_tratamento_de_erros(self):
        """Testa se o autômato bloqueia caracteres inválidos levantando um ValueError."""
        with self.assertRaises(ValueError):
            analisador_lexico("( 10.0 @ 3.0 + )")
            
        with self.assertRaises(ValueError):
            analisador_lexico("5.0 2.0 $")
    
    def test_espacos_e_linhas_vazias(self):
        """Testa se o autômato ignora múltiplos espaços e lida com linhas vazias."""
        # Vários espaços entre os tokens
        self.assertEqual(analisador_lexico("(    5.0   2.0   +   )"), [
            ("OPERADOR", "("),
            ("NUMERO", 5.0),
            ("NUMERO", 2.0),
            ("OPERADOR", "+"),
            ("OPERADOR", ")")
        ])
        # Linha totalmente vazia
        self.assertEqual(analisador_lexico("   "), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)