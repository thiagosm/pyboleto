# -*- coding: utf-8
from ..data import BoletoData, CustomProperty
from datetime import date

class BoletoUnicred(BoletoData):

    nosso_numero = CustomProperty('nosso_numero', 10)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 10)
    carteira = CustomProperty('carteira',2)

    def __init__(self):
        super(BoletoUnicred, self).__init__()

        self.codigo_banco = "136"
        self.logo_image = "logo_unicred.jpg"
        self.carteira = '51'


    def format_nosso_numero(self):
        return '%10s-%1s' %(self.nosso_numero.zfill(10),self.dv_nosso_numero)


    @property
    def dv_nosso_numero(self):
        _nn = self.nosso_numero.zfill(10)
        resto2 = self.modulo11(_nn, 7, 1)
        digito = 11 - resto2

        if digito > 9:
            dv = 0
        else:
            dv = digito
        return dv


    @property
    def agencia_conta_cedente(self):
        return "%s / %s-%s" % (
            self.agencia_cedente.zfill(4),
            self.conta_cedente.zfill(9),self.conta_cedente[-1:])

    @property
    def campo_livre(self):
        content = "%4s%10s%11s" % (self.agencia_cedente.zfill(4),
                                   self.conta_cedente.zfill(10),
                                   self.format_nosso_numero().replace('-',''))
        return str(content)




