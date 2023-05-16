# -*- coding: utf-8
from ..data import BoletoData, CustomProperty
from datetime import date

class BoletoBanestes(BoletoData):

    nosso_numero = CustomProperty('nosso_numero', 11)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 7)

    def __init__(self):
        super(BoletoBanestes, self).__init__()

        self.codigo_banco = "021"
        self.logo_image = "logo_bancobanestes.jpg"
        self.carteira = '1'


    def format_nosso_numero(self):
        return "%s-%s" % (
            self.nosso_numero,
            self.dv_nosso_numero
        )

    @property
    def dv_nosso_numero(self):
        campo_livre = '%2s%11s' %(self.carteira, self.nosso_numero)
        
        _c = '2765432765432'
        _t = tuple(campo_livre)
        _z = 0

        for i in range(len(_t)):
            _z += int(_t[i]) * int(_c[i])

        resto = _z % 11
        
        if resto == 0:
            dv = 0
        elif resto == 1:
            dv = "P"
        else:
            dv = 11 - resto

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
