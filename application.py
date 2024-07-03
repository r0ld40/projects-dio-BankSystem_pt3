from sys_banc import Cliente

app = Cliente()
bool = True
while bool == True:
    app.perguntaUsuario()
    p = input('\n    Continuar? [S/N] -> ').lower()

    bool = True if p == 's' else False