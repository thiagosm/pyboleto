#-*- coding: utf-8 -*-
from ..data import BoletoData, custom_property

from caixa import BoletoCaixa

class CaixaSigcb(BoletoCaixa):
    '''
        Gera Dados necessários para criação de boleto para o banco Caixa
        Economica Federal - SIGCB
    '''
    
    def __init__(self,inicio_nosso_numero='24'):
        super(CaixaSigcb, self).__init__()
        self.inicio_nosso_numero = inicio_nosso_numero # 2=sem registro,  4=emitido pelo proprio cliente
        
    nosso_numero = custom_property('nosso_numero', 15)
    agencia_cedente = custom_property('agencia_cedente', 4)
    conta_cedente = custom_property('conta_cedente', 6)
    
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
    def campo_livre(self):
        content = "%s%s%s%s%s%s" %(self.conta_cedente,
                                   self.dv_conta_cedente,
                                   self.nosso_numero[:3],
                                   self.inicio_nosso_numero[0:1],
                                   self.nosso_numero[3:6],
                                   self.inicio_nosso_numero[1:2],
                                   self.nosso_numero[6:15])
        return "%s%s" %(content,self._dv_num(content))                
    
    def _dv_num(self, num):

        resto2 = self.modulo11(num, 9, 1)
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
        
        return nnum        
        
        