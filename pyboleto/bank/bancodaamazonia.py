# -*- coding: utf-8
from ..data import BoletoData, custom_property

class BoletoBancodaAmazonia(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco da Amazonia
        Rodapé das instruções com: ARRECADAÇÃO BASA – CONVÊNIO XXXX – AGÊNCIA ZZZ-Z
    '''

    nosso_numero = custom_property('nosso_numero', 16)
    agencia_cedente = custom_property('agencia_cedente', 4)
    conta_cedente = custom_property('conta_cedente', 7)
    convenio = custom_property('convenio', 4)

    def __init__(self):
        super(BoletoBancodaAmazonia, self).__init__()

        self.codigo_banco = "003"
        self.logo_image = "logo_bancodaamazonia.jpg"
        self.carteira = 'CNR'
        self.indicador_sistema = '8'

    def format_nosso_numero(self):
        return self.nosso_numero

    @property
    def agencia_conta_cedente(self):
        return "%s-%s / %s-%s" % (
            self.agencia_cedente[0:3],
            self.agencia_cedente[3:4],
            self.conta_cedente[0:6],
            self.conta_cedente[6:7])

    @property
    def campo_livre(self):
        content = "%4s%4s%16s%1s" % (self.agencia_cedente.zfill(4),
                                     self.convenio.zfill(4),
                                     self.nosso_numero.zfill(16),
                                     self.indicador_sistema)
        return str(content)