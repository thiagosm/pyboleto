# -*- coding: utf-8
from ..data import BoletoData, custom_property
from datetime import date

class BoletoSicredi(BoletoData):

    nosso_numero = custom_property('nosso_numero', 5)
    agencia_cedente = custom_property('agencia_cedente', 4)
    conta_cedente = custom_property('conta_cedente', 5)
    posto = custom_property('posto',2)

    def __init__(self,posto,byte_idt='2',tipo_cobranca='3',tipo_carteira='1'):
        super(BoletoSicredi, self).__init__()

        self.codigo_banco = "748"
        self.logo_image = "logo_sicredi.jpg"
        self.carteira = 'A'
        # Byte de Identificação do cedente 1 - Cooperativa; 2 a 9 - Cedente
        self.byte_idt = byte_idt

        if not self.inicio_nosso_numero:
            self.inicio_nosso_numero = date.today().strftime('%y')

        self.tipo_cobranca = tipo_cobranca  # SICREDI ( 1 = com registro )
        self.tipo_carteira = tipo_carteira  # Carteira simples
        self.posto = posto

    def format_nosso_numero(self):
        return '%2s/%1s%5s-%1s' %(self.inicio_nosso_numero,
                                 self.byte_idt,
                                 self.nosso_numero,
                                 self.dv_nosso_numero)


    @property
    def dv_nosso_numero(self):
        _nn = '%s%s%s%s%s%s' %(self.agencia_cedente,
                               self.posto,
                               self.conta_cedente,
                               self.inicio_nosso_numero,
                               self.byte_idt,
                               self.nosso_numero)

        resto2 = self.modulo11(_nn, 9, 1)
        digito = 11 - resto2

        if digito > 9:
            dv = 0
        else:
            dv = digito
        return dv


    @property
    def agencia_conta_cedente(self):
        return "%s.%s.%s" % (
            self.agencia_cedente,
            self.posto,
            self.conta_cedente)

    def _dv_num(self, num):
        resto2 = self.modulo11(num, 9, 1)
        if resto2 <=1:
            dv = 0
        else:
            dv = 11 - resto2
        return dv 

    @property
    def campo_livre(self):
        content = "%1s%1s%2s%1s%5s%1s%4s%2s%5s10" % (self.tipo_cobranca,
                                                   self.tipo_carteira,
                                                   self.inicio_nosso_numero,
                                                   self.byte_idt,
                                                   self.nosso_numero,
                                                   self.dv_nosso_numero,
                                                   self.agencia_cedente,
                                                   self.posto,
                                                   self.conta_cedente)
        return str("%s%s" %(content,self._dv_num(content)))

