from MetodoPago import MetodoPago
class Compra:
    def __init__(self, valor, metodo_pago: MetodoPago):
        self.valor = valor
        self.metodo_pago = metodo_pago
        
    def calcular_total(self):
        return self.metodo_pago.procesar_pago(self.valor)