# -*- coding: utf-8
from ..data import BoletoData, CustomProperty


class BoletoLocalGateway(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco local gateway
    '''

    nosso_numero = CustomProperty('nosso_numero', 18)
    agencia_cedente = CustomProperty('agencia_cedente', 5)
    conta_cedente = CustomProperty('conta_cedente', 8)

    def __init__(self):
        super(BoletoInter, self).__init__()

        self.codigo_banco = "localgateway"
        self.logo_image = ""
        self.carteira = ''
        self.barcode_ = '' # pegar barcode do gateway de pagamento

    @property
    def agencia_conta_cedente(self):
        return " "

    def format_nosso_numero(self):
        return self.nosso_numero

    @property
    def barcode(self):
        return self.barcode_


 