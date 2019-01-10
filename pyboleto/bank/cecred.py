# -*- coding: utf-8 -*-
from ..data import BoletoData, CustomProperty


class BoletoCecred(BoletoData):
    """
      Boleto Cecred
    """
    agencia_cedente = CustomProperty('agencia_cedente', 6)
    conta_cedente = CustomProperty('conta_cedente', 8)
    nosso_numero = CustomProperty('nosso_numero', 7)

    def __init__(self):
        BoletoData.__init__(self)
        self.codigo_banco = "085"
        self.logo_image = "logo_cecred.jpg"


    @property
    def agencia_conta_cedente(self):
        return "%s/%s" % (self.agencia_cedente, self.conta_cedente)

    def format_nosso_numero(self):
        return "%s%s" % (str(self.conta_cedente).zfill(8),str(self.numero_documento).zfill(9))

    @property
    def campo_livre(self):
        content = "%6s%8s%9s%2s"  % (str(self.convenio).zfill(6),
                                     str(self.conta_cedente).zfill(8),
                                     str(self.numero_documento).zfill(9),
                                     self.carteira)
        return str(content)
