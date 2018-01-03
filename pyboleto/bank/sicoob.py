# -*- coding: utf-8 -*-
from ..data import BoletoData, CustomProperty


class BoletoSicoob(BoletoData):
    """
      Boleto Sicoob
    """
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 8)
    nosso_numero = CustomProperty('nosso_numero', 7)
    convenio = CustomProperty('convenio', 7)

    def __init__(self):
        BoletoData.__init__(self)
        self.codigo_banco = "756"
        self.logo_image = "logo_sicoob.jpg"
        self.modalidade_cobranca = '01'
        self.numero_parcela = '001'

    @property
    def agencia_conta_cedente(self):
        return "%s/%s" % (self.agencia_cedente, self.convenio)

    @property
    def dv_nosso_numero(self):
        _c = '319731973197319731973'
        _d = '%4s%10s%7s' %(self.agencia_cedente,
                            self.convenio.zfill(10),
                            self.nosso_numero)
        t = 0
        for i in range(len(_c)):
            t+= int(_d[i]) * int(_c[i])

        r = t % 11 
        if r in [0,1]:
            return 0
        else:
            return 11-r

    def format_nosso_numero(self):
        return "%s-%s" % (self.nosso_numero,self.dv_nosso_numero)

    @property
    def campo_livre(self):
        content = "%1s%4s%2s%7s%8s%3s"  % (self.carteira,
                                           self.agencia_cedente,
                                           self.modalidade_cobranca,
                                           self.convenio,
                                           '%7s%1s' %(self.nosso_numero,
                                                      self.dv_nosso_numero),
                                           self.numero_parcela)
        return str(content)
