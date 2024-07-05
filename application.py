from sys_banc import Cliente

app = Cliente()

bool = True
while bool == True:
    app.perguntaUsuario()
    p = input('\n    Continuar? [S/N] -> ').lower()

    if p == 's':
        bool = True
    elif p == 'n':
        bool = False
    else:
        print("    ##### [ERRO] OPERACAO INVALIDA #####")