import textwrap

#001 mostrar menu
def menu():
    menuOpcoes = """\n
    ================ MENU ================
    [nu]\tNovo usuário
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    
    [q]\tSair
    => """
    return input(textwrap.dedent(menuOpcoes))

#003 classe novo usuario/cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        # TODO: validar o número de transações e invalidar a operação se for necessário
        # print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


#004 metodo criar novo cliente/usuario
#@log_transacao
def novo_usuario(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

#005
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

#006 para criar novo usuario/cliente precisa dessa classe
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf



#002função principal executa o menu
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            novo_usuario(clientes)

        # elif opcao == "d":
        #     depositar(clientes)

        # elif opcao == "s":
        #     sacar(clientes)

        # elif opcao == "e":
        #     exibir_extrato(clientes)



        # elif opcao == "nc":
        #     numero_conta = len(contas) + 1
        #     criar_conta(numero_conta, clientes, contas)

        # elif opcao == "lc":
        #     listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()