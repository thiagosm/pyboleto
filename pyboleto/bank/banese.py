# -*- coding: utf-8 -*-
from ..data import BoletoData, CustomProperty
from decimal import Decimal


class BoletoBanese(BoletoData):
    agencia_cedente = CustomProperty('agencia_cedente',2)
    conta_cedente = CustomProperty('conta_cedente', 9)
    nosso_numero = CustomProperty('nosso_numero', 9)

    def __init__(self):
        BoletoData.__init__(self)
        self.codigo_banco = "047"
        self.logo_image = "logo_banese.jpg"

    @property
    def _nosso_numero_f(self):
        return "%s%s" % (
            str(int(self.agencia_cedente[-3:])).zfill(3),
            str(self.nosso_numero)[-8:].zfill(8),
        )

    def format_nosso_numero(self):        
        return "%s%s" % (
            str(self.nosso_numero)[-8:].zfill(8),
            str(self.dv_nosso_numero)[0]
        )

    @property
    def dv_nosso_numero(self):
        _c = '43298765432'
        _t = tuple(self._nosso_numero_f)
        dv = _z = 0

        for i in range(len(_t)):
            _z += int(_t[i]) * int(_c[i])

        resto = _z % 11

        if resto in [0, 1]:
            dv = 0
        else:
            dv = 11 - resto 

        return dv

    @property
    def campo_livre(self):
        campo_livre = "%s%s%s%s" % (
            str(int(self.agencia_cedente[-2:])).zfill(2),
            str(int(self.conta_cedente[-9:])).zfill(9),
            self.format_nosso_numero(),
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
