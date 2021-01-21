# -*- coding: utf-8
from ..data import BoletoData, CustomProperty


class BoletoJuno(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco juno
    '''

    nosso_numero = CustomProperty('nosso_numero', 15)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 11)

    def __init__(self):
        super(BoletoJuno, self).__init__()

        self.codigo_banco = "383"
        self.logo_image = "logo_juno.jpg"
        self.carteira = '001'
        self.barcode_ = '' # pegar barcode do gateway de pagamento

    @property
    def agencia_conta_cedente(self):
        return "%s / %s" % (
            self.agencia_cedente,
            self.conta_cedente)

    def format_nosso_numero(self):
        return self.nosso_numero

    @property
    def barcode(self):
        return self.barcode_


