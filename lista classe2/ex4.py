class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

        if not self._verificar_data():
            raise ValueError("Data inválida.")

    def _verificar_data(self):
        if self.dia < 1 or self.dia > 31:
            return False
    
        if self.mes < 1 or self.mes > 12:
            return False
        
        if self.ano <= 0:
            return False

        if self.mes in [4, 6, 9, 11] and self.dia > 30:
            return False
        elif self.mes == 2:
            if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
                if self.dia > 29:
                    return False
            elif self.dia > 28:
                return False
        
        return True

    def retornar_data(self):
        return "{:02d}/{:02d}/{:04d}".format(self.dia, self.mes, self.ano)

    def dia_seguinte(self):
        dia_max = 31
        if self.mes in [4, 6, 9, 11]:
            dia_max = 30
        elif self.mes == 2:
            if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
                dia_max = 29
            else:
                dia_max = 28
        
        if self.dia == dia_max:
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1
        else:
            self.dia += 1
try:
    data1 = Data(31, 12, 2021)
    print("Data:", data1.retornar_data())
    data1.dia_seguinte()
    print("Data do dia seguinte:", data1.retornar_data())
except ValueError as e:
    print(e)

