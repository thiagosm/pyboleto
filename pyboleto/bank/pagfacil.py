# -*- coding: utf-8
"""
    pyboleto.bank.pagfacil
    ~~~~~~~~~~~~~~~~~~~~~~

    Lógica para boletos do pagfacil.

"""
from ..data import BoletoData, CustomProperty
from datetime import date
from decimal import Decimal

class BoletoPagFacil(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o pagfacil
    '''

    nosso_numero = CustomProperty('nosso_numero', 6)
    conta_cedente = CustomProperty('convenio', 6)

    def __init__(self):
        super(BoletoPagFacil, self).__init__()
        self.codigo_banco = "099"
        self.logo_image = "logo_pagfacil.png"
        self.carteira = '2'
        self.ano = date.today().strftime("%Y")

    def format_nosso_numero(self):
        return "%6s%6s%4s-%1s" % (
            self.convenio.zfill(6),
            self.nosso_numero.zfill(6),
            self.ano,
            self.dv_nosso_numero
        )

    def calcula_dv(self,num):
        soma = 0
        i = 0
        for n in num:
            soma += (i+1) * int(n) 
            i += 1
        dv = (soma % 11) % 10
        return str(dv)

    @property
    def dv_nosso_numero(self):
        num = '%6s%6s%4s' %(self.convenio.zfill(6),
                            self.nosso_numero.zfill(6),
                            self.ano)
        return self.calcula_dv(num)

    @property
    def linha_digitavel(self):
        num = self.barcode
        return ".".join([num[0:4],         # 4     0-4
                         num[4],           # 1     4-4
                         num[5:17],        # 12    5-17
                         num[17:25],       # 8     17-25
                         num[25:31],       # 6     25-31
                         num[31:37],       # 6     31-37
                         num[37],          # 1     37-37
                         num[38:41],       # 3     38-41
                         num[41]           # 1     41-41
                         ])         

    @property
    def barcode(self):
        num = str("%3s%1s%12s%8s%17s" % (self.codigo_banco,
                                     self.carteira[0],
                                     str(int(Decimal(self.valor_documento)*100)).zfill(12),
                                     self.data_vencimento.strftime("%d%m%Y"),
                                     self.format_nosso_numero().replace('-','')))
        dv = self.calcula_dv(num)
        barcode = num[:4] + str(dv) + num[4:]
        return barcode

