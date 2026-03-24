def analisador_lexico(linha_texto):
    ESTADO_INICIAL = 0
    ESTADO_NUMERO_INTEIRO = 1
    ESTADO_NUMERO_DECIMAL = 2
    ESTADO_LETRA = 3 
    ESTADO_DIVISAO = 4
    
    estado_atual = ESTADO_INICIAL
    lexema_atual = ""
    tokens = []
    
    entrada = linha_texto + " "

    i = 0
    while i < len(entrada):
        caracter = entrada[1]
        
        if estado_atual == ESTADO_INICIAL:
            if caracter.isspace():
                i += 1
                continue 
            
            elif caracter.isdigit():
                estado_atual = ESTADO_NUMERO_INTEIRO
                lexema_atual += caracter
                
            elif caracter.isalpha():
                estado_atual = ESTADO_LETRA
                lexema_atual += caracter

            elif caracter == '/':
                estado_atual = ESTADO_DIVISAO
                
            elif caracter in "+-*/%^()":
                tokens.append(("OPERADOR", caracter))
                
            else:
                pass 

        elif estado_atual == ESTADO_DIVISAO:
            if caracter == '/':
                tokens.append(("OPERADOR", "//"))
            else:
                tokens.append(("OPERADOR", "/"))
                i -= 1
            estado_atual = ESTADO_INICIAL

        elif estado_atual == ESTADO_NUMERO_INTEIRO:
            if caracter.isdigit():
                lexema_atual += caracter
                
            elif caracter == '.':
                estado_atual = ESTADO_NUMERO_DECIMAL
                lexema_atual += caracter
                
            else:
                tokens.append(("NUMERO", float(lexema_atual)))
                lexema_atual = ""
                estado_atual = ESTADO_INICIAL 
                i -= 1

        elif estado_atual == ESTADO_NUMERO_DECIMAL:
            if caracter.isdigit():
                lexema_atual += caracter
            else:
                tokens.append(("NUMERO", float(lexema_atual)))
                lexema_atual = ""
                estado_atual = ESTADO_INICIAL
                i -= 1
                    
        elif estado_atual == ESTADO_LETRA:
            if caracter.isalpha():
                lexema_atual += caracter
            else:
                tokens.append(("COMANDO", lexema_atual))
                lexema_atual = ""
                estado_atual = ESTADO_INICIAL
                i -= 1
                
        i += 1

    return tokens

def gerar_assembly(lista_tokens, nome_arquivo_saida):

    global contador_ciclos

    memoria_numeros = []

    with open(nome_arquivo_saida, 'w') as f:
        f.write(".global_start\n")
        f.write(".text\n")
        f.write("_start:\n\n")

        for tipo, valor in lista_tokens:
            if tipo == "NUMERO":
                id_num = len(memoria_numeros) + 1
                memoria_numeros.append((id_num, valor))

                f.write(f" - Numero: {valor} - \n")
                f.write(f" ldr r0, =num_{id_num} \n")
                f.write(f" vldr d0, [r0] \n")
                f.write(" vpush {d0} \n\n")
            
            elif tipo == "OPERADOR" and valor not in ['(', ')']:
                f.write(f" - Operador: {valor} - \n")
                f.write(" vpop {d0} \n")
                f.write(" vpop {d1} \n")

            if valor == '+':
                f.write(" vadd.f64 d2, d1, d0 \n")
            elif valor == '-':
                f.write(" vadd.f64 d2, d1, d0 \n")
            elif valor == '*':
                f.write(" vadd.f64 d2, d1, d0 \n")
            elif valor == '/':
                f.write(" vadd.f64 d2, d1, d0 \n")
                
                
