import unittest
import os
from Compilador import analisador_lexico, gerar_assembly

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

    pass

class TestIntegracaoCompilador(unittest.TestCase):
    
    def setUp(self):
        """Prepara o ambiente antes do teste rodar (Cria um arquivo de teste temporário)."""
        self.arquivo_entrada = "temp_teste_integracao.txt"
        self.arquivo_saida = "temp_saida_assembly.s"
        
        with open(self.arquivo_entrada, "w") as f:
            f.write("( 5.0 3.0 + )\n")
            f.write("( 10.0 2.0 / )\n")

    def tearDown(self):
        """Limpa a casa depois que o teste termina (Apaga os arquivos temporários)."""
        if os.path.exists(self.arquivo_entrada):
            os.remove(self.arquivo_entrada)
        if os.path.exists(self.arquivo_saida):
            os.remove(self.arquivo_saida)

    def test_geracao_assembly_completa(self):
        """Testa se o compilador lê o arquivo e gera o código Assembly corretamente."""
        
        todos_tokens = []
        with open(self.arquivo_entrada, 'r') as arquivo:
            for linha in arquivo:
                todos_tokens.extend(analisador_lexico(linha))
                
        gerar_assembly(todos_tokens, self.arquivo_saida)
        
        self.assertTrue(os.path.exists(self.arquivo_saida), "O arquivo Assembly não foi criado!")
        
        with open(self.arquivo_saida, 'r') as f:
            conteudo_assembly = f.read()
            
        self.assertIn(".global _start", conteudo_assembly)
        
        self.assertIn("vadd.f64", conteudo_assembly)
        self.assertIn("vdiv.f64", conteudo_assembly)
        
        self.assertIn("variavel_mem: .space 8", conteudo_assembly)
        self.assertIn("num_1: .double 5.0", conteudo_assembly)

if __name__ == '__main__':
    unittest.main(verbosity=2)