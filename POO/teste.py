from conta import *

conta = Conta(123, "Henrique", 55.0)
conta2 = Conta(321, "José", 100.0)
conta.deposito(55.0)
conta.extrato()
conta.sacar(10000.0)
conta.sacar(60.0)
conta.extrato()

conta.transferir(300.0, conta2)
conta.transferir(2.0, conta2)
conta.extrato()
conta2.extrato()

#conta.limite = 2000.0
#print(conta.numero)

print(Conta.codigo_banco())
