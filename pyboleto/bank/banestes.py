# -*- coding: utf-8
from ..data import BoletoData, CustomProperty
from datetime import date

class BoletoBanestes(BoletoData):

    nosso_numero = CustomProperty('nosso_numero', 11)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 7)

    def __init__(self):
        super(BoletoBanestes, self).__init__()

        self.codigo_banco = "021"
        self.logo_image = "logo_bancobanestes.jpg"
        self.carteira = '1'

    @property
    def _nosso_numero_f(self):
        return str(self.nosso_numero)[-8:].zfill(8)

    def format_nosso_numero(self):
        nosso_numero_f = self._nosso_numero_f
        dv1 = self.get_dv_nosso_numero(nosso_numero_f, '0908070605040302')
        dv2 = self.get_dv_nosso_numero('%s%s' % (nosso_numero_f, dv1), '100908070605040302')

        return "%s%s%s" % (nosso_numero_f, dv1, dv2)
    
    def dv_nosso_numero(self, nosso_numero_f, produto):
        _c = produto
        _t = tuple(nosso_numero_f)
        dv = _z = 0

        j = 0
        for i in range(len(_t)):
            _z += int(_t[i]) * int('%s%s' % (_c[j],_c[j+1]))
            j += 2

        resto = _z % 11

        if resto in [0, 1]:
            dv = 0
        else:
            dv = 11 - resto 

        return dv
        
    @property
    def campo_livre(self):
        campo_livre = "%s%s%s%s" % (
            self._nosso_numero_f,
            str(int(self.conta_cedente[-11:])).zfill(11),
            '4', # com registro
            self.codigo_banco
        )

        return "%s%s" % (campo_livre, self._dv_campo_livre(campo_livre))

    def _dv_campo_livre(self, campo_livre):
        dv1 = 0
        dv2 = 0

        # dv1
        _c = '21212121212121212121212'
        _t = tuple(campo_livre)
        _z = 0

        for i in range(len(_t)):
            p = int(_t[i]) * int(_c[i])
            
            if p > 9:
                _z += (p - 9)
            else:
                _z += p

        resto = _z % 10
        
        if resto == 0:
            dv1 = 0
        else:
            dv1 = 10 - resto

        # dv2
        def calc_dv2(campo_livre, dv1):
            _c = '765432765432765432765432'
            _t = tuple('%s%s' % (campo_livre, dv1))
            _z = 0

            for i in range(len(_t)):
                _z += int(_t[i]) * int(_c[i])

            resto = _z % 11

            if resto == 0:
                return dv1, resto
            elif resto == 1:
                if dv1 < 9:
                    return calc_dv2(campo_livre, dv1 + 1)
                else:
                    return calc_dv2(campo_livre, 0)
            else:
                return dv1, 11 - resto

        dv1, dv2 = calc_dv2(campo_livre, dv1)
                
        return "%s%s" % (dv1, dv2)