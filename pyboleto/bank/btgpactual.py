# -*- coding: utf-8
from ..data import BoletoData, CustomProperty
import re

class BoletoBtgPactual(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Inter
    '''

    nosso_numero = CustomProperty('nosso_numero', 15)
    agencia_cedente = CustomProperty('agencia_cedente', 5)
    conta_cedente = CustomProperty('conta_cedente', 10)

    def __init__(self):
        super(BoletoBtgPactual, self).__init__()

        self.codigo_banco = "208"
        self.logo_image = "logo_btgpactual.jpg"
        self.carteira = '50'
        self.barcode_ = '' # pegar barcode do gateway de pagamento

    @property
    def agencia_conta_cedente(self):
        return self.conta_cedente

    def format_nosso_numero(self):
        return self.nosso_numero

    @property
    def barcode(self):
        return self.barcode_


