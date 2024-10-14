class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"


class Conta:
    def __init__(self, cliente, numero_conta):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saque inválido: saldo insuficiente ou valor inválido.")

    def extrato(self):
        print(f"Extrato da Conta {self.numero_conta}: R${self.saldo:.2f}")

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso.")
        else:
            print("Transferência inválida: saldo insuficiente ou valor inválido.")


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, cliente):
        numero_conta = len(self.contas) + 1
        conta = Conta(cliente, numero_conta)
        self.contas[numero_conta] = conta
        print(f"Conta criada com sucesso: {conta.numero_conta}")
        return conta

    def buscar_conta(self, numero_conta):
        return self.contas.get(numero_conta, None)


# Exemplo de uso
if __name__ == "__main__":
    banco = Banco()

    # Criando clientes
    cliente1 = Cliente("Marçal", "123.456.789-00")
    cliente2 = Cliente("Ana", "987.654.321-00")

    # Criando contas
    conta1 = banco.criar_conta(cliente1)
    conta2 = banco.criar_conta(cliente2)

    # Operações
    conta1.depositar(1000)
    conta1.sacar(200)
    conta1.extrato()

    conta1.transferir(300, conta2)
    conta2.extrato()
