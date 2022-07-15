
from datetime import datetime as dtime


class Funcoes():
    def __init__(self,dbo,cpf):
        self.dbo = dbo
        self.cpf = cpf

    def atualiza_saldo(self,valor):
        saldo=self.dbo.get_data(self.cpf,'saldo')
        saldo+=valor
        self.dbo.upsert_data(self.cpf,saldo,campo='saldo')

    def movimenta_conta(self,valor,tipo):
        try:
            if tipo == 's':
                saldo=self.dbo.get_data(self.cpf,'saldo')
                if valor <= saldo:
                    valor*=-1
                else:
                    print('\n','\n')
                    print('[INFO] Saldo insuficiente!')
                    print('\n','\n')
                    return False

            self.dbo.upsert_data(self.cpf,{tipo:{'date':str(dtime.now()),'valor':valor}},campo='mov')

        except Exception as err:
            print('movimenta_conta',err)
        else:
            self.atualiza_saldo(valor)
            return True

    def cria_conta(self,doc):
        resp = self.dbo.upsert_data(self.cpf,doc)
        return resp

    def extrato_conta(self):
        ext=self.dbo.get_data(self.cpf,'mov')
        if not len(ext):
            print('\n','[INFO] Conta sem movimentação!.','\n')
        else:
            saldo=self.dbo.get_data(self.cpf,'saldo')
            print('\n','\n')
            print('_____________________________________________________________________','\n')
            print('		EXTRATO DE MOVIMENTAÇÃO (Saques/Depositos)')
            print('_____________________________________________________________________','\n','\n')
            print('"D" = Depósito  "S" = Saque','\n','\n')
            print('Saldo da conta: ','R$',float(saldo))
            print('\n','\n')
            print('Data                |Tipo		|Valor em Reais')
            print('__________________________________________________')
            for i in ext:
                for c in i:
                    print('{0}  {1}                   {2}'.format(i[c]['date'][0:19],c.upper(),i[c]['valor']))
            print('\n','\n','\n')
