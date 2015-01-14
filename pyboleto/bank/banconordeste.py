# -*- coding: utf-8 -*-
from ..data import BoletoData, custom_property


class BoletoBancoNordeste(BoletoData):
    agencia_cedente = custom_property('agencia_cedente', 4)
    conta_cedente = custom_property('conta_cedente', 7)
    conta_cedente_dv = custom_property('conta_cedente_dv',1)
    nosso_numero = custom_property('nosso_numero', 7)
    carteira = custom_property('carteira', 2)

    def __init__(self):
        BoletoData.__init__(self)
        self.codigo_banco = "004"
        self.logo_image = "logo_banconordeste.jpg"

    @property
    def agencia_conta_cedente(self):
        return "%s / %s-%s" % (
            self.agencia_cedente,
            self.conta_cedente,
            self.conta_cedente_dv
        )


    @property
    def dv_nosso_numero(self):
        return self.modulo11(self.nosso_numero)

    def format_nosso_numero(self):
        return "%s-%s" % (self.nosso_numero,self.modulo11(self.nosso_numero))

    @property
    def campo_livre(self):
        content = "%4s%7s%1s%7s%1s%2s%3s" % (self.agencia_cedente.split('-')[0],
                                        self.conta_cedente.split('-')[0],
                                        self.conta_cedente_dv,
                                        self.nosso_numero,
                                        self.dv_nosso_numero,
                                        self.carteira,
                                        '000'
                                        )
        return content
