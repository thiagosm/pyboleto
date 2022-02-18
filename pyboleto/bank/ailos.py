# -*- coding: utf-8 -*-
from ..data import BoletoData, CustomProperty


class BoletoAilos(BoletoData):

    nosso_numero = CustomProperty('nosso_numero', 9)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 8)
    carteira = CustomProperty('carteira', 2)

    def __init__(self):
        super(BoletoAilos, self).__init__()

        self.codigo_banco = "085"
        self.logo_image = "logo_ailos.jpg"
        self.carteira = '01'

    @property
    def agencia_conta_cedente(self):
        return "%s / %s-%s" % (
            self.agencia_cedente.zfill(4),
            self.conta_cedente[0:-1].zfill(9),self.conta_cedente[-1:])

    def format_nosso_numero(self):
        return "%s%s" % (str(self.conta_cedente).zfill(8), 
                         str(self.numero_documento).zfill(9))

    @property
    def campo_livre(self):
        content = "%6s%8s%9s"  % (str(self.convenio).zfill(6),
                                  str(self.conta_cedente).zfill(8),
                                  str(self.numero_documento).zfill(9))
        return str(content)

