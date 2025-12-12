class Pagamento:
    def __init__(self,numero_cartao="1234 5678 9012 3456",nome="João Silva",validade="12/25",ccv="123",email="joao.silva@gmail.com",banco="Banco Central",agencia="1234",conta="12345678"):
        
        self.numero_cartao=numero_cartao
        self.nome = nome
        self.validade = validade
        self.ccv = ccv
        
        self.email = email
        
        self.banco = banco
        self.agencia = agencia
        self.conta = conta


    def processar_pagamento(self):
        pass
    

class CartaoCredito(Pagamento):
    valor=0
    def processar_pagamento(self):
        print(self.numero_cartao,self.nome,self.validade)


class PayPal(Pagamento):
    valor=0
    def processar_pagamento(self):
        print(self.email)


class TransferenciaBancaria(Pagamento):
    valor=0
    def processar_pagamento(self):
        self.valor=150
        pass


def realizar_pagamento(pagamento: Pagamento):
        pagamento.processar_pagamento()
        pass

