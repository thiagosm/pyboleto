# -*- coding: utf-8 -*-
from ..data import BoletoData, CustomProperty


class BoletoAilos(BoletoData):

    nosso_numero = CustomProperty('nosso_numero', 10)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 10)
    carteira = CustomProperty('carteira', 2)

    def __init__(self):
        super(BoletoAilos, self).__init__()

        self.codigo_banco = "085"
        self.logo_image = "logo_ailos.jpg"
        self.carteira = '01'


    def format_nosso_numero(self):        
        return "%s%s%s" % (
            str(self.conta_cedente)[-8:].zfill(8),
            str(self.nosso_numero)[-8:].zfill(8),
            str(self.dv_nosso_numero)[0]
        )

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
            self.conta_cedente[0:-1].zfill(9),self.conta_cedente[-1:])

    @property
    def campo_livre(self):
        content = "%4s%11s" % (self.agencia_cedente.zfill(4),
                               self.format_nosso_numero().replace('-',''))
        return str(content)

