# -*- coding: utf-8 -*-
from ..data import BoletoData, custom_property
from decimal import Decimal
import re 

class BoletoArrecadacao(BoletoData):
    """
    Arrecadação Febraban

    """
    carteira = custom_property('carteira', 1)

    def __init__(self):
        BoletoData.__init__(self)
        self.moeda_formato = '8'

    def dac11(self,num):
        r = self.modulo11(num,9,1)
        if r in [0,1]:
            return 0
        else:
            return 11-r

    @property
    def identificacao(self):
        return re.sub('[^0-9]','',self.convenio)

    @property
    def linha_digitavel(self):
        """Monta a linha digitável a partir do barcode

        Esta é a linha que o cliente pode utilizar para digitar se o código
        de barras não estiver legível.
        """
        linha = ''
        if self.carteira not in ['6','8']:
            self.carteira = '8'

        c1 = self.barcode[0:11]
        c2 = self.barcode[11:22]
        c3 = self.barcode[22:33]
        c4 = self.barcode[33:44]

        d1 = str(self.dac11(c1))
        d2 = str(self.dac11(c2))
        d3 = str(self.dac11(c3))
        d3 = str(self.dac11(c4))

        if self.carteira == '6':
            d1 = str(self.modulo10(c1))
            d2 = str(self.modulo10(c2))
            d3 = str(self.modulo10(c3))
            d3 = str(self.modulo10(c4))
        
        linha = '%s-%s %s-%s %s-%s %s-%s' (c1,d1,c2,d2,c3,d3,c4,d4)
        return str(linha)

    @property
    def campo_livre(self):
        doc_zfill = 17
        identp2 = ''
        if self.carteira in ['6','9']:
            identp2 = self.identificacao[4:8]

        doc_zfill -= len(identp2)
        content = "%s%8s"  % (identp2,
                              self.data_vencimento.strftime('%Y%m%d'),
                              str(self.numero_documento).zfill(doc_zfill)
                              )
        return str(content)


    @property
    def barcode(self):
        """Função para gerar código de barras para arrecadação - FEBRABAN

        Convenio: Codigo de identificacao no banco
        Carteiras: 
        1. Prefeituras;
        2. Saneamento;
        3. Energia Eletrica e Gas;
        4. Telecomunicacoes;
        5. Orgaos Governamentais;
        6. Carnes e Assemelhados 
            ou demais Empresas / Orgaos que serao identificadas atraves do CNPJ. 
        7. Multas de transito
        9. Uso exclusivo do banco

        Posição  #   Conteúdo
        01 a 01  01  produto
        02 a 02  01  segmento ( carteira )
        03 a 03  01  moeda formato
        04 a 04  01  digito verificador geral
        05 a 15  11  valor 
        # ----- Se telecomunicacao ---------
        16 a 19  04  Identificacao empresa
        20 a 44  25  Campo Livre
        # ------ Se empresa CNPJ -----------
        16 a 23  08  Identificacao Empresa e/ou ident. + codigo definido no banco
        24 a 44  21  Campo Livre 

        Total    44
        """
        if self.carteira not in ['6','8']:
            self.carteira = '8'

        barcode = '%1s%1s%1s%011d%4s%25s' %('8',
                                            self.carteira,
                                            self.moeda_formato,
                                            Decimal(self.valor_documento) * 100,
                                            self.identificacao[0:4],
                                            self.campo_livre)
        dv = self.dac11(barcode)
        if self.carteira == '6':
            dv = self.modulo10(barcode)
        return barcode[0:4] + str(dv) + barcode[4:]

