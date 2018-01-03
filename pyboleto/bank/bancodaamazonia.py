# -*- coding: utf-8
from ..data import BoletoData, CustomProperty

class BoletoBancodaAmazonia(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco da Amazonia
        Rodapé das instruções com: ARRECADAÇÃO BASA – CONVÊNIO XXXX – AGÊNCIA ZZZ-Z
    '''

    nosso_numero = CustomProperty('nosso_numero', 16)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 7)
    convenio = CustomProperty('convenio', 4)

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
        content = ""
        # Boleto sem registro
        if self.indicador_sistema == '8':
            content = "%4s%4s%16s%1s" % (self.agencia_cedente.zfill(4),
                                         self.convenio.zfill(4),
                                         self.nosso_numero.zfill(16),
                                         self.indicador_sistema)
        # Boleto com registro
        elif self.indicador_sistema == '0':
            venc_ddmmyy = '000000'
            if self.data_vencimento:
                venc_ddmmyy = self.data_vencimento.strftime('%d%m%y')  
            content = "%4s%7s%6s%7s%1s" % (self.agencia_cedente.zfill(4),
                                         self.nosso_numero[-7:].zfill(7),
                                         venc_ddmmyy,
                                         '0000000',
                                         self.indicador_sistema)
        return str(content)
