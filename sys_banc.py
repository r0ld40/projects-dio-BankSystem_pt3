class Cliente:
    LIMITE_SAQUES = 3
    LIMITE = 500
        
    def __init__(self):
        self.CONTAS_E_USUARIOS = {}
                                                                
    def listaUsers(self):
        for keys, values in self.CONTAS_E_USUARIOS.items():
            print(keys,values)

    def criarConta(self):

        print("\n    ######## CRIAR CONTA ########\n")

        userN = input('    Digite seu nome: ')
        cpfN = int(input('    Digite seu CPF: '))
        senhaN = int(input('    Crie sua senha: '))

        print('    Digite abaixo seu endereco completo:\n')

        cidade = input('    >>> Cidade: ')
        bairro = input('    >>> Bairro: ')
        rua = input('    >>> Rua: ')
        numero = int(input('    >>> Numero: '))
        cep = int(input('    >>> CEP: '))

        if cpfN in (conta['CPF'] for conta in self.CONTAS_E_USUARIOS.values()) or senhaN in (conta['senha'] for conta in self.CONTAS_E_USUARIOS.values()):
            print('\n    [ERRO] Usuário ou dados já cadastrados.')  
        else:
            self.CONTAS_E_USUARIOS[userN] = {'CPF': cpfN, 'senha': senhaN, 'dados': {'saldo': 0, 'extrato': [], 'num_saques': 0}, 'endereco': {'cidade': cidade, 'bairro': bairro, 'numero': numero, 'rua': rua, 'CEP': cep}}

    def deposito(self, user):

        x = float(input("    Digite um valor para deposito: R$ "))

        self.CONTAS_E_USUARIOS[user]['dados']['saldo'] += x
        self.CONTAS_E_USUARIOS[user]['dados']['extrato'].append(x)

        print("\n    ######## VOLTANDO AO INICIO ########\n")

    def saque(self, user):

        x = float(input("    Digite um valor para saque: R$ "))

        if x > self.CONTAS_E_USUARIOS[user]['dados']['saldo'] or self.CONTAS_E_USUARIOS[user]['dados']['num_saques'] >= self.LIMITE_SAQUES or x >= self.LIMITE:
            print("    [ERRO] LIMITE DE SAQUES EXCEDIDO OU VALOR MAIOR QUE O ESPERADO.")
        else:
            self.CONTAS_E_USUARIOS[user]['dados']['saldo'] -= x
            self.CONTAS_E_USUARIOS[user]['dados']['num_saques'] += 1
            self.CONTAS_E_USUARIOS[user]['dados']['extrato'].append(-x)

        print("\n    ######## VOLTANDO AO INICIO ########\n")

    def mostraExtrato(self, user):

        print(f"""\n    ######## SUA CONTA ########\n
    SALDO: {self.CONTAS_E_USUARIOS[user]['dados']['saldo']}
    EXTRATO: {self.CONTAS_E_USUARIOS[user]['dados']['extrato']}
    SAQUES: {self.CONTAS_E_USUARIOS[user]['dados']['num_saques']}
    LIMITE DE SAQUES: {self.LIMITE_SAQUES}""")

    def perguntaMenu(self, user):

        menu = input("""
    ######## MENU ########
        
    [A] DEPOSITO
    [B] SAQUE
    [C] EXTRATO
    [D] CRIAR NOVA CONTA
    [E] LISTAR CONTAS
    [F] SAIR
                    
    >>> """).lower()
        print()
        
        if menu == "a":
            Cliente.deposito(self, user)
        elif menu == "b":
            Cliente.saque(self, user)
        elif menu == "c":
            Cliente.mostraExtrato(self, user)
        elif menu == "d":
            Cliente.criarConta(self)
        elif menu == "e":
            Cliente.listaUsers(self)
        elif menu == 'f':
            print('\n    ##### FINALIZANDO O PROGRAMA #####')
        else:
            print("    ##### [ERRO] OPERACAO INVALIDA #####")

    def perguntaUsuario(self):
        
        x = str(input('\n    Ja tem conta? [S/N] --> '))

        if x == 'S' or x == 's': 

            print("\n    ######## INICIO ########\n")

            user = str(input('    Digite seu nome: '))
            cpf = int(input('    Digite seu CPF: '))
            senha = int(input('    Digite sua senha: '))

            if user in self.CONTAS_E_USUARIOS and self.CONTAS_E_USUARIOS[user]['CPF'] == cpf and self.CONTAS_E_USUARIOS[user]['senha'] == senha:
                Cliente.perguntaMenu(self, user)
            else:
                print('\n    [ERRO] Dados nao encontrados.\n')
        else:
            Cliente.criarConta(self)