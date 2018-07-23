# -*- coding: utf-8
"""
    pyboleto.bank.brb
    ~~~~~~~~~~~~~~~~~~~~~~~
"""
from ..data import BoletoData, CustomProperty


class BoletoBrb(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco BRB
    '''

    nosso_numero = CustomProperty('nosso_numero', 6)

    #: Também chamado de "ponto de venda"
    agencia_cedente = CustomProperty('agencia_cedente', 3)

    #: Também chamdo de código do cedente, se for uma conta de 9 dígitos
    #: ignorar os 2 primeiros
    conta_cedente = CustomProperty('conta_cedente', 7)

    def __init__(self):
        super(BoletoBrb, self).__init__()

        self.codigo_banco = "070"
        self.logo_image = "logo_brb.jpg"
        self.carteira = 'COB'
        self.modalidade_cobranca = '1'  # 1 ou 2 


    @property
    def agencia_conta_cedente(self):
        return "000-%s-%s" % (self.agencia_cedente.zfill(3),
                              self.conta_cedente.zfill(7))

    def format_nosso_numero(self):
        return self.campo_livre[13:]

    def dv_campo_livre(self,chave,d1):
        modulo = self.modulo11('%s%s' %(str(chave),str(d1)), 7, 1)
        if modulo == 0:
            d2 = 0
            return d1,d2
        elif modulo > 1:
            d2 = 11 - modulo
            return d1,d2
        elif modulo == 1:
            d1 += 1
            if d1 == 10:
                d1 = 0
            self.dv_campo_livre(chave,d1)


    @property
    def campo_livre(self):
        chave = "000%3s%7s%1s%6s%3s" %(self.agencia_cedente.zfill(3),
                                       self.conta_cedente.zfill(7),
                                       self.modalidade_cobranca,
                                       self.nosso_numero.zfill(6),
                                       self.codigo_banco)
        d_chave = self.modulo10(chave)
        d1,d2 = self.dv_campo_livre(chave,d_chave)
        return str('%s%s%s' %(chave,d1,d2))

