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
        dataN = input('    Data de nascimento: ')
        senhaN = int(input('    Crie sua senha: '))
        numeroC = input('    Numero da conta: ')

        print('    Digite abaixo seu endereco completo:\n')

        cidade = input('    >>> Cidade: ')
        bairro = input('    >>> Bairro: ')
        rua = input('    >>> Rua: ')
        numero = int(input('    >>> Numero: '))
        cep = int(input('    >>> CEP: '))

        if cpfN in (conta['CPF'] for conta in self.CONTAS_E_USUARIOS.values()) or senhaN in (conta['Senha'] for conta in self.CONTAS_E_USUARIOS.values()) or numeroC in (conta['Numero da conta'] for conta in self.CONTAS_E_USUARIOS.values()):
            print('\n    [ERRO] Usuário ou dados já cadastrados.')  
        else:
            self.CONTAS_E_USUARIOS[userN] = {'CPF': cpfN, 
                                             'Data de Nascimento': dataN, 
                                             'Senha': senhaN, 
                                             'Dados': {
                                                        'Agencia': '0001', 
                                                        'Numero da conta': numeroC, 
                                                        'Saldo': 0, 
                                                        'Extrato': [], 
                                                        'Numero de saques': 0}, 
                                                            'Endereco': {   
                                                                'Cidade': cidade, 
                                                                'Bairro': bairro, 
                                                                'Numero': numero, 
                                                                'Rua': rua, 
                                                                'CEP': cep}}

    def deposito(self, user):

        x = float(input("    Digite um valor para deposito: R$ "))

        self.CONTAS_E_USUARIOS[user]['Dados']['Saldo'] += x
        self.CONTAS_E_USUARIOS[user]['Dados']['Extrato'].append(x)

        print("\n    ######## VOLTANDO AO INICIO ########\n")

    def saque(self, user):  

        x = float(input("    Digite um valor para saque: R$ "))

        if x > self.CONTAS_E_USUARIOS[user]['Dados']['Saldo'] or self.CONTAS_E_USUARIOS[user]['Dados']['Numero de saques'] >= self.LIMITE_SAQUES or x >= self.LIMITE:
            print("    [ERRO] LIMITE DE SAQUES EXCEDIDO OU VALOR MAIOR QUE O ESPERADO.")
        else:
            self.CONTAS_E_USUARIOS[user]['Dados']['Saldo'] -= x
            self.CONTAS_E_USUARIOS[user]['Dados']['Numero de saques'] += 1
            self.CONTAS_E_USUARIOS[user]['Dados']['Extrato'].append(-x)

        print("\n    ######## VOLTANDO AO INICIO ########\n")

    def mostraExtrato(self, user):

        print(f"""\n    ######## SUA CONTA ########\n
    SALDO: {self.CONTAS_E_USUARIOS[user]['Dados']['Saldo']}
    EXTRATO: {self.CONTAS_E_USUARIOS[user]['Dados']['Extrato']}
    SAQUES: {self.CONTAS_E_USUARIOS[user]['Dados']['Numero de saques']}
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
        
        boolW = True
        while boolW == True:
            if menu == "a":
                boolW = False
                Cliente.deposito(self, user)
            elif menu == "b":
                boolW = False
                Cliente.saque(self, user)
            elif menu == "c":
                boolW = False
                Cliente.mostraExtrato(self, user)
            elif menu == "d":
                boolW = False
                Cliente.criarConta(self)
            elif menu == "e":
                boolW = False
                Cliente.listaUsers(self)
            elif menu == 'f':
                boolW = False
                print('\n    ##### FINALIZANDO O PROGRAMA #####')
            else:
                print("    ##### [ERRO] OPERACAO INVALIDA #####")

    def perguntaUsuario(self):
        
        boolW = True
        while boolW == True:

            x = str(input('\n    Ja tem conta? [S/N] --> ')).lower()

            if x == 's': 

                print("\n    ######## INICIO ########\n")

                user = str(input('    Digite seu nome: '))
                cpf = int(input('    Digite seu CPF: '))
                numeroC = input('    Digite o numero da conta: ')
                senha = int(input('    Digite sua senha: '))

                if user in self.CONTAS_E_USUARIOS and self.CONTAS_E_USUARIOS[user]['CPF'] == cpf and self.CONTAS_E_USUARIOS[user]['Senha'] == senha and self.CONTAS_E_USUARIOS[user]['Dados']['Numero da conta'] == numeroC:
                    boolW = False
                    Cliente.perguntaMenu(self, user)
                else:
                    print('\n    [ERRO] Dados nao encontrados.\n')
            elif x == 'n':
                boolW = False
                Cliente.criarConta(self)
            else:
                print("    ##### [ERRO] OPERACAO INVALIDA #####")