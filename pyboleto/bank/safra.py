# -*- coding: utf-8 -*-
from ..data import BoletoData, CustomProperty


class BoletoSafra(BoletoData):
    """
      Boleto Safra
    """
    agencia_cedente = CustomProperty('agencia_cedente', 5)
    conta_cedente = CustomProperty('conta_cedente', 8)
    conta_cedente_dv = CustomProperty('conta_cedente_dv',1)
    nosso_numero = CustomProperty('nosso_numero', 8)
    

    def __init__(self):
        BoletoData.__init__(self)
        self.codigo_banco = "422"
        self.logo_image = "logo_safra.jpg"
        self.modalidade_cobranca = '2'

    @property
    def agencia_conta_cedente(self):
        return "%s/%s-%s" % (self.agencia_cedente, self.conta_cedente,self.conta_cedente_dv)

    @property
    def dv_nosso_numero(self):
        _c = '98765432'
        _d = '%8s' %(self.nosso_numero.zfill(8))
        t = 0
        for i in range(len(_c)):
            t+= int(_d[i]) * int(_c[i])

        r = t % 11 
        if r == 0:
            return 1
        elif r == 1:
            return 0 
        else:
            return 11-r

    def format_nosso_numero(self):
        return "%s-%s" % (self.nosso_numero,self.dv_nosso_numero)

    @property
    def campo_livre(self):
        content = "%1s%5s%8s%1s%8s%1s%1s"  % ('7',
                                           self.agencia_cedente,
                                           self.conta_cedente,
                                           self.conta_cedente_dv,
                                           self.nosso_numero,
                                           self.dv_nosso_numero,
                                           self.modalidade_cobranca)
        return str(content)



