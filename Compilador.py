def analisador_lexico(linha_texto):
    ESTADO_INICIAL = 0
    ESTADO_NUMERO_INTEIRO = 1
    ESTADO_NUMERO_DECIMAL = 2
    ESTADO_LETRA = 3 
    
    estado_atual = ESTADO_INICIAL
    lexema_atual = ""
    tokens = []
    
    entrada = linha_texto + " "

    for caracter in entrada:
        
        if estado_atual == ESTADO_INICIAL:
            if caracter.isspace():
                continue 
            
            elif caracter.isdigit():
                estado_atual = ESTADO_NUMERO_INTEIRO
                lexema_atual += caracter
                
            elif caracter.isalpha():
                estado_atual = ESTADO_LETRA
                lexema_atual += caracter
                
            elif caracter in "+-*/%^()":
                tokens.append(("OPERADOR", caracter))
                
            else:
                pass 

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
                
                if caracter in "+-*/%^()":
                    tokens.append(("OPERADOR", caracter))

        elif estado_atual == ESTADO_NUMERO_DECIMAL:
            if caracter.isdigit():
                lexema_atual += caracter
            else:
                tokens.append(("NUMERO", float(lexema_atual)))
                lexema_atual = ""
                estado_atual = ESTADO_INICIAL
                
                if caracter in "+-*/%^()":
                    tokens.append(("OPERADOR", caracter))
                    
        elif estado_atual == ESTADO_LETRA:
            if caracter.isalpha():
                lexema_atual += caracter
            else:
                tokens.append(("COMANDO", lexema_atual))
                lexema_atual = ""
                estado_atual = ESTADO_INICIAL
                
                if caracter in "+-*/%^()":
                    tokens.append(("OPERADOR", caracter))

    return tokens
