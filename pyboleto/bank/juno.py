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
        self.carteira = '0001'
        self.barcode_ = '' # pegar barcode do gateway de pagamento
        self.linha_digitavel_ = '' # pegar linha_digitavel do gateway de pagamento

    @property
    def agencia_conta_cedente(self):
        return self.agencia_conta

    def format_nosso_numero(self):
        return self.nosso_numero

    @property
    def barcode(self):
        return self.barcode_

    @property
    def linha_digitavel(self):
        if not self.linha_digitavel_:
            linha = self.barcode
            if not linha:
                raise BoletoException("Boleto doesn't have a barcode")

            def monta_campo(campo):
                campo_dv = "%s%s" % (campo, self.modulo10(campo))
                return "%s.%s" % (campo_dv[0:5], campo_dv[5:])

            return ' '.join([monta_campo(linha[0:4] + linha[19:24]),
                             monta_campo(linha[24:34]),
                             monta_campo(linha[34:44]),
                             linha[4],
                             linha[5:19]])

        return self.linha_digitavel_