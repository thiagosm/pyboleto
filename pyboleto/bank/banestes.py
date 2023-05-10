# -*- coding: utf-8
"""
    pyboleto.bank.banestes
    ~~~~~~~~~~~~~~~~~~~~~~

    Lógica para boletos do banco Banestes.
"""
from ..data import BoletoData, CustomProperty


class BoletoBanestes(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Banestes
    '''

    nosso_numero = CustomProperty('nosso_numero', 11)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 7)

    def __init__(self):
        super(BoletoBanestes, self).__init__()

        self.codigo_banco = "021"
        self.logo_image = "logo_bancobanestes.jpg"
        self.carteira = '06'

    def format_nosso_numero(self):
        return "%s/%s-%s" % (
            self.carteira,
            self.nosso_numero,
            self.dv_nosso_numero
        )

    @property
    def dv_nosso_numero(self):
        resto2 = self.modulo11('%2s%11s' %(self.carteira,self.nosso_numero), 7, 1)
        digito = 11 - resto2
        if digito == 10:
            dv = 'P'
        elif digito == 11:
            dv = 0
        else:
            dv = digito
        return dv

    @property
    def campo_livre(self):
        content = "%4s%2s%11s%7s%1s" % (self.agencia_cedente.split('-')[0],
                                        self.carteira,
                                        self.nosso_numero,
                                        self.conta_cedente.split('-')[0],
                                        '0'
                                        )
        return content