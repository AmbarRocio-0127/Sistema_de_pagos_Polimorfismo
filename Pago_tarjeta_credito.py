from MetodoPago import Metodopago

class Pago_tarjeta_credito(Metodopago):
    def procesar_pago(self, value):
        comision = value * 0.05
        return comision + value