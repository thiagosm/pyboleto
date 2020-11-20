# -*- coding: utf-8
from ..data import BoletoData, CustomProperty


class BoletoInter(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Inter
    '''

    nosso_numero = CustomProperty('nosso_numero', 10)
    agencia_cedente = CustomProperty('agencia_cedente', 5)
    conta_cedente = CustomProperty('conta_cedente', 8)

    def __init__(self):
        super(BoletoInter, self).__init__()

        self.codigo_banco = "077"
        self.logo_image = "logo_bancointer.jpg"
        self.carteira = '112'
        self.barcode_ = '' # pegar barcode do gateway de pagamento

    @property
    def agencia_conta_cedente(self):
        return "%s / %s" % (
            self.agencia_cedente,
            self.conta_cedente)

    def format_nosso_numero(self):
        return '%s/%s/%s' %(self.agencia_cedente,self.carteira,self.nosso_numero)

    @property
    def barcode(self):
        return self.barcode_


