# -*- coding: utf-8 -*-
from ..data import BoletoData, CustomProperty


class BoletoBanese(BoletoData):
    agencia_cedente = CustomProperty('agencia_cedente',2)
    conta_cedente = CustomProperty('conta_cedente', 9)
    nosso_numero = CustomProperty('nosso_numero', 9)

    def __init__(self):
        BoletoData.__init__(self)
        self.codigo_banco = "047"
        self.logo_image = "logo_banese.jpg"

    def _dv_nosso_numero(self):
        return str(self.modulo11(self.nosso_numero, 9, 0))

    @property
    def campo_livre(self):
        content = '%02d%09d%09d%03d' % (int(self.agencia_cedente),
                                        int(self.conta_cedente),
                                        int(self.nosso_numero),
                                        int(self.codigo_banco))
        return str('%s%s' % (content, self._dv_campo_livre(content)))


    def _dv_campo_livre(self, campo_livre):
        dv = self.modulo10(campo_livre)
        while True:
            restoMod11 = self.modulo11(campo_livre + str(dv), 7, 1)
            if restoMod11 != 1:
                break
            dv += 1
            dv %= 10

        return str(dv) + str(11 - restoMod11)
