from MetodoPago import Metodopago

class Pago_criptomonedas(Metodopago):
    def procesar_pago(self, value):
        comision = value * 0.10
        return comision + value