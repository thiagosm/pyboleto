#-*- coding: utf-8 -*-
from ..data import BoletoData, custom_property


class BoletoCaixa(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Caixa
        Economica Federal

    '''

    conta_cedente = custom_property('conta_cedente', 11)
    '''
        Este numero tem o inicio fixo
        Carteira SR: 80, 81 ou 82
        Carteira CR: 90 (Confirmar com gerente qual usar)

    '''
    nosso_numero = custom_property('nosso_numero', 10)

    def __init__(self):
        super(BoletoCaixa, self).__init__()

        self.codigo_banco = "104"
        self.local_pagamento = "Preferencialmente nas Casas Lotéricas e \
Agências da Caixa"
        self.logo_image = "logo_bancocaixa.jpg"

    @property
    def dv_nosso_numero(self):
        resto2 = self.modulo11(self.nosso_numero.split('-')[0], 9, 1)
        digito = 11 - resto2
        if digito == 10 or digito == 11:
            dv = 0
        else:
            dv = digito
        return dv

    @property
    def campo_livre(self):
        content = "%10s%4s%11s" % (self.nosso_numero,
                                   self.agencia_cedente,
                                   self.conta_cedente.split('-')[0])
        return content

    def format_nosso_numero(self):
        return self.nosso_numero + '-' + str(self.dv_nosso_numero)
        

class BoletoCaixa17(BoletoCaixa):
    """
       Geração de boleto com nosso número de 17 dígitos + DV.
    """
    nosso_numero = custom_property('nosso_numero', 16)
    agencia_cedente = custom_property('agencia_cedente', 4)
    conta_cedente = custom_property('conta_cedente', 6)

    def __init__(self,inicio_nosso_numero):
        super(BoletoCaixa2, self).__init__()
        self.inicio_nosso_numero = inicio_nosso_numero

    @property
    def dv_nosso_numero(self):
        resto2 = self.modulo11('%s%s' %(self.inicio_nosso_numero,
                                        self.nosso_numero.split('-')[0]), 9, 1)
        digito = 11 - resto2
        if digito == 10 or digito == 11:
            dv = 0
        else:
            dv = digito
        return dv

    @property
    def campo_livre(self):
        content = str("%1s%6s%2s%16s" % (self.inicio_nosso_numero[1],
                                         self.conta_cedente.split('-')[0],
                                         self.inicio_nosso_numero,
                                         self.nosso_numero))
        return content

    def format_nosso_numero(self):
        return str('%s%s' %(self.inicio_nosso_numero,
                            self.nosso_numero + '-' + str(self.dv_nosso_numero)))


        
class BoletoCaixaSIGCB(BoletoCaixa):
    '''
        Gera Dados necessários para criação de boleto para o banco Caixa
        Economica Federal - SIGCB
    '''
    
    nosso_numero = custom_property('nosso_numero', 15)
    agencia_cedente = custom_property('agencia_cedente', 4)
    conta_cedente = custom_property('conta_cedente', 6)
    
    def __init__(self,inicio_nosso_numero='24'):
        super(BoletoCaixaSIGCB, self).__init__()
        self.inicio_nosso_numero = inicio_nosso_numero # 24 - 2=sem registro,  
                                                       #      4=emitido pelo proprio cliente
        

    @property
    def dv_conta_cedente(self):
        resto2 = self.modulo11(self.conta_cedente.split('-')[0], 9, 1)
        digito = 11 - resto2
        if digito == 10 or digito == 11:
            dv = 0
        else:
            dv = digito
        return dv

    @property
    def agencia_conta_cedente(self):
        return "%s / %s-%s" % (
            self.agencia_cedente,
            self.conta_cedente.split('-')[0],
            self.dv_conta_cedente)


    @property
    def campo_livre(self):
        content = "%s%s%s%s%s%s%s" %(self.conta_cedente.split('-')[0],
                                   self.dv_conta_cedente,
                                   self.nosso_numero[:3],
                                   self.inicio_nosso_numero[0:1],
                                   self.nosso_numero[3:6],
                                   self.inicio_nosso_numero[1:2],
                                   self.nosso_numero[6:15])
        return str("%s%s" %(content,self._dv_num(content)))                

    def _dv_num(self, num):
        resto2 = self.modulo11(num.split('-')[0], 9, 1)
        digito = 11 - resto2
        if digito == 10 or digito == 11:
            dv = 0
        else:
            dv = digito
        return dv    


    def format_nosso_numero(self):
        nnum = "%s%s%s%s" % (
                                self.inicio_nosso_numero[0:2],
                                self.nosso_numero[:3],
                                self.nosso_numero[3:6],
                                self.nosso_numero[6:15]
                            )
        nossonumero = '%s%s' %(nnum,self._dv_num(nnum))

        return nossonumero    
        

                        

        
