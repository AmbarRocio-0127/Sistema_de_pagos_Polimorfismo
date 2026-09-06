from MetodoPago import Metodopago

class Compra:
    def __init__(self, value, metodopago: Metodopago):
        self.value = value
        self.metodopago = metodopago
        
    def calcular_compra(self):
        return self.metodopago.procesar_pago(self.value)