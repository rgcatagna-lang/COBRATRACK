from datetime import date

class AcuerdoPago:

    def __init__(self, cliente_id, monto, fecha_compromiso):

        if cliente_id <= 0:
            raise ValueError("Cliente inválido")

        if monto <= 0:
            raise ValueError("Monto inválido")

        if fecha_compromiso <= date.today():
            raise ValueError("Fecha inválida")

        self.cliente_id = cliente_id
        self.monto = monto
        self.fecha_compromiso = fecha_compromiso

    def obtener_estado(self):

        if self.fecha_compromiso > date.today():
            return "VIGENTE"

        return "VENCIDO"

    def resumen(self):

        return {
            "cliente": self.cliente_id,
            "monto": self.monto,
            "estado": self.obtener_estado()
        }
