# -*- coding: utf-8
from ..data import BoletoData, CustomProperty


class BoletoJuno(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Inter
    '''

    nosso_numero = CustomProperty('nosso_numero', 15)
    agencia_conta = CustomProperty('conta_cedente', 15)

    def __init__(self):
        super(BoletoJuno, self).__init__()

        self.codigo_banco = "383"
        self.logo_image = "logo_juno.jpg"
        self.carteira = '0000'
        self.barcode_ = '' # pegar barcode do gateway de pagamento

    @property
    def agencia_conta_cedente(self):
        return self.agencia_conta

    def format_nosso_numero(self):
        return self.nosso_numero

    @property
    def barcode(self):
        return self.barcode_


